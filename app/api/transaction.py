from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.transaction import TransactionResponse
from app.services.transaction_service import get_transaction_by_id


router = APIRouter(
    prefix="/v1/transactions",
    tags=["Transactions"]
)


@router.get(
    "/{transaction_id}",
    response_model=List[TransactionResponse]
)
def get_transaction(
    transaction_id: str,
    db: Session = Depends(get_db),
):
    transactions = get_transaction_by_id(db, transaction_id)

    if not transactions:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transactions


