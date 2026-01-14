from fastapi import APIRouter
from pydantic import BaseModel
from pathlib import Path
import json

router = APIRouter()

# GET - отдать тест
@router.get("/{test_name}")
def get_test(test_name: str):
    path = Path("tests") / f"{test_name}.json"
    if not path.exists():
        return {"error": "Test not found"}
    
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# POST - принять ответы и посчитать результат
class Answer(BaseModel):
    question_id: str
    value: int

class TestSubmit(BaseModel):
    test_name: str
    answers: list[Answer]

@router.post("/submit")
def submit_test(submit: TestSubmit):
    path = Path("tests") / f"{submit.test_name}.json"
    if not path.exists():
        return {"error": "Test not found"}

    with open(path, "r", encoding="utf-8") as f:
        test = json.load(f)

    score = 0
    for answer in submit.answers:
        q = next((q for q in test["questions"] if q["id"] == answer.question_id), None)
        if q:
            score += answer.value

    return {"score": score}
