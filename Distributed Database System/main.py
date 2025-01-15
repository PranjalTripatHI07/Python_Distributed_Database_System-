from models import User, Product, Order
from database import Database
import threading
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def insert_users(db, user_data):
    try:
        user = User(user_data['id'], user_data['name'], user_data['email'])
        db.insert_user(user)
        logging.info(f"Successfully inserted user: ID={user.id}, Name={user.name}, Email={user.email}")
    except Exception as e:
        logging.error(f"Failed to insert user {user_data['id']}: {str(e)}")

def insert_products(db, product_data):
    try:
        product = Product(product_data['id'], product_data['name'], product_data['price'])
        db.insert_product(product)
        logging.info(f"Successfully inserted product: ID={product.id}, Name={product.name}, Price=${product.price}")
    except Exception as e:
        logging.error(f"Failed to insert product {product_data['id']}: {str(e)}")

def insert_orders(db, order_data):
    try:
        order = Order(order_data['id'], order_data['user_id'], order_data['product_id'], order_data['quantity'])
        db.insert_order(order)
        logging.info(f"Successfully inserted order: ID={order.id}")
    except Exception as e:
        logging.error(f"Failed to insert order {order_data['id']}: {str(e)}")

def display_results(users_db, products_db, orders_db):
    logging.info("\nInsertion Results:")
    
    logging.info("\nUsers:")
    for user in users_db.fetch_all_data():
        logging.info(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    
    logging.info("\nProducts:")
    for product in products_db.fetch_all_data():
        logging.info(f"ID: {product[0]}, Name: {product[1]}, Price: ${product[2]}")
    
    logging.info("\nOrders:")
    for order in orders_db.fetch_all_data():
        logging.info(f"ID: {order[0]}, User ID: {order[1]}, Product ID: {order[2]}, Quantity: {order[3]}")

def main():
    start_time = time.time()
    
    users_db = Database('users.db')
    products_db = Database('products.db')
    orders_db = Database('orders.db')

    users_data = [
        {'id': 1, 'name': "Alice", 'email': "alice@example.com"},
        {'id': 2, 'name': "Bob", 'email': "bob@example.com"},
        {'id': 3, 'name': "Charlie", 'email': "charlie@example.com"},
        {'id': 4, 'name': "David", 'email': "david@example.com"},
        {'id': 5, 'name': "Eve", 'email': "eve@example.com"},
        {'id': 6, 'name': "Frank", 'email': "frank@example.com"},
        {'id': 7, 'name': "Grace", 'email': "grace@example.com"},
        {'id': 8, 'name': "Alice", 'email': "alice@example.com"},
        {'id': 9, 'name': "Henry", 'email': "henry@example.com"},
        {'id': 10, 'name': "Jane", 'email': "jane@example.com"}  # Changed from email to name as per task
    ]

    products_data = [
        {'id': 1, 'name': "Laptop", 'price': 1000.00},
        {'id': 2, 'name': "Smartphone", 'price': 700.00},
        {'id': 3, 'name': "Headphones", 'price': 150.00},
        {'id': 4, 'name': "Monitor", 'price': 300.00},
        {'id': 5, 'name': "Keyboard", 'price': 50.00},
        {'id': 6, 'name': "Mouse", 'price': 30.00},
        {'id': 7, 'name': "Laptop", 'price': 1000.00},
        {'id': 8, 'name': "Smartwatch", 'price': 250.00},
        {'id': 9, 'name': "Gaming Chair", 'price': 500.00},  # Fixed space in name
        {'id': 10, 'name': "Earbuds", 'price': -50.00}
    ]

    orders_data = [
        {'id': 1, 'user_id': 1, 'product_id': 1, 'quantity': 2},
        {'id': 2, 'user_id': 2, 'product_id': 2, 'quantity': 1},
        {'id': 3, 'user_id': 3, 'product_id': 3, 'quantity': 5},
        {'id': 4, 'user_id': 4, 'product_id': 4, 'quantity': 1},
        {'id': 5, 'user_id': 5, 'product_id': 5, 'quantity': 3},
        {'id': 6, 'user_id': 6, 'product_id': 6, 'quantity': 4},
        {'id': 7, 'user_id': 7, 'product_id': 7, 'quantity': 2},
        {'id': 8, 'user_id': 8, 'product_id': 8, 'quantity': 0},
        {'id': 9, 'user_id': 9, 'product_id': 1, 'quantity': -1},
        {'id': 10, 'user_id': 10, 'product_id': 11, 'quantity': 2}
    ]

    threads = []

    # Create threads for users
    for user_data in users_data:
        thread = threading.Thread(target=insert_users, args=(users_db, user_data))
        threads.append(thread)

    # Create threads for products
    for product_data in products_data:
        thread = threading.Thread(target=insert_products, args=(products_db, product_data))
        threads.append(thread)

    # Create threads for orders
    for order_data in orders_data:
        thread = threading.Thread(target=insert_orders, args=(orders_db, order_data))
        threads.append(thread)

    thread_start_time = time.time()

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    thread_end_time = time.time()

    display_results(users_db, products_db, orders_db)
    
    end_time = time.time()
    logging.info(f"\nPerformance Metrics:")
    logging.info(f"Thread execution time: {thread_end_time - thread_start_time} seconds")
    logging.info(f"Total execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
