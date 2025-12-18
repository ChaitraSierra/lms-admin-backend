from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    DateTime
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from uuid import uuid4

from ..database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    
    uuid = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid4)

    title = Column(Text, nullable=False)

    description = Column(Text)

    difficulty = Column(String(20))

    tags = Column(Text)

    time_limit = Column(Integer)

    memory_limit = Column(Integer)

    question_data = Column(JSONB)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    deleted_at = Column(DateTime(timezone=True))
