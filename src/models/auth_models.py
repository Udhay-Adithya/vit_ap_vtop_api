from typing import Literal, Optional

from pydantic import BaseModel, Field

from vitap_vtop_client import OtpChallenge, RestorableSession


class LoginRequest(BaseModel):
    """VTOP credentials, sent once to open a session."""

    registration_number: str
    password: str


class LoginResponse(BaseModel):
    """The outcome of a login attempt.

    VTOP's login is two steps whenever it decides to challenge for an OTP, which
    it does after a period of inactivity or when the login comes from an IP it
    has not seen. Both outcomes are a successful request, so both are 200; read
    `status` to tell them apart.
    """

    status: Literal["authenticated", "otp_required"]
    # Set when status is "authenticated". Send it back on every data request.
    session: Optional[RestorableSession] = None
    # Set when status is "otp_required". Collect the OTP from the student and
    # post it to /auth/verify_otp along with this, unchanged.
    otp_challenge: Optional[OtpChallenge] = None


class VerifyOtpRequest(BaseModel):
    """The OTP the student received, with the challenge it answers."""

    otp_challenge: OtpChallenge
    otp: str = Field(min_length=1)


class ResendOtpRequest(BaseModel):
    """Asks VTOP to send a fresh OTP for a challenge already in flight."""

    otp_challenge: OtpChallenge


class ResendOtpResponse(BaseModel):
    status: Literal["sent"] = "sent"
    # The challenge stays valid; keep using it to verify the new OTP.
    otp_challenge: OtpChallenge


class SessionRequest(BaseModel):
    """Base for every data request: the session from /auth/login."""

    session: RestorableSession
