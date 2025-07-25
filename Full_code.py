#  1. Importation des bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  2. Chargement et filtrage des données
# Remplacer le chemin par le tien
df = pd.read_csv('events.csv')

# On garde uniquement les événements intéressants
df = df[df['event'].isin(['view', 'addtocart', 'transaction'])]

# 3. Transformation de la colonne "timestamp"
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df['date'] = df['timestamp'].dt.date
df['hour'] = df['timestamp'].dt.hour
df['dayofweek'] = df['timestamp'].dt.day_name()

#  4. Statistiques descriptives
print("✅ Aperçu des données :")
print(df.head())

print("\n📊 Répartition des types d’événements :")
print(df['event'].value_counts())

print("\n👥 Nombre de visiteurs uniques :", df['visitorid'].nunique())
print("📦 Nombre d'articles différents :", df['itemid'].nunique())

#  5. Analyse des produits populaires

# Produits les plus vus
top_viewed = df[df['event'] == 'view']['itemid'].value_counts().head(10)

# Produits les plus ajoutés au panier
top_carted = df[df['event'] == 'addtocart']['itemid'].value_counts().head(10)

# Produits les plus achetés
top_purchased = df[df['event'] == 'transaction']['itemid'].value_counts().head(10)

print("\n🔝 Produits les plus vus :\n", top_viewed)
print("\n🛒 Produits les plus ajoutés au panier :\n", top_carted)
print("\n💰 Produits les plus achetés :\n", top_purchased)

#  6. Visualisation des résultats


plt.figure(figsize=(12, 4))
plt.suptitle('Classement top 10 des produits les plus attractifs par étape du parcours client', fontsize=16)
plt.subplot(1, 3, 1)
top_viewed.plot(kind='bar', title='Top Vues', color='skyblue')
plt.xticks(rotation=45)

plt.subplot(1, 3, 2)
top_carted.plot(kind='bar', title='Top Ajouts Panier', color='orange')
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
top_purchased.plot(kind='bar', title='Top Achats', color='green')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# 7. Taux de conversion simple

total_views = df[df['event'] == 'view'].shape[0]
total_purchases = df[df['event'] == 'transaction'].shape[0]
conversion_rate = total_purchases / total_views * 100
print(f"\n📈 Taux de conversion (achats / vues) : {conversion_rate:.2f}%")

#  8. Fonction de recommandation simple

def recommend_top_products(df, event_type='transaction', n=5):
    """
    Recommande les produits les plus populaires selon le type d'événement.
    event_type : 'view', 'addtocart' ou 'transaction'
    """
    top_items = df[df['event'] == event_type]['itemid'].value_counts().head(n)
    return top_items.index.tolist()

# Exemple : top 5 produits les plus achetés
recommendations = recommend_top_products(df, event_type='transaction', n=5)
print("\n🎁 Recommandation simple (produits les plus achetés) :", recommendations)
