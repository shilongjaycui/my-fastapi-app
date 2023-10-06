"""My FastAPI app."""

import time
from enum import Enum
from typing import Annotated

from fastapi import Body, FastAPI, Request
from pydantic import BaseModel, Field


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
    description: str | None = Field(
        default=None,
        title="The description of the item",
        max_length=300,
    )
    price: float = Field(
        gt=0,
        description="The price must be greater than zero"
    )
    tax: float | None = None


app: FastAPI = FastAPI()


@app.get("/")
def read_root():
    """Return Hello World.

    Returns:
        dict: Hello World
    """
    return {"Hello": "World"}


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
                      q: str | None = None) -> dict:
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


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Return the ID of the item.

    Args:
        item_id (int): The ID of the item

    Returns:
        dict: Item ID.
    """
    return {"item_id": item_id}


@app.put("/items/{item_id}")
async def update_item(item_id: int,
                      item: Annotated[Item, Body(embed=True)]) -> dict:
    """Update an item.

    Args:
        item_id (int): ID of the item.
        item (Annotated[Item, Body, optional): The item. Defaults to True)].

    Returns:
        dict: The item and its ID.
    """
    results = {"item_id": item_id, "item": item}
    return results


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Modify the request (and the response).

    Args:
        request (Request): The request.
        call_next (_type_): A function that passes the request
                            to the path operation.

    Returns:
        _type_: The response.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
