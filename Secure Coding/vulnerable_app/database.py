import sqlite3

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # ❌ No input validation
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")

    data = cursor.fetchall()
    conn.close()
    return data
