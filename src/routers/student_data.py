import asyncio
from contextlib import asynccontextmanager

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from src.dependencies import verify_api_key
from src.models.api_models import (
    AttendanceDetailRequest,
    CapstoneAttendanceRequest,
    GradeViewRequest,
    GradeViewDetailRequest,
    BaseVtopRequest,
    AttendanceRequest,
    BiometricRequest,
    TimetableRequest,
    ExamScheduleRequest,
    MarksRequest,
    ComprehensiveDataRequest,
    ComprehensiveDataResponse,
)
from vitap_vtop_client import RestorableSession, VtopClient

from vitap_vtop_client.attendance import (
    AttendanceDetailModel,
    AttendanceModel,
    CapstoneAttendanceModel,
)
from vitap_vtop_client.grade_view import GradeViewCourse, GradeViewDetail
from vitap_vtop_client.profile import StudentProfileModel
from vitap_vtop_client.timetable import TimetableModel
from vitap_vtop_client.biometric import BiometricModel
from vitap_vtop_client.grade_history import GradeHistoryModel
from vitap_vtop_client.mentor import MentorModel
from vitap_vtop_client.exam_schedule import ExamScheduleModel
from vitap_vtop_client.marks import MarksModel
from vitap_vtop_client.outing import GeneralOutingModel, WeekendOutingModel
from vitap_vtop_client.payments import PendingPayment, PaymentReceipt
from vitap_vtop_client.semester import SemesterData

from vitap_vtop_client.exceptions import VitapVtopClientError

from src.routers._common import vtop_errors
from src.utils.handle_client_exception import handle_client_exception


router = APIRouter(
    prefix="/student",
    tags=["student"],
    # API Key dependency to apply to all routes in this router
    dependencies=[Depends(verify_api_key)],
)


@asynccontextmanager
async def _client_for(session: RestorableSession):
    """Rebuilds the caller's VTOP session for the life of one request.

    VTOP holds the session server side against its cookie, so this costs no
    requests and no login. The client carries no password, so if the session has
    expired it raises rather than silently logging in again -- the caller has to
    go back through /auth/login, which may need an OTP only they can answer.
    """
    client = VtopClient.restore(
        registration_number=session.registration_number,
        cookie=session.cookie,
        csrf_token=session.csrf_token,
        user_agent=session.user_agent,
    )
    try:
        yield client
    finally:
        await client.close()


@router.post("/semesters", response_model=SemesterData)
async def get_semesters(request: BaseVtopRequest):
    """
    Fetches the semesters available to the student.

    The ids returned here are what every sem_sub_id parameter on the other
    endpoints expects, so prefer this over hardcoding semester ids.
    """
    try:
        async with _client_for(request.session) as client:
            semesters = await client.get_semesters()
            return semesters
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


# All data endpoints will taking credentials in the body.
@router.post("/all_data", response_model=ComprehensiveDataResponse)
async def get_all_student_data(request: ComprehensiveDataRequest):
    """
    Fetches comprehensive student data (profile, attendance, timetable)
    for the specified semester using VTOP credentials.

    This endpoint combines multiple data fetches into a single request
    for efficient initial data loading/caching in frontend applications.
    """
    try:
        async with _client_for(request.session) as client:

            # get_profile fetches grade history itself to populate its nested
            # field, and we fetch it again below for the top level one. That is
            # the same 137KB page twice in one request, so ask the profile to
            # skip it and attach the copy we already have.
            profile_task = client.get_profile(include_grade_history=False)
            attendance_task = client.get_attendance(sem_sub_id=request.sem_sub_id)
            timetable_task = client.get_timetable(sem_sub_id=request.sem_sub_id)
            exam_schedule_task = client.get_exam_schedule(sem_sub_id=request.sem_sub_id)
            grade_history_task = client.get_grade_history()
            marks_task = client.get_marks(sem_sub_id=request.sem_sub_id)

            # Fetch data concurrently using asyncio.gather
            # Await all tasks concurrently. If any task raises an exception,
            # asyncio.gather will cancel the others and re-raise the first exception.
            (
                profile_data,
                attendance_data,
                timetable_data,
                exam_schedule_data,
                grade_history_data,
                marks_data,
            ) = await asyncio.gather(
                profile_task,
                attendance_task,
                timetable_task,
                exam_schedule_task,
                grade_history_task,
                marks_task,
            )

            # The profile was fetched without its grade history; it is the
            # same data we fetched separately, so fill it back in.
            profile_data.grade_history = grade_history_data

            # Construct the response object using the fetched data
            comprehensive_data = ComprehensiveDataResponse(
                profile=profile_data,
                attendance=attendance_data,
                timetable=timetable_data,
                grade_history=grade_history_data,
                exam_schedule=exam_schedule_data,
                marks=marks_data,
            )

            return comprehensive_data

    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


# All data endpoints will now be POST requests, taking credentials in the body.
@router.post("/profile", response_model=StudentProfileModel)
async def get_profile(request: BaseVtopRequest):
    """
    Fetches the student's profile information using VTOP credentials.
    """
    try:
        async with _client_for(request.session) as client:
            profile_data = await client.get_profile()
            return profile_data
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/attendance", response_model=List[AttendanceModel])
async def get_attendance(request: AttendanceRequest):
    """
    Fetches attendance data for the specified semester using VTOP credentials.
    """
    try:
        async with _client_for(request.session) as client:
            attendance_data = await client.get_attendance(sem_sub_id=request.sem_sub_id)
            return attendance_data
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/biometric", response_model=List[BiometricModel])
async def get_biometric(request: BiometricRequest):
    """
    Fetches biometric (entry/exit) logs for a specific date using VTOP credentials.
    """
    try:
        async with _client_for(request.session) as client:
            biometric_logs = await client.get_biometric(date=request.date)
            return biometric_logs
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/timetable", response_model=TimetableModel)
async def get_timetable(request: TimetableRequest):
    """
    Fetches the timetable for the specified semester using VTOP credentials.
    """
    try:
        async with _client_for(request.session) as client:
            timetable_data = await client.get_timetable(sem_sub_id=request.sem_sub_id)
            return timetable_data
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/grade_history", response_model=GradeHistoryModel)
async def get_grade_history(request: BaseVtopRequest):
    """
    Fetches the student's grade history (CGPA, credits registered/earned) using VTOP credentials.
    """
    try:
        async with _client_for(request.session) as client:
            grade_history_data = await client.get_grade_history()
            return grade_history_data
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/mentor", response_model=MentorModel)
async def get_mentor(request: BaseVtopRequest):
    """
    Fetches details of the student's assigned mentor using VTOP credentials.
    """
    try:
        async with _client_for(request.session) as client:
            mentor_details = await client.get_mentor()
            return mentor_details
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/exam_schedule", response_model=ExamScheduleModel)
async def get_exam_schedule(request: ExamScheduleRequest):
    """
    Fetches all exam schedule for the specified semester using VTOP credentials
    """
    try:
        async with _client_for(request.session) as client:
            exam_schedule = await client.get_exam_schedule(
                sem_sub_id=request.sem_sub_id
            )
            return exam_schedule
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/marks", response_model=MarksModel)
async def get_marks(request: MarksRequest):
    """
    Fetches all the marks for the specified semester using VTOP credentials
    """
    try:
        async with _client_for(request.session) as client:
            exam_schedule = await client.get_marks(sem_sub_id=request.sem_sub_id)
            return exam_schedule
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/general_outing_requests", response_model=GeneralOutingModel)
async def get_general_outing_responses(request: BaseVtopRequest):
    """
    Fetches all the previously submitted Genneral Outing requests.
    """
    try:
        async with _client_for(request.session) as client:
            exam_schedule = await client.get_general_outing_requests()
            return exam_schedule
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/weekend_outing_requests", response_model=WeekendOutingModel)
async def get_weekend_outing_responses(request: BaseVtopRequest):
    """
    Fetches all the previously submitted Weekend Outing requests
    """
    try:
        async with _client_for(request.session) as client:
            exam_schedule = await client.get_weekend_outing_requests()
            return exam_schedule
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/pending_payments", response_model=List[PendingPayment])
async def get_pending_payments(request: BaseVtopRequest):
    """
    Fetches the list of pending payments.
    """
    try:
        async with _client_for(request.session) as client:
            pending_payments = await client.get_pending_payments()
            return pending_payments
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/payment_receipts", response_model=List[PaymentReceipt])
async def get_payment_receipts(request: BaseVtopRequest):
    """
    Fetches the list of pending payments.
    """
    try:
        async with _client_for(request.session) as client:
            payment_receipts = await client.get_payment_receipts()
            return payment_receipts
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/attendance_detail", response_model=List[AttendanceDetailModel])
async def get_attendance_detail(request: AttendanceDetailRequest):
    """
    Fetches the per-class register behind one course's attendance row.

    `course_id` and `course_type` come from an entry in /student/attendance --
    its `course_id` and `course_type_code`. Neither is the course code.
    """
    async with vtop_errors():
        async with _client_for(request.session) as client:
            return await client.get_attendance_detail(
                sem_sub_id=request.sem_sub_id,
                course_id=request.course_id,
                course_type=request.course_type,
            )


@router.post("/capstone_attendance", response_model=Optional[CapstoneAttendanceModel])
async def get_capstone_attendance(request: CapstoneAttendanceRequest):
    """
    Fetches capstone/SDP attendance for a semester.

    Kept apart from /student/attendance because VTOP counts it per semester
    rather than per course. Students without a capstone get null, which is a
    normal answer rather than an error.
    """
    async with vtop_errors():
        async with _client_for(request.session) as client:
            return await client.get_capstone_attendance(sem_sub_id=request.sem_sub_id)


@router.post("/grade_view", response_model=List[GradeViewCourse])
async def get_grade_view(request: GradeViewRequest):
    """
    Fetches the graded courses of a semester.

    Grades appear only once a semester has ended, so the current semester
    returns an empty list until results publish. That is expected.
    """
    async with vtop_errors():
        async with _client_for(request.session) as client:
            return await client.get_grade_view(sem_sub_id=request.sem_sub_id)


@router.post("/grade_view_detail", response_model=GradeViewDetail)
async def get_grade_view_detail(request: GradeViewDetailRequest):
    """
    Fetches one course's mark breakdown and class statistics.

    `course_id` comes from an entry in /student/grade_view.
    """
    async with vtop_errors():
        async with _client_for(request.session) as client:
            return await client.get_grade_view_detail(
                sem_sub_id=request.sem_sub_id, course_id=request.course_id
            )
