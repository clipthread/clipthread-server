from fastapi import APIRouter, HTTPException
from typing import Optional

from clipthread.server.models.schemas import ClipboardCreate, ClipboardUpdate, Clipboard
from clipthread.core.db import ClipboardHandler

router = APIRouter()
clipboard_handler = ClipboardHandler("database.db")

@router.post("/", response_model=Clipboard)
def create_clipboard(clip: ClipboardCreate) -> Clipboard:
    clip_id = clipboard_handler.create(text=clip.text, pinned=clip.pinned)
    return clipboard_handler.read(clip_id)

@router.get("/{clip_id}", response_model=Clipboard)
def read_clipboard(clip_id: str):
    result = clipboard_handler.read(clip_id)
    if not result:
        raise HTTPException(status_code=404, detail="Clipboard entry not found")
    return result

@router.put("/{clip_id}", response_model=Clipboard)
def update_clipboard(clip_id: str, clip: ClipboardUpdate):
    success = clipboard_handler.update(
        clip_id, 
        text=clip.text, 
        pinned=clip.pinned
    )
    if not success:
        raise HTTPException(status_code=404, detail="Clipboard entry not found")
    return clipboard_handler.read(clip_id)

@router.delete("/{clip_id}")
def delete_clipboard(clip_id: str):
    success = clipboard_handler.delete(clip_id)
    if not success:
        raise HTTPException(status_code=404, detail="Clipboard entry not found")
    return {"message": "Clipboard entry deleted"}