from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserAPIKey(BaseModel):
    key: str


class ComputerAPIKey(BaseModel):
    key: str


class Computer(BaseModel):
    computer_id: int
    computer_label: Union[str, None] = None
    os_version: Union[str, None] = None


# IMPORTANT: API keys should be provided in future
@app.post(
    "/computer/",
    response_model = Computer,
    summary = "Create a computer",
    description = "Create a computer with its id, label and version",
)
async def create_item(computer: Computer):
    return computer