import uuid
import asyncio
from typing import Dict, Optional

from vitap_vtop_client.client import VtopClient
from vitap_vtop_client.exceptions import VtopLoginError, VitapVtopClientError

# In-memory store for active client sessions
# Maps session_token (UUID str) to VtopClient instance
active_sessions: Dict[str, VtopClient] = {}
session_lock = asyncio.Lock()  # Protect the sessions dictionary


async def create_vtop_session(username: str, password: str) -> tuple[str, VtopClient]:
    """
    Creates a new VtopClient session, logs in, and stores the client.

    Args:
        username: VTOP registration number.
        password: VTOP password.

    Returns:
        A tuple containing the session token (str) and the VtopClient instance.

    Raises:
        VtopLoginError: If login fails.
        VitapVtopClientError: For other client-related errors during login.
        Exception: For unexpected errors.
    """
    # Create a new VtopClient instance
    # Handles the client lifespan explicitly here: create, ensure_logged_in, close on removal.
    client = VtopClient(username=username, password=password)

    try:
        # Log in using the client's internal method
        # This will perform the full login sequence including CAPTCHA solving
        logged_in_info = (
            await client._perform_login_sequence()
        )  # Accessing protected method for now

        # Generate a unique session token
        session_token = str(uuid.uuid4())

        # Store the client instance
        async with session_lock:
            # Before storing, check if a session for this user already exists and close it?
            # Or allow multiple sessions per user? Let's allow multiple for simplicity now.
            # A more robust system might track users and only allow one active session per user.

            active_sessions[session_token] = client

        print(f"Created session {session_token} for user {username}")

        return session_token, client

    except (VtopLoginError, VitapVtopClientError) as e:
        # If login fails, make sure to close the client we just created
        await client.close()
        print(f"Login failed for user {username}: {e}")
        raise  # Re-raise the specific error

    except Exception as e:
        # Handle unexpected errors during client creation or login
        await client.close()
        print(f"Unexpected error creating session for user {username}: {e}")
        raise VitapVtopClientError(f"Failed to create session: {e}") from e


async def get_vtop_client(session_token: str) -> Optional[VtopClient]:
    """
    Retrieves an active VtopClient instance by its session token.

    Args:
        session_token: The unique token for the session.

    Returns:
        The VtopClient instance if found, otherwise None.
    """
    async with session_lock:
        return active_sessions.get(session_token)


async def remove_vtop_session(session_token: str):
    """
    Removes an active VtopClient session and closes the client.

    Args:
        session_token: The unique token for the session.
    """
    client = None
    async with session_lock:
        client = active_sessions.pop(session_token, None)

    if client:
        print(f"Removing session {session_token}")
        await client.close()
    else:
        print(f"Attempted to remove non-existent session {session_token}")
