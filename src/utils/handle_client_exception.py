from fastapi import APIRouter, Depends, HTTPException, status
from vitap_vtop_client.exceptions import (
    VitapVtopClientError,
    VtopLoginError,
    VtopAttendanceError,
    VtopBiometricError,
    VtopTimetableError,
    VtopGradeHistoryError,
    VtopMentorError,
    VtopProfileError,
    VtopParsingError,
    VtopSessionError,
    VtopConnectionError,
    VtopCaptchaError,
)


# Helper function to map client exceptions to HTTP exceptions
def handle_client_exception(e: VitapVtopClientError):
    """Maps specific client exceptions to appropriate HTTPExceptions."""
    if isinstance(e, (VtopLoginError, VtopCaptchaError)):
        # Invalid credentials or captcha failure means unauthorized
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    elif isinstance(e, VtopSessionError):
        # If a session *somehow* becomes invalid mid-request (less likely with per-request client)
        # still 401 might be appropriate.
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    elif isinstance(e, VtopConnectionError):
        # 502 Bad Gateway for issues connecting to VTOP
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Error connecting to VTOP: {e}",
        )
    elif isinstance(e, VtopParsingError):
        # 500 Internal Server Error for scraping/parsing issues (VTOP structure changed?)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Data parsing failed: {e}. VTOP structure might have changed.",
        )
    elif isinstance(
        e,
        (
            VtopAttendanceError,
            VtopBiometricError,
            VtopTimetableError,
            VtopGradeHistoryError,
            VtopMentorError,
            VtopProfileError,
        ),
    ):
        # Catch specific data fetching errors (might indicate invalid parameters or VTOP internal error)
        # 400 Bad Request if clearly invalid input, 500 otherwise
        # More granular checking of the error message 'str(e)' might be needed for 400 vs 500
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )  # Default to 500 for VTOP internal issues
    else:
        # Generic client error or unhandled exception
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An internal client error occurred: {e}",
        )
