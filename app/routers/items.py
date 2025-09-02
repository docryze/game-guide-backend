from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.post("/", response_model=schemas.Item)
def create_item_for_user(
    item: schemas.ItemCreate,
    user_id: int,
    db: Session = Depends(get_db)
):
    db_item = models.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/", response_model=List[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items
