from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Computer(BaseModel):
    computer_id: int
    computer_label: Union[str, None] = None
    os_version: Union[str, None] = None


@app.post(
    "/items/",
    response_model = Computer,
    summary = "Create a computer",
    description = "Create a computer with its id, label and version",
)
async def create_item(computer: Computer):
    return computer