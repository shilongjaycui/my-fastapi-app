"""My FastAPI app."""

from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel


class ModelName(str, Enum):
    """Machine learning models.

    Args:
        str (str): The string datatype.
        Enum (Enum): The Enum datatype.
    """

    # pylint: disable=invalid-name
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    """This is the dataclass for items.

    Args:
        BaseModel (BaseModel): A base class for creating Pydantic models.
    """

    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app: FastAPI = FastAPI()


@app.get("/")
def read_root():
    """Return Hello World.

    Returns:
        dict: Hello World
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Return the ID of the item.

    Args:
        item_id (int): The ID of the item

    Returns:
        dict: Item ID.
    """
    return {"item_id": item_id}


@app.get("/dua_lipa")
def running_away_with_dua_lipa():
    """Love Dua Lipa.

    Returns:
        dict: Dua Lipa's social media.
    """
    return {
        "her wiki": "https://en.wikipedia.org/wiki/Dua_Lipa",
        "her insta": "https://www.instagram.com/dualipa/",
        "her store": "https://store.dualipa.com/",
    }


@app.get("/users/me")
async def read_user_me():
    """Get data about the current user.

    Returns:
        dict: ID of the current user.
    """
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """Get data about the user with the specified ID.

    Args:
        user_id (str): ID of the user.

    Returns:
        dict: ID of the user.
    """
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """Get model info by model name.

    Args:
        model_name (ModelName): Name of the machine learning model.

    Returns:
        dict: Information on the machine learning model.
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.put("/items/{item_id}")
async def create_item(item_id: int,
                      item: Item,
                      q: str | None = None) -> dict[str, any]:
    """Create an item.

    Args:
        item_id (int): ID of the item.
        item (Item): The item.
        q (str | None, optional): A query parameter. Defaults to None.

    Returns:
        dict: Information on the item.
    """
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
