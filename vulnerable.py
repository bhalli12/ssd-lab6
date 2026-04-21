import sqlite3
import random

DB_PASSWORD = "admin123"   #  Hardcoded password

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    #  SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    return cursor.fetchall()

def generate_otp():
    #  Not secure random
    return random.randint(100000, 999999)

unused_count = 0   #  Unused variable
