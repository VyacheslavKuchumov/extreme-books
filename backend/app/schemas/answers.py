from pydantic import BaseModel, ConfigDict
# from app.schemas.books import BookOut




# answer create schema
class AnswerCreate(BaseModel):
    answer_text: str
    question_id: int
    is_correct: bool
    
# answer update schema
class AnswerUpdate(BaseModel):
    answer_text: str
    question_id: int
    is_correct: bool

# answer out schema
class AnswerOut(BaseModel):
    answer_id: int
    answer_text: str
    question_id: int
    is_correct: bool

    model_config = ConfigDict(from_attributes=True)

