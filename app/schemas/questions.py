from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Dict, Any

class QuestionCreate(BaseModel):
    title: str
    question_data:Dict[str,Any]
    
    description: Optional[str] = None
    difficulty: Optional[str] = None
    tags: Optional[str] = None
    time_limit: Optional[int] = None
    memory_limit: Optional[int] = None

class QuestionListResponse(BaseModel):
    uuid: UUID
    title: str
    difficulty: Optional[str]
    time_limit:Optional[int]
    tags: Optional[str]

    class Config:
        from_attributes = True
        
        
class QuestionResponse(BaseModel):
   uuid: UUID
   title: str
   description: Optional[str]
   difficulty: Optional[str]
   tags: Optional[str]
   time_limit: Optional[int]
   memory_limit: Optional[int]
   question_data: Dict[str, Any]
   
   class Config:
        from_attributes = True


class QuestionUpdate(BaseModel):
     title: str
     question_data:Dict[str,Any]
     
     description: Optional[str] = None
     difficulty: Optional[str] = None
     tags: Optional[str] = None
     time_limit: Optional[int] = None
     memory_limit: Optional[int] = None


class QuestionPatch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[str] = None
    tags: Optional[str] = None
    time_limit: Optional[int] = None
    memory_limit: Optional[int] = None
    question_data: Optional[Dict[str, Any]] = None