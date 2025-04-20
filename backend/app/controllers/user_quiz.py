from sqlalchemy.orm import Session
from app.models.user_quiz import UserQuiz
from app.schemas.user_quiz import UserQuizCreate, UserQuizUpdate


# function for getting a user quiz by user uid
def get_user_quiz_by_uid(db: Session, user_uid: str):
    return db.query(UserQuiz).filter(UserQuiz.user_uid == user_uid).all()

# function for getting a user quizzes by quiz id
def get_user_quiz_by_quiz_id(db: Session, quiz_id: int):
    return db.query(UserQuiz).filter(UserQuiz.quiz_id == quiz_id).all()

# function for creating a new user quiz
def create_user_quiz(db: Session, user_quiz: UserQuizCreate):
    db_user_quiz = UserQuiz(
        user_uid=user_quiz.user_uid,
        quiz_id=user_quiz.quiz_id,
        final_score=user_quiz.final_score
    )
    db.add(db_user_quiz)
    db.commit()
    db.refresh(db_user_quiz)
    return db_user_quiz

# function for updating an existing user quiz by id
def update_user_quiz(db: Session, user_quiz_id: int, user_quiz: UserQuizUpdate):
    db_user_quiz = db.query(UserQuiz).filter(UserQuiz.user_quiz_id == user_quiz_id).first()
    db_user_quiz.user_uid = user_quiz.user_uid
    db_user_quiz.quiz_id = user_quiz.quiz_id
    db_user_quiz.final_score = user_quiz.final_score
    db.commit()
    db.refresh(db_user_quiz)
    return db_user_quiz

# function for deleting an existing user quiz by id
def delete_user_quiz(db: Session, user_quiz_id: int):
    user_quiz = db.query(UserQuiz).filter(UserQuiz.user_quiz_id == user_quiz_id).first()
    db.delete(user_quiz)
    db.commit()
    return user_quiz

