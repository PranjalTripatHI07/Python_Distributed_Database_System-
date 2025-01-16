import sqlite3
import threading
import logging

class Database:
    _lock = threading.Lock()
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Drop existing tables for clean start
                if 'users.db' in self.db_name:
                    cursor.execute('DROP TABLE IF EXISTS users')
                elif 'products.db' in self.db_name:
                    cursor.execute('DROP TABLE IF EXISTS products')
                elif 'orders.db' in self.db_name:
                    cursor.execute('DROP TABLE IF EXISTS orders')
                
                if 'users.db' in self.db_name:
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE
                        )
                    ''')
                elif 'products.db' in self.db_name:
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            price REAL NOT NULL
                        )
                    ''')
                elif 'orders.db' in self.db_name:
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS orders (
                            id INTEGER PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            product_id INTEGER NOT NULL,
                            quantity INTEGER NOT NULL
                        )
                    ''')
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database initialization error: {e}")
            raise

    def insert_user(self, user):
        with Database._lock, sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (id, name, email) VALUES (?, ?, ?)',
                         (user.id, user.name, user.email))
            conn.commit()

    def insert_product(self, product):
        with Database._lock, sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO products (id, name, price) VALUES (?, ?, ?)',
                         (product.id, product.name, product.price))
            conn.commit()

    def insert_order(self, order):
        with Database._lock, sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO orders (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)',
                         (order.id, order.user_id, order.product_id, order.quantity))
            conn.commit()

    def fetch_all_data(self):
        try:
            with Database._lock, sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                table_name = self.db_name.split('.')[0]
                cursor.execute(f'SELECT * FROM {table_name}')
                return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error fetching data: {e}")
            return []
