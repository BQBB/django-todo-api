from ninja import Schema
from pydantic import UUID4
from typing import List
from account.schemas import AccountOut

class TodoOut(Schema):
    id: UUID4
    title: str
    description: str
    is_finished: bool
    user: AccountOut