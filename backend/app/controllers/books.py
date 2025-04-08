from sqlalchemy.orm import Session
from app.models.books import Book
from app.schemas.books import BookCreate, BookUpdate


# function for getting all books
def get_books(db: Session):
    return db.query(Book).all()

# function for getting a book by id
def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.book_id == book_id).first()

# function for creating a new book
def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        author=book.author,
        img_url=book.img_url
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# function for updating an existing book by id
def update_book(db: Session, book_id: int, book: BookUpdate):
    db_book = db.query(Book).filter(Book.book_id == book_id).first()
    db_book.title = book.title
    db_book.author = book.author
    db_book.img_url = book.img_url
    db.commit()
    db.refresh(db_book)
    return db_book


# function for deleting an existing book by id
def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.book_id == book_id).first()
    db.delete(book)
    db.commit()
    return book

