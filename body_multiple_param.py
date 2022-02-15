from typing import Optional

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    desc: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="Item ID", ge=0, le=999),
    q: Optional[str] = None,
    item: Optional[Item] = None,
):
    res = {"item_id": item_id}
    
    if q:
        res.update({"q": q})
    if item:
        res.update({"item": item})
        
    return res
