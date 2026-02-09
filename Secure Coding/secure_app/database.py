import sqlite3

def get_user_secure(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Parameterized query (prevents SQL injection)
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()
    return user
