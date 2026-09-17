from fastapi import APIRouter, Depends

from src.dependencies import verify_api_key
from src.models.api_models import (
    CourseDetailRequest,
    CoursePageCoursesRequest,
    CoursePageSlotsRequest,
)
from src.routers._common import client_for, vtop_errors

from vitap_vtop_client.course_page import (
    CoursePageDetailModel,
    CoursesResponseModel,
    SlotsResponseModel,
)

router = APIRouter(
    prefix="/student/course_page",
    tags=["course page"],
    dependencies=[Depends(verify_api_key)],
)

# VTOP will not answer the course page's lookups until StudentCoursePage has
# been opened on that session. Each request here restores a fresh client, so
# the page has to be opened every time -- unlike the redundant primes removed
# from the other read paths, this one VTOP genuinely enforces.


@router.post("/courses", response_model=CoursesResponseModel)
async def get_courses(request: CoursePageCoursesRequest):
    """Fetches the courses in the course page's dropdown for a semester."""
    async with vtop_errors():
        async with client_for(request.session) as client:
            await client.init_course_page()
            return await client.get_course_page_courses(sem_sub_id=request.sem_sub_id)


@router.post("/slots", response_model=SlotsResponseModel)
async def get_slots(request: CoursePageSlotsRequest):
    """
    Fetches the slots for one course, along with its class rows.

    `class_id` comes from /student/course_page/courses.
    """
    async with vtop_errors():
        async with client_for(request.session) as client:
            await client.init_course_page()
            return await client.get_course_page_slots(
                sem_sub_id=request.sem_sub_id, class_id=request.class_id
            )


@router.post("/detail", response_model=CoursePageDetailModel)
async def get_course_detail(request: CourseDetailRequest):
    """
    Fetches a course's lectures and reference material.

    `erp_id` and `class_id` both come from /student/course_page/slots.
    """
    async with vtop_errors():
        async with client_for(request.session) as client:
            await client.init_course_page()
            return await client.get_course_detail(
                sem_sub_id=request.sem_sub_id,
                erp_id=request.erp_id,
                class_id=request.class_id,
            )
