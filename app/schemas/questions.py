from pydantic import BaseModel
from typing import Optional, Dict, Any

class QuestionCreate(BaseModel):
    title: str
    description: Optional[str]
    difficulty: Optional[str]
    tags: Optional[str]
    time_limit: Optional[int]
    memory_limit: Optional[int]
    question_data: Dict[str, Any]


class QuestionResponse(BaseModel):
    uuid: str
    title: str
    difficulty: Optional[str]

    class Config:
        orm_mode = True


class QuestionUpdate(BaseModel):
    title: str
    description: str
    difficulty: str
    tags: str
    time_limit: int
    memory_limit: int
    question_data: Dict[str, Any]


class QuestionPatch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[str] = None
    tags: Optional[str] = None
    time_limit: Optional[int] = None
    memory_limit: Optional[int] = None
    question_data: Optional[Dict[str, Any]] = None