from typing import List

from fastapi import APIRouter, Depends

from src.dependencies import verify_api_key
from src.models.api_models import (
    CalendarMonthRequest,
    CalendarRequest,
    ClassGroupsRequest,
)
from src.routers._common import client_for, vtop_errors

from vitap_vtop_client.academic_calendar import (
    AcademicCalendarModel,
    CalendarDayModel,
    CalendarMonthRefModel,
    ClassGroupModel,
)

router = APIRouter(
    prefix="/student/calendar",
    tags=["calendar"],
    dependencies=[Depends(verify_api_key)],
)


@router.post("/class_groups", response_model=List[ClassGroupModel])
async def get_class_groups(request: ClassGroupsRequest):
    """
    Fetches the calendar class groups available for a semester.

    Class groups are semester dependent, so list them here rather than assuming
    the "COMB" default the other calendar endpoints use.
    """
    async with vtop_errors():
        async with client_for(request.session) as client:
            return await client.get_calendar_class_groups(sem_sub_id=request.sem_sub_id)


@router.post("/months", response_model=List[CalendarMonthRefModel])
async def get_months(request: CalendarRequest):
    """Fetches the months the calendar covers for a semester."""
    async with vtop_errors():
        async with client_for(request.session) as client:
            return await client.get_calendar_months(
                sem_sub_id=request.sem_sub_id, class_group_id=request.class_group_id
            )


@router.post("/month", response_model=List[CalendarDayModel])
async def get_month(request: CalendarMonthRequest):
    """Fetches a single month of the calendar, day by day."""
    async with vtop_errors():
        async with client_for(request.session) as client:
            return await client.get_calendar_month(
                sem_sub_id=request.sem_sub_id,
                cal_date=request.cal_date,
                class_group_id=request.class_group_id,
            )


@router.post("", response_model=AcademicCalendarModel)
async def get_academic_calendar(request: CalendarRequest):
    """
    Fetches the whole semester's calendar as one date-ordered list of days.

    This walks every month, so it is several requests against VTOP. Prefer
    /student/calendar/month when you only need one.
    """
    async with vtop_errors():
        async with client_for(request.session) as client:
            return await client.get_academic_calendar(
                sem_sub_id=request.sem_sub_id, class_group_id=request.class_group_id
            )
