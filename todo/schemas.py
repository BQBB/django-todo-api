from ninja import Schema
from pydantic import UUID4
from typing import List
from account.schemas import AccountOut


class Uid(Schema):
    id: UUID4

class TodoBody(Schema):
    title: str
    description: str

class TodoUpdate(Schema):
    is_finished: bool

class TodoOut(Uid, TodoBody, TodoUpdate):
    user: AccountOut

class TodoCreate(TodoBody):
    pass
