from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class HistoryResponse(BaseModel):
    id: int
    product_id: Optional[int]
    product_name: str
    action: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)