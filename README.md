# analyse_produits_e-commerce
Analyse des interactions utilisateurs (vues, paniers, achats) sur un site e-commerce à partir de logs d'événements
# 🛍️ Analyse des événements utilisateurs – Dataset Retailrocket

Ce projet présente une analyse exploratoire des événements utilisateurs (vues, ajouts au panier, achats) sur un site e-commerce, à partir du jeu de données public de **Retailrocket**. Il s'inscrit dans une logique de **compréhension du comportement client** et de préparation pour un **système de recommandation**.

---

## 📦 Jeu de données

Le jeu de données utilisé est issu de la plateforme [Retailrocket](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset), et contient 3 fichiers principaux :

- `events.csv` : enregistre les interactions utilisateurs (`view`, `addtocart`, `transaction`)
- `item_properties.csv` : caractéristiques des produits (catégorie, prix, etc.)
- `category_tree.csv` : hiérarchie des catégories

Dans ce projet, nous nous concentrons sur le fichier **`events.csv`**.

---

## 🎯 Objectifs du projet

- Analyser les types d’événements (vues, paniers, achats)
- Identifier les produits les plus populaires
- Extraire des KPI clés : taux de conversion, visiteurs uniques, produits les plus performants
- Visualiser le parcours utilisateur par type d'interaction
- Implémenter une recommandation simple de produits basée sur la fréquence

---

## 🛠️ Technologies utilisées

- **Python 3**
- **Pandas** – manipulation de données
- **Matplotlib & Seaborn** – visualisation
- **Jupyter Notebook** – environnement interactif
- **Git / GitHub** – versioning et partage

---

## 🗂️ Structure du projet

```bash
retailrocket-analysis/
│
├── data/
│   └── events.csv             # Fichier principal utilisé dans cette analyse
│
├── notebooks/
│   └── analyse_retail.ipynb   # Notebook Jupyter complet de l’analyse
│
├── outputs/
│   └── visualisations.png     # Graphiques produits (top produits, courbes, etc.)
│
├── scripts/
│   └── recommandation.py      # Script Python de recommandation simple
│
├── requirements.txt           # Bibliothèques nécessaires pour exécuter le projet
├── README.md                  # Ce fichier
└── .gitignore

