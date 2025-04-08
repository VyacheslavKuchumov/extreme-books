from sqlalchemy import Column, BigInteger, Text, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.questions import Question

# class for quizzes
class Quiz(Base):
    __tablename__ = "quizzes"

    quiz_id = Column(BigInteger, primary_key=True, index=True)
    quiz_name = Column(Text, nullable=False)
    points = Column(BigInteger, nullable=False)
    book_id = Column(BigInteger, ForeignKey("books.book_id"), nullable=False)
    
    book = relationship("Book", back_populates="quiz")
    question = relationship("Question", uselist=True, back_populates="quiz", cascade="all, delete")




