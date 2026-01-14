from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.test import Test
from app.schemas.test import TestSubmit
from app.services.scoring import calculate_scores

router = APIRouter(prefix="/tests", tags=["Tests"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{slug}")
def get_test(slug: str, db: Session = Depends(get_db)):
    test = db.query(Test).filter(Test.slug == slug, Test.is_active == True).first()
    if not test:
        raise HTTPException(404)
    return test

@router.post("/{slug}/submit")
def submit_test(slug: str, data: TestSubmit, db: Session = Depends(get_db)):
    test = db.query(Test).filter(Test.slug == slug).first()
    if not test:
        raise HTTPException(404)

    scores = calculate_scores(test.questions, data.answers)
    return {"scores": scores}
