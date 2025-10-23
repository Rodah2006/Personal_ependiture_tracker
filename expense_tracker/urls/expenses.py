from fastapi import APIRouter

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.get("/")
def read_expenses():
    return {"message": "Welcome to your Expense Tracker API!"}
