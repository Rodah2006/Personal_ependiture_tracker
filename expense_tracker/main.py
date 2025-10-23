from fastapi import FastAPI
from urls import expenses

# create the FastAPI instance
expense_tracker = FastAPI(title="Personal Expense Tracker")

# include routes
expense_tracker.include_router(expenses.router)

@expense_tracker.get("/")
def home():
    return {"message": "Welcome to the Personal Expense Tracker API "}
