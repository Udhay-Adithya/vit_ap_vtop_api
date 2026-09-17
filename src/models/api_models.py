from pydantic import BaseModel
from typing import List, Optional

from src.models.auth_models import SessionRequest

# Import models from your client library for responses
from vitap_vtop_client.attendance import AttendanceModel
from vitap_vtop_client.profile import StudentProfileModel
from vitap_vtop_client.timetable import TimetableModel
from vitap_vtop_client.grade_history import GradeHistoryModel
from vitap_vtop_client.marks import MarksModel
from vitap_vtop_client.exam_schedule import ExamScheduleModel


# --- Request Models ---
# Data endpoints take the session from /auth/login rather than credentials.
# VTOP's login is captcha gated and costs around a dozen requests, so repeating
# it on every call was slow and hard on a portal that is not built for it. It
# also could not work at all once VTOP started challenging for an OTP, because
# the challenge is raised while answering one request and answered on the next.
class BaseVtopRequest(SessionRequest):
    """Base model for requests that act on an existing VTOP session."""


class AttendanceRequest(BaseVtopRequest):
    """Request model for fetching attendance."""

    sem_sub_id: str


class BiometricRequest(BaseVtopRequest):
    """Request model for fetching biometric data."""

    date: str


class TimetableRequest(BaseVtopRequest):
    """Request model for fetching timetable."""

    sem_sub_id: str


class ExamScheduleRequest(BaseVtopRequest):
    """Request model for fetching exam schedules."""

    sem_sub_id: str


class MarksRequest(BaseVtopRequest):
    """Request model for fetching all marks."""

    sem_sub_id: str


class ComprehensiveDataRequest(BaseVtopRequest):
    """Request model for fetching all comprehensive student data."""

    sem_sub_id: str


class ComprehensiveDataResponse(BaseModel):
    """Response model for the comprehensive student data endpoint."""

    profile: StudentProfileModel
    attendance: List[AttendanceModel]
    timetable: TimetableModel
    exam_schedule: ExamScheduleModel
    grade_history: GradeHistoryModel
    marks: MarksModel


# Profile, GradeHistory, Mentor requests only need username/password
# They can use BaseVtopRequest directly.

# --- Response Models ---
# We will reuse the models directly from the vitap-vtop-client library.
# AttendanceModel, StudentProfileModel, TimetableModel, BiometricModel,
# GradeHistoryModel, MentorModel are already defined in the client's model files.
# Ensure they are imported above if needed for response_model type hints.
