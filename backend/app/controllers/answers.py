from sqlalchemy.orm import Session
from app.models.answers import Answer
from app.schemas.answers import AnswerCreate, AnswerUpdate


# function for getting all answers for a question
def get_answers_for_question(db: Session, question_id: int):
    return db.query(Answer).filter(Answer.question_id == question_id).all()

# function for getting an answer by id
def get_answer_by_id(db: Session, answer_id: int):
    return db.query(Answer).filter(Answer.answer_id == answer_id).first()

# function for creating a new answer
def create_answer(db: Session, answer: AnswerCreate):
    db_answer = Answer(
        answer_text=answer.answer_text,
        question_id=answer.question_id,
        is_correct=answer.is_correct
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

# function for updating an existing answer by id
def update_answer(db: Session, answer_id: int, answer: AnswerUpdate):
    db_answer = db.query(Answer).filter(Answer.answer_id == answer_id).first()
    db_answer.answer_text = answer.answer_text
    db_answer.question_id = answer.question_id
    db_answer.is_correct = answer.is_correct
    db.commit()
    db.refresh(db_answer)
    return db_answer

# function for deleting an existing answer by id
def delete_answer(db: Session, answer_id: int):
    answer = db.query(Answer).filter(Answer.answer_id == answer_id).first()
    db.delete(answer)
    db.commit()
    return answer
