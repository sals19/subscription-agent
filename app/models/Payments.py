from typing import Optional
import datetime
import decimal

from sqlalchemy import BINARY, DECIMAL, Date, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.Base import Base

class Payments(Base):
    __tablename__ = 'payments'
    __table_args__ = (
        ForeignKeyConstraint(['subscription_id'], ['subscriptions.subscription_id'], name='fk_payment_subscription'),
        Index('fk_payment_subscription', 'subscription_id')
    )

    payment_id: Mapped[bytes] = mapped_column(BINARY(16), primary_key=True)
    subscription_id: Mapped[bytes] = mapped_column(BINARY(16), nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False)
    payment_date: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    subscription: Mapped['Subscriptions'] = relationship('Subscriptions', back_populates='payments')