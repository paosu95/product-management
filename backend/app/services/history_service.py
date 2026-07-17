from sqlalchemy.orm import Session

from app.models.history import History


def get_history(db: Session):
    return (
        db.query(History)
        .order_by(History.created_at.desc())
        .all()
    )