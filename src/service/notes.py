from sqlalchemy.orm import Session
from src.models.notes_model import Note
from src.schema.notes_schema import *
from loguru import logger

def create_note_service(db: Session, note: NoteCreate):
    logger.info(f"Creating note for user_id={note.user_id}")
    try:
        new_note = Note(**note.dict())
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
        logger.success(f"Note created successfully with ID={new_note.id}")
        return new_note
    except Exception as e:
        logger.error(f"Error creating note: {e}")
        db.rollback()
        raise

def get_all_notes_service(db: Session):
    logger.info("Fetching all notes")
    try:
        notes = db.query(Note).all()
        logger.success(f"Retrieved {len(notes)} notes")
        return notes
    except Exception as e:
        logger.error(f"Error fetching notes: {e}")
        raise

def get_note_by_id_service(db: Session, note_id: int):
    logger.info(f"Fetching note with ID={note_id}")
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        logger.warning(f"Note not found: ID={note_id}")
        return None
    logger.success(f"Note retrieved: ID={note.id}")
    return note

def update_note_service(db: Session, note_id: int, note_update: NoteUpdate):
    logger.info(f"Updating note ID={note_id}")
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        logger.warning(f"Update failed: Note not found ID={note_id}")
        return None
    for key, value in note_update.dict(exclude_unset=True).items():
        setattr(note, key, value)
    db.commit()
    db.refresh(note)
    logger.success(f"Note updated successfully: ID={note.id}")
    return note

def delete_note_service(db: Session, note_id: int):
    logger.info(f"Deleting note ID={note_id}")
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        logger.warning(f"Delete failed: Note not found ID={note_id}")
        return None
    db.delete(note)
    db.commit()
    logger.success(f"Note deleted successfully: ID={note_id}")
    return True
