from datetime import datetime
from typing import Optional
from pydantic import BaseModel, UUID4


class ClipboardBase(BaseModel):
    text: str
    pinned: bool = False

class ClipboardCreate(ClipboardBase):
    pass

class ClipboardUpdate(BaseModel):
    text: Optional[str] = None
    pinned: Optional[bool] = None

class Clipboard(ClipboardBase):
    id: UUID4
    created_at: datetime

    class Config:
        from_attributes = True

class JournalBase(BaseModel):
    query: str
    session_id: str

class JournalCreate(JournalBase):
    pass

class JournalUpdate(BaseModel):
    query: str

class Journal(JournalBase):
    id: UUID4
    created_at: datetime

    class Config:
        from_attributes = True