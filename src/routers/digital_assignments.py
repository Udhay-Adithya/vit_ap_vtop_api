from typing import List

from fastapi import APIRouter, Depends

from src.dependencies import verify_api_key
from src.models.api_models import CourseAssignmentsRequest, DigitalAssignmentsRequest
from src.routers._common import client_for, vtop_errors

from vitap_vtop_client.digital_assignment import (
    AssignmentRecordModel,
    DigitalAssignmentModel,
)

router = APIRouter(
    prefix="/student/digital_assignments",
    tags=["digital assignments"],
    dependencies=[Depends(verify_api_key)],
)


@router.post("", response_model=List[DigitalAssignmentModel])
async def get_digital_assignments(request: DigitalAssignmentsRequest):
    """
    Fetches every course's digital assignments for a semester.

    VTOP serves the course list and each course's assignments from separate
    endpoints, so this fans out one request per course. That is deliberate but
    not cheap -- prefer /student/digital_assignments/course when you already
    know the class id.
    """
    async with vtop_errors():
        async with client_for(request.session) as client:
            return await client.get_digital_assignments(sem_sub_id=request.sem_sub_id)


@router.post("/course", response_model=List[AssignmentRecordModel])
async def get_course_assignments(request: CourseAssignmentsRequest):
    """Fetches one course's digital assignments by class id."""
    async with vtop_errors():
        async with client_for(request.session) as client:
            return await client.get_course_assignments(class_id=request.class_id)
