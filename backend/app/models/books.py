from sqlalchemy import Column, BigInteger, Text, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

# class for books
class Book(Base):
    __tablename__ = "books"

    book_id = Column(BigInteger, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    img_url = Column(Text, nullable=True)
    
    # One-to-many relationship: one book can have many quizzes.
    quizzes = relationship(
        "Quiz",
        back_populates="book",
        cascade="all, delete"
    )
