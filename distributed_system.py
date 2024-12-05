import sqlite3
import threading
import time
import logging

# Configure logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")


# define Function to create database and tables
def setup_database(db_name, table_query):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(table_query)
        conn.commit()
        logging.info(f"Database setup complete: {db_name}")
    except sqlite3.Error as e:
        logging.error(f"Error setting up database {db_name}: {e}")
    finally:
        conn.close()


# define Function to validate and insert users
def insert_users():
    users = [
        (1, "Alice", "alice@example.com"),
        (2, "Bob", "bob@example.com"),
        (3, "Charlie", "charlie@example.com"),
        (4, "David", "david@example.com"),
        (5, "Eve", "eve@example.com"),
        (6, "Frank", "frank@example.com"),
        (7, "Grace", "grace@example.com"),
        (8, "Henry", "henry@example.com"),
        (9, "Ivy", "ivy@example.com"),
        (10, "Jack", "jack@example.com"),
    ]
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        for user in users:
            if not user[1] or "@" not in user[2]:
                logging.warning(f"Skipping invalid user: {user}")
                continue
            cursor.execute("INSERT INTO users (id, name, email) VALUES (?, ?, ?)", user)
            conn.commit()
            logging.info(f"Inserted User: {user}")
            time.sleep(0.1)
    except sqlite3.Error as e:
        logging.error(f"Error inserting into users: {e}")
    finally:
        conn.close()


# define Function to validate and insert products
def insert_products():
    products = [
        (1, "Laptop", 1000.00),
        (2, "Smartphone", 700.00),
        (3, "Headphones", 150.00),
        (4, "Monitor", 300.00),
        (5, "Keyboard", 50.00),
        (6, "Mouse", 30.00),
        (7, "Smartwatch", 250.00),
        (8, "Gaming Chair", 500.00),
        (9, "Tablet", 600.00),
        (10, "Earbuds", 80.00),
    ]
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        for product in products:
            if product[2] < 0:  # Validate price
                logging.warning(f"Skipping invalid product: {product}")
                continue
            cursor.execute("INSERT INTO products (id, name, price) VALUES (?, ?, ?)", product)
            conn.commit()
            logging.info(f"Inserted Product: {product}")
            time.sleep(0.1)
    except sqlite3.Error as e:
        logging.error(f"Error inserting into products: {e}")
    finally:
        conn.close()


# define Function to validate and insert orders
def insert_orders():
    orders = [
        (1, 1, 1, 2),
        (2, 2, 2, 1),
        (3, 3, 3, 5),
        (4, 4, 4, 1),
        (5, 5, 5, 3),
        (6, 6, 6, 4),
        (7, 7, 7, 2),
        (8, 8, 8, 1),
        (9, 9, 9, 3),
        (10, 10, 10, 2),
    ]
    try:
        conn = sqlite3.connect("orders.db")
        cursor = conn.cursor()
        for order in orders:
            if order[3] <= 0:  # Validate quantity
                logging.warning(f"Skipping invalid order: {order}")
                continue
            cursor.execute("INSERT INTO orders (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)", order)
            conn.commit()
            logging.info(f"Inserted Order: {order}")
            time.sleep(0.1)
    except sqlite3.Error as e:
        logging.error(f"Error inserting into orders: {e}")
    finally:
        conn.close()


# define Main function to setup databases and run threads
def main():
    # SQL queries to create tables
    user_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )"""
    product_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )"""
    order_table_query = """
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL
    )"""

    # Setup databases
    setup_database("users.db", user_table_query)
    setup_database("products.db", product_table_query)
    setup_database("orders.db", order_table_query)

    # Create and start threads
    user_thread = threading.Thread(target=insert_users)
    product_thread = threading.Thread(target=insert_products)
    order_thread = threading.Thread(target=insert_orders)

    user_thread.start()
    product_thread.start()
    order_thread.start()

    # Wait for threads to finish
    user_thread.join()
    product_thread.join()
    order_thread.join()

    print("All data insertion completed. Check 'app.log' for details.")


if __name__ == "__main__":
    main()
