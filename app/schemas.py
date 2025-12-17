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
