from typing import Optional, Sequence

from sqlmodel import Session, select

from src.models import User, UserCreate


def get_user_by_name(db: Session, name: str) -> Optional[User]:
    return db.exec(select(User).where(User.name == name)).first()


def create_user(db: Session, user: UserCreate) -> User:
    user = User.model_validate(user)  # type: ignore
    db.add(user)
    db.commit()
    db.refresh(user)
    return user  # type: ignore


def get_users(db: Session, skip: int = 0, limit: int = 100) -> Sequence[User]:
    return db.exec(select(User).offset(skip).limit(limit)).all()


def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.exec(select(User).where(User.user_id == user_id)).first()
