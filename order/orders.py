import os
import json
import random
import pickle
import mysql.connector


class RandomDate:
    def __init__(self):
        self.date = 20240112  # Initial date: January 12, 2024
        self.time_step = ([0] * 20) + ([1] * 4) + ([2] * 2) + [3]

    def generate(self):
        day = self.date % 28
        month = (self.date // 100) % 100
        year = self.date // 10000
        formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
        self.date += random.choice(self.time_step)
        return formatted_date


# Lists of possible values for each column
articles = ["Pomme", "Banane", "Orange", "Fraise", "Pastèque", "Ananas"]
quantities = list(range(1, 21))
prices = [0.99, 1.49, 1.99, 2.49, 2.99]
random_date = RandomDate()
blood_groups = ["A", "B", "AB", "O"]


# Function to generate a random order
def generate_random_order():
    order_id = random.randint(1000, 9999)
    article = articles[order_id % 5]
    quantity = random.choice(quantities)
    price = prices[order_id % 5]
    client_id = random.randint(1000, 9999)
    age = random.randint(18, 75)
    blood_group = random.choice(blood_groups)

    return {
        "id": order_id,
        "article": article,
        "quantity": quantity,
        "price": price,
        "date": random_date.generate(),
        "client_id": client_id,
        "client_age": age,
        "blood_group": blood_group
    }


# Function to generate multiple random orders
def generate_random_orders(num_orders):
    orders = []
    for _ in range(num_orders):
        orders.append(generate_random_order())
    return orders


# Function to write orders to MySQL
def write_orders_to_mysql(random_orders):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="orders"
    )
    cursor = conn.cursor()

    for order in random_orders:
        sql = "INSERT INTO orders (id, article, quantity, price, date, client_id, client_age, blood_group) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (order["id"], order["article"], order["quantity"], order["price"], order["date"], order["client_id"], order["client_age"], order["blood_group"])
        cursor.execute(sql, val)

    conn.commit()
    conn.close()


# Function to save the current date
def save_date():
    with open(".save", "wb") as file:
        pickle.dump(random_date.date, file)


# Function to retrieve the saved date
def get_date():
    if os.path.exists(".save"):
        with open(".save", "rb") as file:
            random_date.date = pickle.load(file)


# Number of orders to generate
num_orders_to_generate = 10

# Generate random orders
get_date()
random_orders = generate_random_orders(num_orders_to_generate)

# Export orders to MySQL
write_orders_to_mysql(random_orders)
save_date()

print("Orders have been successfully exported to MySQL")
