import sqlite3
import random
from datetime import datetime, timedelta

def create_database(db_path="finance.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop old tables
    cursor.execute("DROP TABLE IF EXISTS clients;")
    cursor.execute("DROP TABLE IF EXISTS investments;")

    # Create new tables
    cursor.execute("""
    CREATE TABLE clients (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        risk_profile TEXT,
        portfolio_value REAL
    );
    """)

    cursor.execute("""
    CREATE TABLE investments (
        investment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        fund_name TEXT,
        amount_invested REAL,
        date TEXT,
        FOREIGN KEY (client_id) REFERENCES clients (client_id)
    );
    """)

    # Insert dummy data
    risk_profiles = ["Low", "Medium", "High"]
    fund_names = ["Alpha Growth Fund", "Beta Equity Fund", "Gamma Bond Fund", "Delta Index Fund", "Omega Balanced Fund"]

    for i in range(30):
        name = f"Client_{i+1}"
        age = random.randint(25, 70)
        risk = random.choice(risk_profiles)
        portfolio_value = round(random.uniform(20000, 500000), 2)
        cursor.execute("INSERT INTO clients (name, age, risk_profile, portfolio_value) VALUES (?, ?, ?, ?)",
                       (name, age, risk, portfolio_value))

    for i in range(30):
        client_id = random.randint(1, 30)
        fund = random.choice(fund_names)
        amount = round(random.uniform(1000, 20000), 2)
        date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO investments (client_id, fund_name, amount_invested, date) VALUES (?, ?, ?, ?)",
                       (client_id, fund, amount, date))

    conn.commit()
    conn.close()
    print(f"✅ Database '{db_path}' created successfully.")
