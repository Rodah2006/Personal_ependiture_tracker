from sqlalchemy.orm import Session
from . import models, schemas

#  CREATE an expense
def create_expense(db: Session, expense: schemas.ExpenseCreate):
    new_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


#  READ all expenses
def get_expenses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Expense).offset(skip).limit(limit).all()


#  READ one expense by ID
def get_expense_by_id(db: Session, expense_id: int):
    return db.query(models.Expense).filter(models.Expense.id == expense_id).first()


#  UPDATE an expense
def update_expense(db: Session, expense_id: int, updated_expense: schemas.ExpenseUpdate):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if expense:
        expense.title = updated_expense.title
        expense.amount = updated_expense.amount
        expense.category = updated_expense.category
        db.commit()
        db.refresh(expense)
        return expense
    return None


#  DELETE an expense
def delete_expense(db: Session, expense_id: int):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if expense:
        db.delete(expense)
        db.commit()
        return True
    return False
