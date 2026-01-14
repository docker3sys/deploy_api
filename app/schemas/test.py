from pydantic import BaseModel

class TestCreate(BaseModel):
    title: str
    description: str | None = None

class TestResponse(BaseModel):
    id: int
    title: str
    description: str | None = None

    class Config:
        from_attributes = True

class TestSubmit(BaseModel):
    user_id: int
    test_id: int
    score: int