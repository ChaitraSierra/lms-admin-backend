from fastapi import FastAPI
from .routes.admin import admin_questions,meta
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LMS Admin Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://192.168.1.103:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(admin_questions.router)
app.include_router(meta.router)

