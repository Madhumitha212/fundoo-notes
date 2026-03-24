from sqlalchemy.orm import Session
from src.models.user_model import User
from src.schema.user_schema import *
from loguru import logger

def create_user_service(db: Session, user: UserCreate):
    logger.info(f"Attempting to create user with email: {user.email}")
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        logger.warning(f"User creation failed: Email {user.email} already exists")
        return None

    try:
        new_user = User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        logger.success(f"User created successfully with ID: {new_user.id}")
        return new_user
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        db.rollback()
        raise

def get_all_user_service(db: Session):
    logger.info("Fetching all users from database")
    try:
        users = db.query(User).all()
        logger.success(f"Retrieved {len(users)} users")
        return users
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        raise

def get_user_by_id_service(db: Session, user_id: int):
    logger.info(f"Fetching user with ID: {user_id}")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logger.warning(f"User not found: ID={user_id}")
        return None
    logger.success(f"User retrieved: ID={user.id}")
    return user


def update_user_service(db: Session, user_id: int, user_update: UserUpdate):
    logger.info(f"Updating user ID={user_id}")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logger.warning(f"Update failed: User not found ID={user_id}")
        return None
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    logger.success(f"User updated successfully: ID={user.id}")
    return user

def delete_user_service(db: Session, user_id: int):
    logger.info(f"Deleting user ID={user_id}")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logger.warning(f"Delete failed: User not found ID={user_id}")
        return None
    db.delete(user)
    db.commit()
    logger.success(f"User deleted successfully: ID={user_id}")
    return True




