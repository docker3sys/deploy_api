from pydantic import BaseModel
from typing import Dict

class TestSubmit(BaseModel):
    answers: Dict[str, int]
