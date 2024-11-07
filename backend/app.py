# backend/app.py (within feature/database-service)

# Code to create a table on app startup if it doesn’t exist
@app.before_first_request
def setup_database():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        content TEXT NOT NULL
    );
    """)
    conn.commit()

    # Insert a default message if the table is empty
    cur.execute("SELECT COUNT(*) FROM messages;")
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute("INSERT INTO messages (content) VALUES ('Hello from the database!');")
        conn.commit()
