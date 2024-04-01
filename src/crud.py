from sqlalchemy.orm import Session

import src.models
import src.schemas


def get_user(db: Session, user_id: int):
    return db.query(src.models.User).filter(src.models.User.user_id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(src.models.User).offset(skip).limit(limit).all()


def get_user_by_name(db: Session, name: str):
    return db.query(src.models.User).filter(src.models.User.name == name).first()


def create_user(db: Session, user: src.schemas.User):
    db_user = src.models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
