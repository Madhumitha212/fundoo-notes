from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database_conn import get_db
from src.schema.notes_schema import NoteCreate, NoteUpdate, NoteOut
from src.service.notes import *

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.post("/", response_model=NoteOut)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = create_note_service(db, note)
    if not new_note:
        raise HTTPException(status_code=400, detail="Note creation failed")
    return new_note

@router.get("/", response_model=list[NoteOut])
def get_all_notes(db: Session = Depends(get_db)):
    return get_all_notes_service(db)

@router.get("/{note_id}", response_model=NoteOut)
def get_note_by_id(note_id: int, db: Session = Depends(get_db)):
    note = get_note_by_id_service(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note_update: NoteUpdate, db: Session = Depends(get_db)):
    updated_note = update_note_service(db, note_id, note_update)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    deleted = delete_note_service(db, note_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": f"Note ID={note_id} deleted successfully"}
