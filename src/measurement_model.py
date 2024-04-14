from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class MeasurementBase(SQLModel):
    type: str
    value: float
    user_id: int = Field(default=None, foreign_key="user.user_id")


class Measurement(MeasurementBase, table=True):
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    measurement_id: int = Field(default=None, primary_key=True)


class MeasurementCreate(MeasurementBase):
    created_at: Optional[datetime]


class MeasurementRead(MeasurementBase):
    measurement_id: int
    created_at: datetime
