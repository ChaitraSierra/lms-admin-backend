from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4
from uuid import UUID

from ...database import SessionLocal
from ...models.questions import Question
from ...schemas.questions import QuestionCreate,QuestionUpdate,QuestionPatch

router = APIRouter(prefix="/admin/questions", tags=["Admin Questions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE QUESTION
@router.post("")
def create_question(payload: QuestionCreate, db: Session = Depends(get_db)):
    question = Question(
        uuid=uuid4(),
        title=payload.title,
        description=payload.description,
        difficulty=payload.difficulty,
        tags=payload.tags,
        time_limit=payload.time_limit,
        memory_limit=payload.memory_limit,
        question_data=payload.question_data
    )

    db.add(question)
    db.commit()
    db.refresh(question)

    return {
        "uuid": str(question.uuid),
        "message": "Question created successfully"
    }


# LIST QUESTIONS
@router.get("")
def list_questions(db: Session = Depends(get_db)):
    questions = (
        db.query(Question)
        .filter(Question.deleted_at == None)
        .order_by(Question.created_at.desc())
        .all()
    )

    return [
        {
            "uuid": str(q.uuid),
            "title": q.title,
            "difficulty": q.difficulty,
            "tags":q.tags,
            "created_at": q.created_at
        }
        for q in questions
    ]


# GET SINGLE QUESTION
@router.get("/{uuid}")
def get_question(uuid:UUID, db: Session = Depends(get_db)):
    q = db.query(Question).filter(Question.uuid == uuid , Question.deleted_at.is_(None)).first()

    if not q:
        raise HTTPException(status_code=404,detail="Question not found")

    return {
    "uuid": str(q.uuid),
    "title": q.title,
    "description": q.description,
    "difficulty": q.difficulty,
    "tags": q.tags,
    "time_limit": q.time_limit,
    "memory_limit": q.memory_limit,
    "question_data": q.question_data
}



# SOFT DELETE
@router.delete("/{uuid}")
def delete_question(uuid: UUID, db: Session = Depends(get_db)):
    q = db.query(Question).filter(Question.uuid == uuid , Question.deleted_at.is_(None)).first()

    if not q:
        raise HTTPException(status_code=404,detail="Question was not found !")

    from sqlalchemy.sql import func
    q.deleted_at = func.now()
    db.commit()

    return {
        "message": "Question deleted",
        "uuid": q.uuid,
        "title": q.title
        }


# PUT METHOD
@router.put("/{uuid}")
def update_question(uuid:UUID, payload:QuestionUpdate,db:Session=Depends(get_db)):
    question=(
        db.query(Question).
        filter(Question.uuid==uuid,
               Question.deleted_at==None)
            ).first();
    
    if not question:
        raise HTTPException(status_code=404,detail="Question was not found")
    
    question.title=payload.title
    question.description=payload.description
    question.difficulty=payload.difficulty
    question.tags=payload.tags
    question.question_data=payload.question_data
    question.time_limit=payload.time_limit
    question.memory_limit=payload.memory_limit
    
    db.add(question)
    db.commit()
    db.refresh(question)
    
    return {
        "message": "Question Updated successfully",
        "uuid":str(question.uuid),
        "title":question.title,
        "description":question.description
    }
     



# Patch Method
@router.patch("/{uuid}")
def partial_update_question(uuid:UUID, payload:QuestionPatch,db:Session=Depends(get_db)):
    question=(
            db.query(Question)
            .filter(Question.uuid==uuid,
                    Question.deleted_at.is_(None)
                    )
    ).first()
    
    if not question:
        raise HTTPException(status_code=404,detail="Question not found")
    
    update_data=payload.model_dump(exclude_unset=True)
    
    for fields,values in update_data.items():
        setattr(question,fields,values)
        
        
    db.commit()
    db.refresh(question)
    
    return{
        "message": "Question field/fields updated successfully",
        "uuid":question.uuid,
        "title":question.title,
        "description":question.description
        
    }
    