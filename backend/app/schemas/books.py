from pydantic import BaseModel, ConfigDict


# book create schema 
class BookCreate(BaseModel):
    title: str
    author: str
    img_url: str

# book update schema
class BookUpdate(BaseModel):
    title: str
    author: str
    img_url: str

# book out schema
class BookOut(BaseModel):
    book_id: int
    title: str
    author: str
    img_url: str

    model_config = ConfigDict(from_attributes=True)


