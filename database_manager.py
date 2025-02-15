import sqlite3

class DatabaseManager:
    def __init__(self):
        """ Connect to database and create tables if they don’t exist. """
        self.conn = sqlite3.connect("app_data.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """ Creates necessary tables for storing sums and product details. """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS totals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sum_value INTEGER DEFAULT 0
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                price REAL
            )
        """)
        self.conn.commit()

    def get_latest_sum(self):
        """ Retrieves the latest total sum. """
        self.cursor.execute("SELECT sum_value FROM totals ORDER BY id DESC LIMIT 1")
        result = self.cursor.fetchone()
        return int(result[0]) if result else 0

    def update_sum(self, new_sum):
        """ Updates the total sum. """
        self.cursor.execute("INSERT INTO totals (sum_value) VALUES (?)", (new_sum,))
        self.conn.commit()

    def reset_sum(self):
        """ ✅ Properly resets total sum to 0 and ensures correct database update. """
        self.cursor.execute("DELETE FROM totals")  # ✅ Clear existing totals
        self.cursor.execute("INSERT INTO totals (sum_value) VALUES (0)")  # ✅ Insert new total as 0
        self.conn.commit()

    def store_product(self, name, price):
        """ Stores or updates a product. """
        self.cursor.execute("INSERT OR REPLACE INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    def get_stored_products_text(self):
        """ Returns stored products in a formatted string for UI. """
        self.cursor.execute("SELECT name, price FROM products")
        products = self.cursor.fetchall()
        return "\n".join([f"{name}: ${price}" for name, price in products]) if products else "Stored Products: None"

    def clear_products(self):
        """ Deletes all stored products from the database. """
        self.cursor.execute("DELETE FROM products")
        self.conn.commit()
