from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


#  CREATE Expense
@router.post("/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db=db, expense=expense)


#  READ All Expenses
@router.get("/", response_model=list[schemas.Expense])
def read_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    expenses = crud.get_expenses(db, skip=skip, limit=limit)
    return expenses


#  READ Single Expense by ID
@router.get("/{expense_id}", response_model=schemas.Expense)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = crud.get_expense_by_id(db, expense_id=expense_id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


#  UPDATE Expense
@router.put("/{expense_id}", response_model=schemas.Expense)
def update_expense(expense_id: int, expense: schemas.ExpenseUpdate, db: Session = Depends(get_db)):
    updated = crud.update_expense(db, expense_id=expense_id, updated_expense=expense)
    if updated is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated


# 🔴 DELETE Expense
@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_expense(db, expense_id=expense_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense deleted successfully"}
