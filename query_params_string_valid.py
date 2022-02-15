from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


# q is not list[str] meaning we query as: ?q=Foo&q=Bar -> list(Foo, Bar) = q
# A query with more than 10 letters would throw due to max_length
# Use Query(["foo", "bar"]) to have default params instead of None
# title adds metadata to the query


@app.get("/items/")
async def read_items(
    q: Optional[list[str]] = Query(
        None,
        title="Query String",
        description="Query string for the items to search in db",
        max_length=10,
        deprecated=True,  # Will warn users in the docs that the parameter is being deprecated
        # Use include_in_schema to hide form OpenAPI
    )
):  # Restrict the length of the query
    query_items = {"q": q}
    return query_items
