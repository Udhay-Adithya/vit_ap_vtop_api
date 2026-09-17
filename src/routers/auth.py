from contextlib import asynccontextmanager

from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies import verify_api_key
from src.models.auth_models import (
    LoginRequest,
    LoginResponse,
    ResendOtpRequest,
    ResendOtpResponse,
    VerifyOtpRequest,
)
from src.utils.handle_client_exception import handle_client_exception

from vitap_vtop_client import VtopClient
from vitap_vtop_client.exceptions import (
    VitapVtopClientError,
    VtopLoginOtpRequiredError,
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[Depends(verify_api_key)],
)


@asynccontextmanager
async def _closing(client: VtopClient):
    try:
        yield client
    finally:
        await client.close()


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """
    Opens a VTOP session.

    Credentials are sent here once and never again: the response carries a
    session that every data endpoint accepts. That matters because VTOP's login
    is captcha gated and costs around a dozen requests, so repeating it per call
    is slow and hard on the portal.

    VTOP challenges for an OTP after a period of inactivity or when the login
    comes from an IP it has not seen — which a server is, by definition. That is
    a normal outcome rather than a failure, so it returns 200 with
    `status: "otp_required"` and a challenge to post to `/auth/verify_otp`.
    """
    try:
        async with _closing(
            VtopClient(
                registration_number=request.registration_number,
                password=request.password,
            )
        ) as client:
            try:
                await client.login()
            except VtopLoginOtpRequiredError:
                # Credentials and captcha were accepted; only the OTP is left.
                # The challenge carries the cookie and token needed to finish,
                # so the next request can pick it up on a different process.
                return LoginResponse(
                    status="otp_required",
                    otp_challenge=client.otp_challenge,
                )
            return LoginResponse(status="authenticated", session=client.session)

    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/verify_otp", response_model=LoginResponse)
async def verify_otp(request: VerifyOtpRequest):
    """
    Finishes a login that VTOP interrupted with an OTP.

    Post the OTP the student received together with the `otp_challenge` from
    `/auth/login`, unchanged. On success the response is the same shape as a
    login that was never challenged.
    """
    challenge = request.otp_challenge
    try:
        async with _closing(
            VtopClient.restore_otp_challenge(
                registration_number=challenge.registration_number,
                cookie=challenge.cookie,
                csrf_token=challenge.csrf_token,
                user_agent=challenge.user_agent,
            )
        ) as client:
            await client.verify_login_otp(request.otp)
            return LoginResponse(status="authenticated", session=client.session)

    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )


@router.post("/resend_otp", response_model=ResendOtpResponse)
async def resend_otp(request: ResendOtpRequest):
    """
    Asks VTOP to send a fresh OTP for a challenge already in flight.

    Use this when the OTP expired, rather than logging in again — a new login
    would invalidate this challenge and make the student wait for another
    captcha-gated attempt. The challenge stays valid, so keep using it.
    """
    challenge = request.otp_challenge
    try:
        async with _closing(
            VtopClient.restore_otp_challenge(
                registration_number=challenge.registration_number,
                cookie=challenge.cookie,
                csrf_token=challenge.csrf_token,
                user_agent=challenge.user_agent,
            )
        ) as client:
            await client.resend_login_otp()
            return ResendOtpResponse(otp_challenge=client.otp_challenge)

    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )
