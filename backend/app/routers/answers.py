from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.answers import AnswerCreate, AnswerUpdate, AnswerOut
from app.controllers.answers import create_answer, get_answers_for_question, update_answer, delete_answer, get_answer_by_id


from app.database import get_db

router = APIRouter()

# get answers for question
@router.get("/{question_id}", response_model=list[AnswerOut])
def get_answers(question_id: int, db: Session = Depends(get_db)):
    return get_answers_for_question(db, question_id)

# get answer by id
@router.get("/search/{answer_id}", response_model=AnswerOut)
def get_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = get_answer_by_id(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer

# create a new answer
@router.post("/", response_model=AnswerOut)
def create_answer_route(answer: AnswerCreate, db: Session = Depends(get_db)):
    return create_answer(db, answer)

# update an existing answer by id
@router.put("/{answer_id}", response_model=AnswerOut)
def update_answer_route(answer_id: int, answer: AnswerUpdate, db: Session = Depends(get_db)):
    return update_answer(db, answer_id, answer)

# delete an existing answer by id
@router.delete("/{answer_id}", response_model=AnswerOut)
def delete_answer_route(answer_id: int, db: Session = Depends(get_db)):
    return delete_answer(db, answer_id)