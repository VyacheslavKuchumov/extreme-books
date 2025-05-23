from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, user, books, events, quizzes, questions, answers, user_quiz, user_event
from fastapi.openapi.utils import get_openapi

# Create all tables (in production, use Alembic for migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(root_path="/api",
    title="FastAPI",
    description="Sluvik's API"
)

# Define allowed origins (adjust the list to your requirements)
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://vyachik.ru",
    "http://www.vyachik.ru",
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins allowed to make requests
    allow_credentials=True,
    allow_methods=["*"],    # Allows all HTTP methods (GET, POST, PUT, etc.)
    allow_headers=["*"],    # Allows all headers
)

# Include your API routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(events.router, prefix="/events", tags=["events"])
app.include_router(quizzes.router, prefix="/quizzes", tags=["quizzes"])
app.include_router(questions.router, prefix="/questions", tags=["questions"])
app.include_router(answers.router, prefix="/answers", tags=["answers"])

app.include_router(user_quiz.router, prefix="/user_quiz", tags=["user_quiz"])
app.include_router(user_event.router, prefix="/user_event", tags=["user_event"])