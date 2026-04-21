import sqlite3
import secrets
import os

# Fix 1: environment variable
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Fix 2: parameterized query
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    return cursor.fetchall()

def generate_otp():
    # Fix 3: secure random
    return secrets.randbelow(900000) + 100000
