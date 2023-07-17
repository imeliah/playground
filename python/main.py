from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


# 创建数据模型
class Item(BaseModel):
    name: str
    description: Union[str, None] = None  # 可选，默认值None
    price: float
    tax: Union[float, None] = None  # 可选，默认值None


app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = None):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result
