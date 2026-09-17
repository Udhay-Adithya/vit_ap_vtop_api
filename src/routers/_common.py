"""Shared plumbing for the student routers."""

from contextlib import asynccontextmanager

from fastapi import HTTPException, status

from src.utils.handle_client_exception import handle_client_exception

from vitap_vtop_client import RestorableSession, VtopClient
from vitap_vtop_client.exceptions import VitapVtopClientError


@asynccontextmanager
async def client_for(session: RestorableSession):
    """Rebuilds the caller's VTOP session for the life of one request.

    VTOP holds the session server side against its cookie, so this costs no
    requests and no login. The client carries no password, so an expired session
    raises rather than silently logging in again -- the caller has to go back
    through /auth/login, which may need an OTP only they can answer.
    """
    client = VtopClient.restore(
        registration_number=session.registration_number,
        cookie=session.cookie,
        csrf_token=session.csrf_token,
        user_agent=session.user_agent,
    )
    try:
        yield client
    finally:
        await client.close()


@asynccontextmanager
async def vtop_errors():
    """Maps client exceptions onto HTTP responses.

    Every endpoint needs the same two arms, and repeating them was how the
    earlier version ended up with a different fallback message in each one.
    """
    try:
        yield
    except HTTPException:
        raise
    except VitapVtopClientError as e:
        handle_client_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}",
        )
