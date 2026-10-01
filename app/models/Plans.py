from __future__ import annotations
from typing import Optional
import datetime
import decimal

from sqlalchemy import BINARY, DECIMAL, Date, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.models.Base import Base

class Plans(Base):
    __tablename__ = 'plans'

    plan_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    plan_name: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    billing_frequency: Mapped[str] = mapped_column(String(25), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(200))
    plan_type: Mapped[Optional[str]] = mapped_column(String(25))
    status: Mapped[Optional[str]] = mapped_column(String(20))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    created_by: Mapped[Optional[str]] = mapped_column(String(25))

    subscriptions: Mapped[list['Subscriptions']] = relationship('Subscriptions', back_populates='plan')