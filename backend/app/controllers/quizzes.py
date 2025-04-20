from sqlalchemy.orm import Session
from app.models.quizzes import Quiz
from app.schemas.quizzes import QuizCreate, QuizUpdate



# function for getting all quizzes
def get_quizzes_for_book(db: Session, book_id: int):
    return db.query(Quiz).filter(Quiz.book_id == book_id).all()

# function for getting a quiz by id
def get_quiz_by_id(db: Session, quiz_id: int):
    return db.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()

# function for creating a new quiz
def create_quiz(db: Session, quiz: QuizCreate):
    db_quiz = Quiz(
        quiz_name=quiz.quiz_name,
        points=quiz.points,
        book_id=quiz.book_id
    )
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz


# function for updating an existing quiz by id
def update_quiz(db: Session, quiz_id: int, quiz: QuizUpdate):
    db_quiz = db.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()
    db_quiz.quiz_name = quiz.quiz_name
    db_quiz.points = quiz.points
    db_quiz.book_id = quiz.book_id
    db.commit()
    db.refresh(db_quiz)
    return db_quiz


# function for deleting an existing quiz by id
def delete_quiz(db: Session, quiz_id: int):
    quiz = db.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()
    db.delete(quiz)
    db.commit()
    return quiz

