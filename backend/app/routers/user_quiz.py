from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_quiz import UserQuizCreate, UserQuizUpdate, UserQuizOut
from app.controllers.user_quiz import create_user_quiz, get_user_quiz_by_uid, get_user_quiz_by_quiz_id, update_user_quiz, delete_user_quiz


from app.database import get_db

router = APIRouter()

# get user quizzes for user uid
@router.get("/user/{user_uid}", response_model=list[UserQuizOut])
def get_user_quizzes(user_uid: str, db: Session = Depends(get_db)):
    return get_user_quiz_by_uid(db, user_uid)

# get user quizzes for quiz id
@router.get("/quiz/{quiz_id}", response_model=list[UserQuizOut])
def get_user_quizzes(quiz_id: int, db: Session = Depends(get_db)):
    return get_user_quiz_by_quiz_id(db, quiz_id)

# create a new user quiz
@router.post("/", response_model=UserQuizOut)
def create_user_quiz_route(user_quiz: UserQuizCreate, db: Session = Depends(get_db)):
    return create_user_quiz(db, user_quiz)

# update an existing user quiz by id
@router.put("/{user_quiz_id}", response_model=UserQuizOut)
def update_user_quiz_route(user_quiz_id: int, user_quiz: UserQuizUpdate, db: Session = Depends(get_db)):
    return update_user_quiz(db, user_quiz_id, user_quiz)

# delete an existing user quiz by id
@router.delete("/{user_quiz_id}", response_model=UserQuizOut)
def delete_user_quiz_route(user_quiz_id: int, db: Session = Depends(get_db)):
    return delete_user_quiz(db, user_quiz_id)