import sqlite3

def create_database():
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('wallet_database.db')
    cursor = conn.cursor()

    # Create a table with a string for the wallet and four integers
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS wallets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        wallet TEXT NOT NULL,
        value1 INTEGER NOT NULL,
        value2 INTEGER NOT NULL,
        value3 INTEGER NOT NULL,
        value4 INTEGER NOT NULL
    )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Database and table created successfully!")

if __name__ == "__main__":
    create_database()