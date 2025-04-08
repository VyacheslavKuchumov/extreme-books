from sqlalchemy import Column, BigInteger, Text, DateTime, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

# class for answers
class Answer(Base):
    __tablename__ = "answers"

    answer_id = Column(BigInteger, primary_key=True, index=True)
    answer_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question_id = Column(BigInteger, ForeignKey("questions.question_id"), nullable=False)
    
    question = relationship("Question", back_populates="answer")



