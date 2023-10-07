"""My FastAPI app."""

import sys
from pathlib import Path
import time
from enum import Enum

from fastapi import FastAPI, Request, Depends
from pydantic import BaseModel, Field

tests_path = Path(sys.path[0])
sys.path.append(str(tests_path.parent))
# pylint: disable=wrong-import-position
from my_fastapi_app.dependencies import get_query_token  # noqa: E402
from my_fastapi_app.routers import items, users  # noqa: E402


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


app: FastAPI = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(users.router)
app.include_router(items.router)


@app.get("/")
async def root():
    """Return Hello Bigger Applications.

    Returns:
        dict: The message.
    """
    return {"message": "Hello Bigger Applications!"}


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
