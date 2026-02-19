from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class TransactionWebhookRequest(BaseModel):
    transaction_id: str = Field(..., example="txn_abc123def456")
    source_account: str = Field(..., example="acc_user_789")
    destination_account: str = Field(..., example="acc_merchant_456")
    amount: float = Field(..., gt=0, example=1500)
    currency: str = Field(..., example="INR")
    status: Optional[str]


class TransactionBase(BaseModel):
    transaction_id: str
    source_account: str
    destination_account: str
    amount: float
    currency: str


class TransactionResponse(TransactionBase):
    status: str
    created_at: datetime
    processed_at: Optional[datetime]

    class Config:
        from_attributes = True
   
