from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.quizzes import QuizCreate, QuizUpdate, QuizOut
from app.controllers.quizzes import create_quiz, get_quizzes_for_book, update_quiz, delete_quiz, get_quiz_by_id

from app.database import get_db

router = APIRouter()

# get quizzes for book 
@router.get("/{book_id}", response_model=list[QuizOut])
def get_quizzes(book_id: int, db: Session = Depends(get_db)):
    return get_quizzes_for_book(db, book_id)

# get quiz by id
@router.get("/search/{quiz_id}", response_model=QuizOut)
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = get_quiz_by_id(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

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


