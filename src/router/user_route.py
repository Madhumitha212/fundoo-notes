from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database_conn import get_db
from src.schema.user_schema import *
from src.service.user import *

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/create-user", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user_service(db, user)
    if not new_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return new_user

@router.get("/users", response_model=list[UserOut])
def get_all_users(db:Session = Depends(get_db)):
    users = get_all_user_service(db)
    return users

@router.get("/user/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id_service(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/user/{user_id}", response_model=UserOut)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user_service(db, user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user_service(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User with ID {user_id} deleted successfully"}