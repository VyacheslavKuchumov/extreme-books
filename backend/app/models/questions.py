from sqlalchemy import Column, BigInteger, Text, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.answers import Answer

# class for questions
class Question(Base):
    __tablename__ = "questions"

    question_id = Column(BigInteger, primary_key=True, index=True)
    question_text = Column(Text, nullable=False)
    quiz_id = Column(BigInteger, ForeignKey("quizzes.quiz_id"), nullable=False)
    
    quiz = relationship("Quiz", back_populates="question")
    answer = relationship("Answer", back_populates="question", cascade="all, delete")





