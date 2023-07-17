from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    creator: User


@app.put("/items/{item_id}")
async def update_item(item_id: int,
                      item: Item = Body(embed=True),  # item键，值中包含模型内容的json
                      ):
    results = {"item_id": item_id, "item": item}
    print(item)
    print(item.creator)
    return results
