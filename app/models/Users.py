from __future__ import annotations
from typing import Optional
import datetime

from sqlalchemy import BINARY, DECIMAL, Date, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from app.models.Base import Base

class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        Index('email', 'email', unique=True),
    )

    user_id: Mapped[bytes] = mapped_column(BINARY(16), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(25), nullable=False)
    last_name: Mapped[str] = mapped_column(String(25), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    subscriptions: Mapped[list['Subscriptions']] = relationship('Subscriptions', back_populates='user')