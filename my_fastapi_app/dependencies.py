"""Dependencies used in several places of the app."""

from typing import Annotated

from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    """Check whether the token header is valid.

    Args:
        x_token (Annotated[str, Header): The token header.

    Raises:
        HTTPException: X-Token header invalid
    """
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    """Check whether the token is Jessica.

    Args:
        token (str): The token.

    Raises:
        HTTPException: No Jessica token provided
    """
    if token != "jessica":
        raise HTTPException(
            status_code=400,
            detail="No Jessica token provided",
        )
