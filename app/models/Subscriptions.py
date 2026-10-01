from typing import Optional
import datetime

from sqlalchemy import BINARY, DECIMAL, Date, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.models.Base import Base

class Subscriptions(Base):
    __tablename__ = 'subscriptions'
    __table_args__ = (
        ForeignKeyConstraint(['plan_id'], ['plans.plan_id'], name='fk_subscription_plan'),
        ForeignKeyConstraint(['user_id'], ['users.user_id'], name='fk_subscription_user'),
        Index('fk_subscription_plan', 'plan_id'),
        Index('fk_subscription_user', 'user_id')
    )

    subscription_id: Mapped[bytes] = mapped_column(BINARY(16), primary_key=True)
    user_id: Mapped[bytes] = mapped_column(BINARY(16), nullable=False)
    plan_id: Mapped[int] = mapped_column(Integer, nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String(25), nullable=False)
    subscription_name: Mapped[Optional[str]] = mapped_column(String(100))
    subscription_type: Mapped[Optional[str]] = mapped_column(String(25))
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    created_by: Mapped[Optional[str]] = mapped_column(String(25))

    plan: Mapped['Plans'] = relationship('Plans', back_populates='subscriptions')
    user: Mapped['Users'] = relationship('Users', back_populates='subscriptions')
    payments: Mapped[list['Payments']] = relationship('Payments', back_populates='subscription')