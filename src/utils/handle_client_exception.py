from fastapi import HTTPException, status
from vitap_vtop_client.exceptions import (
    VitapVtopClientError,
    VtopLoginError,
    VtopLoginOtpRequiredError,
    VtopLoginOtpIncorrectError,
    VtopLoginOtpExpiredError,
    VtopMenuUnavailableError,
    VtopParsingError,
    VtopSessionError,
    VtopConnectionError,
)


# The client sets a status_code on most of what it raises, and it knows more
# about the failure than we do -- a malformed semester id and a dead session are
# both VtopSessionError, but it marks the first 400 and the second 401. Mapping
# by exception type alone collapses those into one answer, so the carried code
# wins wherever the client supplied one.
#
# These are the cases where the type has to override it, because the right HTTP
# answer differs from what the client records for its own purposes.
_STATUS_OVERRIDES: tuple[tuple[type[Exception], int], ...] = (
    # The client marks this 401 because the credentials leg is unfinished. Over
    # HTTP it is a 409: the credentials were accepted, and retrying them cannot
    # resolve it -- only supplying the OTP can.
    (VtopLoginOtpRequiredError, status.HTTP_409_CONFLICT),
)

# Used only when the client did not set a status code.
_TYPE_DEFAULTS: tuple[tuple[type[Exception], int], ...] = (
    (VtopLoginError, status.HTTP_401_UNAUTHORIZED),
    (VtopSessionError, status.HTTP_401_UNAUTHORIZED),
    (VtopConnectionError, status.HTTP_502_BAD_GATEWAY),
    (VtopMenuUnavailableError, status.HTTP_502_BAD_GATEWAY),
    (VtopParsingError, status.HTTP_500_INTERNAL_SERVER_ERROR),
)


def _describe(e: VitapVtopClientError) -> str:
    """Prefixes the client's message with what the failure means for a caller."""
    if isinstance(e, VtopLoginOtpRequiredError):
        return f"VTOP requires a login OTP to continue: {e}"
    if isinstance(e, VtopLoginOtpExpiredError):
        return f"Login OTP expired: {e}"
    if isinstance(e, VtopLoginOtpIncorrectError):
        return f"Login OTP incorrect: {e}"
    if isinstance(e, VtopConnectionError):
        return f"Error connecting to VTOP: {e}"
    if isinstance(e, VtopMenuUnavailableError):
        return f"VTOP refused the request: {e}"
    if isinstance(e, VtopParsingError):
        return f"Data parsing failed: {e}. VTOP structure might have changed."
    return str(e)


def _status_for(e: VitapVtopClientError) -> int:
    for exc_type, code in _STATUS_OVERRIDES:
        if isinstance(e, exc_type):
            return code

    carried = getattr(e, "status_code", None)
    if isinstance(carried, int) and 400 <= carried <= 599:
        return carried

    for exc_type, code in _TYPE_DEFAULTS:
        if isinstance(e, exc_type):
            return code

    return status.HTTP_500_INTERNAL_SERVER_ERROR


def handle_client_exception(e: VitapVtopClientError):
    """Maps a vitap-vtop-client exception onto an HTTPException."""
    raise HTTPException(status_code=_status_for(e), detail=_describe(e))
