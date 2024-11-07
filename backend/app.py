<<<<<<< HEAD
# backend/app.py

from flask import Flask, jsonify, request
import psycopg2
import redis
import os

app = Flask(__name__)

# PostgreSQL connection
conn = psycopg2.connect(
    host="database",
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)
cur = conn.cursor()

# Redis connection
cache = redis.StrictRedis(host="cache", port=6379, decode_responses=True)

@app.route("/api/message", methods=["GET"])
def get_message():
    # Check cache first
    message = cache.get("message")
    if message:
        return jsonify({"message": message, "cached": True})

    # If not in cache, retrieve from DB
    cur.execute("SELECT content FROM messages LIMIT 1;")
    message = cur.fetchone()[0]
    cache.set("message", message)  # Cache it for future requests
    return jsonify({"message": message, "cached": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
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
>>>>>>> feature/database-service
