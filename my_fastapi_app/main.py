"""My FastAPI app."""

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """This is the dataclass for items.

    Args:
        BaseModel (BaseModel): A base class for creating Pydantic models.
    """

    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    """Return Hello World.

    Returns:
        dict: Hello World
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """Return the ID of the item.

    Args:
        item_id (int): The ID of the item
        q (Union[str, None], optional): Don't know what this is.

    Returns:
        dict: Item ID and the unknown parameter.
    """
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Update an item by its ID.

    Args:
        item_id (int): ID of the item we'd like to update.
        item (Item): An Item data object.

    Returns:
        dict: Name and ID of the item.
    """
    return {
        "item_name": item.name,
        "item_id": item_id,
        "item_price": item.price,
        }
