from pydantic import BaseModel

class NoteCreate(BaseModel):
    user_id: int
    description: str

class NoteUpdate(BaseModel):
    # Make fields optional for partial updates
    description: str | None = None

class NoteOut(BaseModel):
    id: int
    user_id: int
    description: str

    class Config:
        from_attributes = True
