from fastapi import FastAPI
from .routes import admin_questions

app = FastAPI(title="LMS Admin Backend")

app.include_router(admin_questions.router)
