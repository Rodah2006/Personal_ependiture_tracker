from fastapi import FastAPI
from expense_tracker.urls import expenses

# Create the FastAPI app instance
expense_tracker = FastAPI()

# Include the routes from expenses.py
expense_tracker.include_router(expenses.router)

# Add a home route (so / shows something instead of 404)
@expense_tracker.get("/")
def read_root():
    return { "Welcome to your Expense Tracker API!"}
