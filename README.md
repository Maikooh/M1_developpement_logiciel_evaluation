# Système de Gestion de Locations de Véhicules

*Documentation générée à l'aide d'une IA*

Application Python en ligne de commande permettant de gérer des locations de véhicules : clients, véhicules, réservations et tarification.

## Arborescence du projet

```
Evaluation/
├── main.py                     # Point d'entrée de l'application
├── ui.py                       # Interface utilisateur (CLI)
├── data_manager.py             # Couche de persistance (lecture/écriture JSON)
├── models/                     # Package des modèles de données
│   ├── __init__.py
│   ├── base_model.py           # Classe de base Serializable
│   ├── client.py               # Modèle Client
│   ├── vehicule.py             # Modèle Vehicule
│   ├── reservation.py          # Modèle Reservation
│   └── tarifs.py               # Enum ForfaitKM + TarifsManager
├── enonce/                     # Données JSON
│   ├── clients.json
│   ├── vehicules.json
│   └── reservations.json
├── pyproject.toml
└── .python-version
```

## Prérequis

- **Python 3.13** (indiqué dans `.python-version`)
- Aucune dépendance externe (bibliothèque standard uniquement)

## Lancer le projet

```bash
# Se placer dans le répertoire du projet
cd chemin/vers/Evaluation

# Exécuter l'application
python main.py
```

Au lancement, l'application charge les données depuis les fichiers JSON du dossier `enonce/`, puis affiche un menu interactif :

```
1. Afficher les clients
2. Afficher les véhicules
3. Créer une réservation
4. Afficher la grille tarifaire
5. Afficher toutes les réservations
6. Afficher les réservations d'un client
7. Quitter
```

## Modules

### `main.py` — Point d'entrée

Orchestre l'application : charge les données au démarrage, affiche le menu principal et délègue chaque action aux modules `ui` et `data_manager`.

### `ui.py` — Interface utilisateur

Gère tout ce qui concerne l'affichage en terminal et la saisie utilisateur :

- Affichage du menu, des clients, des véhicules, des réservations et de la grille tarifaire.
- Validation des entrées : choix de menu (1–7), identifiants client/véhicule, dates au format `AAAA-MM-JJ`, forfait kilométrique.
- Processus guidé de création d'une réservation avec récapitulatif et confirmation.

### `data_manager.py` — Persistance des données

Lecture et écriture des fichiers JSON (encodage UTF-8, indentation 4 espaces) :

| Fonction | Description |
|----------|-------------|
| `charger_clients(path)` | Charge la liste des clients depuis un fichier JSON |
| `charger_vehicules(path)` | Charge la liste des véhicules depuis un fichier JSON |
| `charger_reservations(path)` | Charge la liste des réservations depuis un fichier JSON |
| `sauvegarder_reservation(reservation, path)` | Ajoute une réservation au fichier JSON existant |
| `generer_id_reservation(reservations)` | Génère le prochain identifiant de réservation (format `R0001`) |
| `filtrer_reservations_par_client(id_client, path)` | Retourne les réservations d'un client donné |

### `models/` — Modèles de données

Package contenant les classes métier du projet, toutes basées sur des `dataclass` Python.

## Classes

### `Serializable` (`models/base_model.py`)

Classe de base fournissant la sérialisation dictionnaire ↔ objet :

| Méthode | Description |
|---------|-------------|
| `to_dict()` | Convertit l'objet en dictionnaire |
| `from_dict(data)` | Crée une instance à partir d'un dictionnaire *(classmethod)* |

---

### `Client` (`models/client.py`)

Représente un client du système de location. Hérite de `Serializable`. Dataclass gelée (`frozen=True`).

| Attribut | Type | Description |
|----------|------|-------------|
| `id_client` | `str` | Identifiant unique (ex. `C001`) |
| `nom` | `str` | Nom de famille |
| `prenom` | `str` | Prénom |
| `mail` | `str` | Adresse électronique |
| `telephone` | `str` | Numéro de téléphone |
| `adresse` | `str` | Adresse postale |

---

### `Vehicule` (`models/vehicule.py`)

Représente un véhicule disponible à la location. Hérite de `Serializable`. Dataclass gelée (`frozen=True`).

| Attribut | Type | Description |
|----------|------|-------------|
| `id_vehicule` | `str` | Identifiant unique (ex. `V001`) |
| `marque` | `str` | Marque du véhicule |
| `modele` | `str` | Modèle du véhicule |
| `cylindree` | `int` | Cylindrée du moteur (4, 5 ou 6) |
| `kilometrage_actuel` | `float` | Kilométrage actuel en km |
| `date_mise_en_circulation` | `str` | Date au format `AAAA-MM-JJ` |

---

### `ForfaitKM` (`models/tarifs.py`)

Énumération des forfaits kilométriques disponibles :

| Valeur | Signification |
|--------|---------------|
| `F100` | 100 km/jour |
| `F200` | 200 km/jour |
| `F300` | 300 km/jour |
| `F300_PLUS` | +300 km/jour (illimité) |

---

### `TarifsManager` (`models/tarifs.py`)

Gère la grille tarifaire selon la cylindrée du véhicule et le forfait kilométrique choisi.

#### Grille tarifaire

| Cylindrée | Forfait | Coût/jour | Prix km supplémentaire |
|-----------|---------|-----------|------------------------|
| 4 cyl. | 100 km | 35,00 € | 0,25 €/km |
| 4 cyl. | 200 km | 50,00 € | 0,20 €/km |
| 4 cyl. | 300 km | 65,00 € | 0,15 €/km |
| 4 cyl. | +300 km | 80,00 € | 0,10 €/km |
| 5 cyl. | 100 km | 45,00 € | 0,30 €/km |
| 5 cyl. | 200 km | 60,00 € | 0,25 €/km |
| 5 cyl. | 300 km | 75,00 € | 0,20 €/km |
| 5 cyl. | +300 km | 95,00 € | 0,15 €/km |
| 6 cyl. | 100 km | 60,00 € | 0,40 €/km |
| 6 cyl. | 200 km | 80,00 € | 0,35 €/km |
| 6 cyl. | 300 km | 100,00 € | 0,30 €/km |
| 6 cyl. | +300 km | 120,00 € | 0,25 €/km |

| Méthode | Description |
|---------|-------------|
| `obtenir_tarif(cylindree, forfait)` | Retourne `(coût_journalier, prix_km_supp)` pour une cylindrée et un forfait donnés |
| `afficher_grille()` | Affiche la grille tarifaire complète dans le terminal |

---

### `Reservation` (`models/reservation.py`)

Représente une réservation de location. Hérite de `Serializable`.

| Attribut | Type | Description |
|----------|------|-------------|
| `id_reservation` | `str` | Identifiant unique (ex. `R0001`) |
| `id_client` | `str` | Identifiant du client |
| `id_vehicule` | `str` | Identifiant du véhicule |
| `date_depart` | `str` | Date de départ (`AAAA-MM-JJ`) |
| `date_retour` | `str` | Date de retour (`AAAA-MM-JJ`) |
| `forfait_km` | `ForfaitKM` | Forfait kilométrique choisi |
| `cout_journalier` | `float` | Coût journalier en euros |
| `prix_km_supp` | `float` | Prix par km supplémentaire |
| `cout_estime` | `float` | Coût total estimé (calculé automatiquement) |

Le coût estimé est calculé automatiquement à l'instanciation via `__post_init__` :

```
coût estimé = coût journalier × nombre de jours
```

## Fonctionnement général

```
Démarrage (main.py)
       │
       ▼
Chargement des données JSON
  (clients, véhicules, réservations)
       │
       ▼
  ┌─────────────────────────────────┐
  │        Menu principal           │
  │  1. Clients    4. Tarifs        │
  │  2. Véhicules  5. Réservations  │
  │  3. Réserver   6. Par client    │
  │                7. Quitter       │
  └────────────┬────────────────────┘
               │
       ┌───────┼───────┐
       ▼       ▼       ▼
   Affichage  Création  Filtrage
   (lecture)  réserv.   par client
              │
              ▼
        Saisie guidée
        (client, véhicule,
         dates, forfait)
              │
              ▼
        Calcul du tarif
        (TarifsManager)
              │
              ▼
        Confirmation
              │
        ┌─────┴─────┐
        ▼            ▼
   Sauvegarde    Annulation
   (JSON)
```
