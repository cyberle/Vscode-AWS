import sqlite3
import sys
# --- TRIGGER: Secret Scanning ---
# This looks like a standard AWS Access Key format
# Slack Bot Token pattern (GitHub almost always catches this)
# SLACK_TOKEN = "xoxb-123456789012-123456789012-AaBbCcDdEeFfGgHhIiJjKkLl"

# Stripe Secret Key pattern
# STRIPE_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

from flask import Flask, request

app = Flask(__name__)

@app.route('/get-user')
def get_user():
    # 'request.args' is a standard "Source" for CodeQL
    user_id = request.args.get('id')
    
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    # The 'Sink': String concatenation in a SQL execution
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    
    return str(cursor.fetchall())

if __name__ == "__main__":
    app.run()
