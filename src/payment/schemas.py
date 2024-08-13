from typing import Optional

from pydantic import BaseModel


class PaymentRequest(BaseModel):
    service_id: int
    reference: str
    amount: float
    additional_info: Optional[dict] = None
