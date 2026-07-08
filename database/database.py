import sqlite3
import os

# Database folder
DB_FOLDER = "database"
DB_NAME = "crop_disease.db"
DB_PATH = os.path.join(DB_FOLDER, DB_NAME)


def get_connection():
    """Create a database connection."""
    os.makedirs(DB_FOLDER, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    """Create the predictions table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_name TEXT,
            disease TEXT,
            confidence REAL,
            fertilizer TEXT,
            pesticide TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_prediction(image_name, disease, confidence, fertilizer, pesticide):
    """Save prediction details to the database."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions
        (image_name, disease, confidence, fertilizer, pesticide)
        VALUES (?, ?, ?, ?, ?)
    """, (
        image_name,
        disease,
        confidence,
        fertilizer,
        pesticide
    ))

    conn.commit()
    conn.close()


def get_all_predictions():
    """Fetch all prediction records."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,
               image_name,
               disease,
               confidence,
               fertilizer,
               pesticide,
               created_at
        FROM predictions
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
