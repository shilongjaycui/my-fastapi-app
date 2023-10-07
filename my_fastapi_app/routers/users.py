"""'users' submodule; e.g. 'import app.routers.users'.

Have the path operations related to your users separated
from the rest of the code, to keep it organized.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    """Read users.

    Returns:
        list[dict]: A list of users and their usernames.
    """
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    """Read current user.

    Returns:
        dict: The current user's username.
    """
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    """Get user by username.

    Args:
        username (str): Username of the user.

    Returns:
        dict: Username of the user.
    """
    return {"username": username}
