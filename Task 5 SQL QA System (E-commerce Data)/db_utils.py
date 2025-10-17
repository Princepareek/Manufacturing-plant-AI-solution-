import os
from create_db import create_database

def get_db_uri():
    """Ensure DB exists and return its URI"""
    if not os.path.exists("finance.db"):
        create_database("finance.db")
    return "sqlite:///finance.db"
