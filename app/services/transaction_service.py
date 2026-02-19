import time
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.transaction import Transaction
from app.core.database import SessionLocal


def create_transaction(db: Session, payload) -> Transaction:
    transaction = Transaction(
        transaction_id=payload.transaction_id,
        source_account=payload.source_account,
        destination_account=payload.destination_account,
        amount=payload.amount,
        currency=payload.currency,
        status="PROCESSING",
    )

    print("transaction>>",transaction)
    db.add(transaction)

    try:
        db.commit()
        return transaction
    except IntegrityError:
        db.rollback()

        existing_transaction = (
            db.query(Transaction)
            .filter(Transaction.transaction_id == payload.transaction_id)
            .first()
        )

        if not existing_transaction:
            raise RuntimeError("Transaction insert failed but record not found")

        return existing_transaction





def process_transaction(transaction_id: str):
    db = SessionLocal()

    try:
        time.sleep(30)

        transaction = (
            db.query(Transaction)
            .filter(Transaction.transaction_id == transaction_id)
            .first()
        )

        if not transaction:
            return

        transaction.status = "PROCESSED"
        transaction.processed_at = datetime.now(timezone.utc)

        db.commit()

    finally:
        db.close()


def get_transaction_by_id(db: Session, transaction_id: str):
    return (
        db.query(Transaction)
        .filter(Transaction.transaction_id == transaction_id)
        .all()
    )
