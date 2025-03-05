from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.quizzes import QuizCreate, QuizUpdate, QuizOut
from app.controllers.quizzes import create_quiz, get_quizzes, update_quiz, delete_quiz

from app.database import get_db

router = APIRouter()

# get all quizzes
@router.get("/", response_model=list[QuizOut])
def get_all_quizzes(db: Session = Depends(get_db)):
    return get_quizzes(db)


# create a new quiz
@router.post("/", response_model=QuizOut)
def create_quiz_route(quiz: QuizCreate, db: Session = Depends(get_db)):
    return create_quiz(db, quiz)


# update an existing quiz by id
@router.put("/{quiz_id}", response_model=QuizOut)
def update_quiz_route(quiz_id: int, quiz: QuizUpdate, db: Session = Depends(get_db)):
    return update_quiz(db, quiz_id, quiz)


# delete an existing quiz by id
@router.delete("/{quiz_id}", response_model=QuizOut)
def delete_quiz_route(quiz_id: int, db: Session = Depends(get_db)):
    return delete_quiz(db, quiz_id)


