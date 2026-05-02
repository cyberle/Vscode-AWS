import sqlite3

# --- TRIGGER: Secret Scanning ---
# This looks like a standard AWS Access Key format
AWS_SECRET_KEY = "AKIAIMOR7S6KEXAMPLE" 
DB_PASSWORD = "admin_password_12345"

def login_user(username, password):
    # Connect to a mock database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # --- TRIGGER: CodeQL SQL Injection (CWE-89) ---
    # DANGER: Using string formatting (f-strings) for SQL queries 
    # allows an attacker to bypass authentication using ' OR '1'='1
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    print(f"Executing query: {query}")
    cursor.execute(query)
    
    return cursor.fetchone()

# Mock usage
user_input = "admin' --" # Example of an injection payload
login_user(user_input, "password")
