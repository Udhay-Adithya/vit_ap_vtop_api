import asyncio
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from dependencies import verify_api_key
from models.api_models import (
    BaseVtopRequest,
    AttendanceRequest,
    BiometricRequest,
    TimetableRequest,
    ComprehensiveDataRequest,
    ComprehensiveDataResponse,
)
from vitap_vtop_client.client import VtopClient

from vitap_vtop_client.attendance import AttendanceModel
from vitap_vtop_client.profile import StudentProfileModel
from vitap_vtop_client.timetable import TimetableModel
from vitap_vtop_client.biometric import BiometricModel
from vitap_vtop_client.grade_history import GradeHistoryModel
from vitap_vtop_client.mentor import MentorModel

from vitap_vtop_client.exceptions import VitapVtopClientError

from src.utils.handle_client_exception import handle_client_exception


router = APIRouter(
    prefix="/student",
    tags=["student"],
    # API Key dependency to apply to all routes in this router
    dependencies=[Depends(verify_api_key)],
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
        async with VtopClient(
            registration_number=request.registration_number, password=request.password
        ) as client:

            profile_task = client.get_profile()
            attendance_task = client.get_attendance(sem_sub_id=request.sem_sub_id)
            timetable_task = client.get_timetable(sem_sub_id=request.sem_sub_id)

            # Fetch data concurrently using asyncio.gather
            # Await all tasks concurrently. If any task raises an exception,
            # asyncio.gather will cancel the others and re-raise the first exception.
            profile_data, attendance_data, timetable_data = await asyncio.gather(
                profile_task, attendance_task, timetable_task
            )

            # Construct the response object using the fetched data
            comprehensive_data = ComprehensiveDataResponse(
                profile=profile_data,
                attendance=attendance_data,
                timetable=timetable_data,
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
        async with VtopClient(
            registration_number=request.registration_number, password=request.password
        ) as client:
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
        async with VtopClient(
            registration_number=request.registration_number, password=request.password
        ) as client:
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
        async with VtopClient(
            registration_number=request.registration_number, password=request.password
        ) as client:
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
        async with VtopClient(
            registration_number=request.registration_number, password=request.password
        ) as client:
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
        async with VtopClient(
            registration_number=request.registration_number, password=request.password
        ) as client:
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
        async with VtopClient(
            registration_number=request.registration_number, password=request.password
        ) as client:
            mentor_details = await client.get_mentor()
            return mentor_details
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


# Add more POST endpoints here for other client methods (marks, payments, etc.)
# They will follow the same pattern: accept a request model (inheriting from BaseVtopRequest
# and adding specific parameters), create client within async with, call client method,
# handle exceptions.
