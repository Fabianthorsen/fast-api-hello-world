from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

# To send data from our client/browser to the API, we use the request body
# We use the HTTP verb /POST to send things to our API


class Item(BaseModel):
    item_id: str = str(uuid4())
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# Models are classes that inherit from the BaseModel class in pydantic

app = FastAPI()


@app.post("/items/")
async def create_item(
    item: Item,
):  # The input is of type Item, so it needs to atleast have a: name and price
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update(
            {"price_with_tax": price_with_tax}
        )  # Update the item_dict with the new attribute
    return item_dict


@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item, q: Optional[str] = None):
    res = {"item_id": item_id, **item.dict()}
    if q:
        res.update({"q": q})
    return res
