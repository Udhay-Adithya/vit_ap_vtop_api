from typing import List

from fastapi import APIRouter, Depends

from src.dependencies import verify_api_key
from src.models.api_models import FacultyDetailsRequest, FacultySearchRequest
from src.models.auth_models import SessionRequest
from src.routers._common import client_for, vtop_errors

from vitap_vtop_client.faculty import FacultyDetailsModel, FacultyModel

router = APIRouter(
    prefix="/student/faculty",
    tags=["faculty"],
    dependencies=[Depends(verify_api_key)],
)


@router.post("/search", response_model=FacultyModel)
async def search_faculty(request: FacultySearchRequest):
    """
    Searches the faculty directory and returns the first match.

    The search term is a name or an employee id. An empty model comes back when
    nothing matches, rather than an error.
    """
    async with vtop_errors():
        async with client_for(request.session) as client:
            return await client.search_faculty(request.search_term)


@router.post("", response_model=List[FacultyModel])
async def get_all_faculty(request: SessionRequest):
    """
    Fetches the entire faculty directory.

    This is a large response -- around 850 records -- so cache it rather than
    calling it per page view.
    """
    async with vtop_errors():
        async with client_for(request.session) as client:
            return await client.get_all_faculty()


@router.post("/details", response_model=FacultyDetailsModel)
async def get_faculty_details(request: FacultyDetailsRequest):
    """Fetches one faculty member's profile and weekly office hours."""
    async with vtop_errors():
        async with client_for(request.session) as client:
            return await client.get_faculty_details(request.emp_id)
