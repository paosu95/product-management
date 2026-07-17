from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.history import HistoryResponse
from app.services.history_service import get_history

router = APIRouter(
    prefix="/history",
    tags=["History"],
)


@router.get("", response_model=list[HistoryResponse])
def list_history(
    db: Session = Depends(get_db),
):
    return get_history(db)