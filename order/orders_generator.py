import os
import json
import random
import pickle


class RandomDate:
    def __init__(self):
        self.date = 20240112  # Date initiale: 12 janvier 2015
        self.time_step = ([0] * 20) + ([1] * 4) + ([2] * 2) + [3]

    def generate(self):
        day = self.date % 28
        month = (self.date // 100) % 100
        year = self.date // 10000
        formatted_date = f"{day:02d}/{month:02d}/{year:02d}"
        # Augmentation de la date avec un nombre aléatoire de jours entre 1 et 30
        self.date += random.choice(self.time_step)
        return formatted_date


# Listes de valeurs possibles pour chaque colonne
articles = ["Pomme", "Banane", "Orange", "Fraise", "Pastèque", "Ananas"]
quantities = list(range(1, 21))
prices = [0.99, 1.49, 1.99, 2.49, 2.99]
random_date = RandomDate()
blood_groups = ["A", "B", "AB", "O"]


# Fonction pour générer une commande aléatoire
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


# Fonction pour générer plusieurs commandes aléatoires
def generate_random_orders(num_orders):
    orders = []
    for _ in range(num_orders):
        orders.append(generate_random_order())
    return orders


# écrire les commandes sous la forme json (créant un nouveau fichier à chaque fois)
def write_orders(random_orders):
    number = 0
    file_name = f"orders{number}.json"
    while os.path.exists(file_name):
        number += 1
        file_name = f"orders{number}.json"
    # Export des commandes au format JSON
    with open(file_name, "w") as f:
        json.dump(random_orders, f, indent=4)


def save_date():
    with open(".save", "wb") as file:
        pickle.dump(random_date.date, file)


def get_date():
    if os.path.exists(".save"):
        with open(".save", "rb") as file:
            random_date.date = pickle.load(file)


# Nombre de commandes à générer
num_orders_to_generate = 10

# Génération des commandes aléatoires
get_date()
random_orders = generate_random_orders(num_orders_to_generate)
write_orders(random_orders)
save_date()

print("Les commandes ont été exportées avec succès")
