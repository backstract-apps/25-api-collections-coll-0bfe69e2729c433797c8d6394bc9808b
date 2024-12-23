from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class BUser(BaseModel):
    id: int
    user_name: str


class ReadBUser(BaseModel):
    id: int
    user_name: str
    class Config:
        from_attributes = True


