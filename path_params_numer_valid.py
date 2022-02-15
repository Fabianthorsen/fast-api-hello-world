from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,  # This will ensure that the kwargs below can be called without specific ordering
    item_id: int = Path(
        ...,  # ... denotes that it is required
        title="The ID of the item to get",  # metadata
        ge=1,  # ge = greater than or equal to the value
    ),
    q: Optional[str] = Query(
        None, alias="item-query"  # alias will make you able to call it as ?item-query=
    ),
    size: float = Query(..., gt=0, lt=10.5),
):
    res = {"item_id": item_id, "size": size}
    if q:
        res.update({"q": q})
    return res
