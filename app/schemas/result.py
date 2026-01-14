from pydantic import BaseModel

class ResultCreate(BaseModel):
    user_id: int
    test_id: int
    score: int

class ResultResponse(BaseModel):
    id: int
    user_id: int
    test_id: int
    score: int

    class Config:
        from_attributes = True