from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.books import BookCreate, BookUpdate, BookOut
from app.controllers.books import create_book, get_books, update_book, delete_book
from app.database import get_db

router = APIRouter()


# get all books
@router.get("/", response_model=list[BookOut])
def get_all_books(db: Session = Depends(get_db)):
    return get_books(db)


# create a new book
@router.post("/", response_model=BookOut)
def create_book_route(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)


# update an existing book by id
@router.put("/{book_id}", response_model=BookOut)
def update_book_route(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    return update_book(db, book_id, book)


# delete an existing book by id
@router.delete("/{book_id}", response_model=BookOut)
def delete_book_route(book_id: int, db: Session = Depends(get_db)):
    return delete_book(db, book_id)




