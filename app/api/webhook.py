from fastapi import APIRouter, Depends, BackgroundTasks, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.transaction import TransactionWebhookRequest
from app.services.transaction_service import (
    create_transaction,
    process_transaction,
)


router = APIRouter(
    prefix="/v1/webhooks",
    tags=["Webhooks"]
)

@router.post(
    "/transactions",
    status_code=status.HTTP_202_ACCEPTED
)
def receive_transaction_webhook(
    payload: TransactionWebhookRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    transaction = create_transaction(db, payload)

    if transaction.status == "PROCESSING":
        background_tasks.add_task(
        process_transaction,
        transaction.transaction_id,
       )
    return {"message": "Webhook received"}

