from fastapi import FastAPI
from expense_tracker.urls import expenses
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

# Create the FastAPI app instance
expense_tracker = FastAPI()

# Include the routes from expenses.py
expense_tracker.include_router(expenses.router)

# Add a home route (so / shows something instead of 404)
@expense_tracker.get("/")
def home_route():
    return { "Welcome to your Expense Tracker API!"}
