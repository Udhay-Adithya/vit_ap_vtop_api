# app/dependencies.py
from fastapi import Header, HTTPException, Depends
from typing import Annotated

from config import settings


async def verify_api_key(
    api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
):
    """
    Dependency to verify the API Key provided in the X-API-Key header.

    Raises:
        HTTPException: If the API Key is missing or invalid.
    """
    if api_key is None:
        raise HTTPException(status_code=401, detail="API Key missing")
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    # If the key is valid, the dependency successfully completes,
    # and the request handler can proceed. No value is returned by the dependency.
