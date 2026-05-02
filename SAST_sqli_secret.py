import sqlite3
import sys
# --- TRIGGER: Secret Scanning ---
# This looks like a standard AWS Access Key format
AWS_SECRET_KEY = "AKIA5F7D6E2B4C1A8Z9X" 
INTERNAL_API_SECRET = "7b25762a492b4a3952454a4b36326b38466b7331"

def run_query():
    # CodeQL recognizes sys.argv as an "untrusted source"
    user_id = sys.argv[1] 
    
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    # DANGER: String concatenation with untrusted input
    # CodeQL will trace 'user_id' from sys.argv into this execution
    query = "SELECT * FROM accounts WHERE id = " + user_id
    
    print(f"DEBUG: Executing {query}") # This triggers the logging alert you saw
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    run_query()
