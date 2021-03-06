from fastapi import FastAPI
from typing import Optional

from enum import Enum

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# root route
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Using query params: localhost:8000/items?skip=x&limit=y
@app.get("/items/")
async def read_items(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# Query parameter type conversion
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This was an amazing item with a long description"})

    return item


@app.get("users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user_id(user_id: int):
    return {"user_id": user_id}


# Using an enum class to compare
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}

    if model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# Reading files
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Required query parameters
@app.get("/items/needy/{item_id}")
async def get_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
