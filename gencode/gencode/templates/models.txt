from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid
import enum

from .database import Base

class State(enum.Enum):
    NEW = "NEW"
    INSTALLING = "INSTALLING"
    RUNNING = "RUNNING"

class App(Base):
    __tablename__ = "apps"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    kind = Column(String)
    name = Column(String)
    version = Column(String)
    description = Column(String)
    state = Column(Enum(State), default=State.NEW)
    json = Column(JSONB)