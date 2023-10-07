"""'items' submodule; e.g. 'import app.routers.items'."""

from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router: APIRouter = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db: dict = {
    "plumbus": {
        "name": "Plumbus"
    },
    "gun": {
        "name": "Portal Gun"
    },
}


@router.get("/")
async def read_items() -> dict:
    """Read fake items.

    Returns:
        dict: The fake items.
    """
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str) -> dict:
    """Read item by ID.

    Args:
        item_id (str): ID of the item.

    Raises:
        HTTPException: Item not found

    Returns:
        dict: Name and ID of the item.
    """
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str) -> dict:
    """Update item by ID.

    Args:
        item_id (str): ID of the item.

    Raises:
        HTTPException: You can only update the item: plumbus

    Returns:
        dict: Item ID and name.
    """
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
