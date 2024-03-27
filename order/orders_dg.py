import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fonction pour récupérer les données de MySQL et créer un DataFrame
def fetch_data_from_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="orders"
    )
    cursor = conn.cursor()

    # Récupérer les données de la table 'orders'
    cursor.execute("SELECT * FROM orders")
    data = cursor.fetchall()

    # Fermer la connexion
    conn.close()

    # Créer le DataFrame
    df = pd.DataFrame(data, columns=["id", "article", "quantité", "prix", "date", "id_client", "âge_client", "groupe_sanguin"])
    return df

# Fonction pour effectuer une analyse de base et une visualisation
def analyze_data(df):
    # Afficher les statistiques de base
    print("Statistiques de base :")
    print(df.describe())

    # Visualiser la distribution des quantités
    plt.figure(figsize=(10, 6))
    sns.histplot(df["quantité"], bins=20, kde=True)
    plt.title("Distribution des Quantités")
    plt.xlabel("Quantité")
    plt.ylabel("Fréquence")
    plt.show()

    # Visualiser la distribution des prix
    plt.figure(figsize=(10, 6))
    sns.histplot(df["prix"], bins=20, kde=True)
    plt.title("Distribution des Prix")
    plt.xlabel("Prix")
    plt.ylabel("Fréquence")
    plt.show()

    # Visualiser la distribution des âges des clients
    plt.figure(figsize=(10, 6))
    sns.histplot(df["âge_client"], bins=20, kde=True)
    plt.title("Distribution des Âges des Clients")
    plt.xlabel("Âge")
    plt.ylabel("Fréquence")
    plt.show()

    # Visualiser la distribution des groupes sanguins
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='groupe_sanguin')
    plt.title("Distribution des Groupes Sanguins")
    plt.xlabel("Groupe Sanguin")
    plt.ylabel("Nombre")
    plt.show()

if __name__ == "__main__":
    # Récupérer les données de MySQL
    df = fetch_data_from_mysql()

    # Effectuer l'analyse et la visualisation
    analyze_data(df)
