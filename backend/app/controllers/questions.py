from sqlalchemy.orm import Session
from app.models.questions import Question
from app.schemas.questions import QuestionCreate, QuestionUpdate





# function for getting all questions for a quiz
def get_questions_for_quiz(db: Session, quiz_id: int):
    return db.query(Question).filter(Question.quiz_id == quiz_id).all()

# function for getting a question by id
def get_question_by_id(db: Session, question_id: int):
    return db.query(Question).filter(Question.question_id == question_id).first()

# function for creating a new question
def create_question(db: Session, question: QuestionCreate):
    db_question = Question(
        question_text=question.question_text,
        quiz_id=question.quiz_id
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

# function for updating an existing question by id
def update_question(db: Session, question_id: int, question: QuestionUpdate):
    db_question = db.query(Question).filter(Question.question_id == question_id).first()
    db_question.question_text = question.question_text
    db_question.quiz_id = question.quiz_id
    db.commit()
    db.refresh(db_question)
    return db_question

# function for deleting an existing question by id
def delete_question(db: Session, question_id: int):
    question = db.query(Question).filter(Question.question_id == question_id).first()
    db.delete(question)
    db.commit()
    return question

