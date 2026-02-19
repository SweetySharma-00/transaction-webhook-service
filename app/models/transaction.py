from sqlalchemy import Column, Integer, String, Numeric, DateTime
from app.core.database import Base
from datetime import datetime, timezone


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(String, unique=True, index=True, nullable=False)

    source_account = Column(String, nullable=False)
    destination_account = Column(String, nullable=False)

    amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String, nullable=False)

    status = Column(String, nullable=False, default="PROCESSING")

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    processed_at = Column(
        DateTime(timezone=True),
        nullable=True
    )
