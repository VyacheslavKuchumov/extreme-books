from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.questions import QuestionCreate, QuestionUpdate, QuestionOut
from app.controllers.questions import create_question, get_questions_for_quiz, update_question, delete_question, get_question_by_id


from app.database import get_db

router = APIRouter()

# get questions for quiz
@router.get("/{quiz_id}", response_model=list[QuestionOut])
def get_questions(quiz_id: int, db: Session = Depends(get_db)):
    return get_questions_for_quiz(db, quiz_id)

# get question by id
@router.get("/search/{question_id}", response_model=QuestionOut)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = get_question_by_id(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

# create a new question
@router.post("/", response_model=QuestionOut)
def create_question_route(question: QuestionCreate, db: Session = Depends(get_db)):
    return create_question(db, question)

# update an existing question by id
@router.put("/{question_id}", response_model=QuestionOut)
def update_question_route(question_id: int, question: QuestionUpdate, db: Session = Depends(get_db)):
    return update_question(db, question_id, question)

# delete an existing question by id
@router.delete("/{question_id}", response_model=QuestionOut)
def delete_question_route(question_id: int, db: Session = Depends(get_db)):
    return delete_question(db, question_id)