# Documentation des Classes - Système de Gestion de Locations de Véhicules

*Documentation générée à l'aide  d'une IA*

## Classe Client

Représente un client du système de location de véhicules.

| Attribut | Type | Description |
|----------|------|-------------|
| `id_client` | str | Identifiant unique du client |
| `nom` | str | Nom de famille du client |
| `prenom` | str | Prénom du client |
| `mail` | str | Adresse électronique du client |
| `telephone` | str | Numéro de téléphone du client |
| `adresse` | str | Adresse postale du client |

## Classe Vehicule

Représente un véhicule disponible à la location.

| Attribut | Type | Description |
|----------|------|-------------|
| `id_vehicule` | str | Identifiant unique du véhicule |
| `marque` | str | Marque fabricant du véhicule |
| `modele` | str | Modèle du véhicule |
| `cylindre` | int | Cylindrée du moteur (4, 5 ou 6) |
| `kilometrage_actuel` | int | Kilométrage actuel du véhicule |
| `date_mise_en_circulation` | date | Date de mise en circulation du véhicule |

## Classe Reservation

Représente une réservation de location de véhicule par un client.

| Attribut | Type | Description |
|----------|------|-------------|
| `id_reservation` | str | Identifiant unique de la réservation |
| `id_client` | str | Identifiant du client effectuant la réservation |
| `id_vehicule` | str | Identifiant du véhicule réservé |
| `date_depart` | date | Date de départ (format AAAA-MM-JJ) |
| `date_retour` | date | Date de retour (format AAAA-MM-JJ) |
| `forfait_km` | int | Forfait kilométrique (100, 200 ou +300 km/jour) |
| `cout_journalier` | float | Coût journalier de la location |
| `prix_km_supp` | float | Prix par kilomètre supplémentaire au-delà du forfait |
| `cout_estime` | float | Coût total estimé de la réservation |