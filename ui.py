from __future__ import annotations
import os
from datetime import date
from models.tarifs import TarifsManager, ForfaitKM
from models.reservation import Reservation

def nettoyer_terminal() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def pause(message: str = "Appuyez sur Entrée pour continuer") -> None:
    input(message)

def afficher_menu() -> None:
    print("=" * 50)
    print("SYSTÈME DE LOCATION DE VÉHICULES".center(50))
    print("=" * 50)
    print("1. Afficher les clients")
    print("2. Afficher les véhicules")
    print("3. Créer une réservation")
    print("4. Afficher la grille tarifaire")
    print("5. Afficher toutes les réservations")
    print("6. Afficher les réservations d'un client")
    print("7. Quitter")
    print("=" * 50)

def demander_choix_menu() -> int:
    while True:
        choix = input("Votre choix : ").strip()
        if choix.isdigit():
            n = int(choix)
            if 1 <= n <= 7:
                return n
        print("Choix invalide. Entrez un nombre entre 1 et 7.")

def afficher_clients(clients) -> None:
    print("=" * 50)
    print("LISTE DES CLIENTS".center(50))
    print("=" * 50)
    for c in clients:
        print(str(c))
    print("=" * 50)

def afficher_vehicules(vehicules) -> None:
    print("=" * 50)
    print("LISTE DES VÉHICULES".center(50))
    print("=" * 50)
    for v in vehicules:
        print(str(v))
    print("=" * 50)

def afficher_reservations(reservations) -> None:
    print("=" * 50)
    print("LISTE DES RÉSERVATIONS".center(50))
    print("=" * 50)

    if not reservations:
        print("Aucune réservation.")
        print("=" * 50)
        return

    for r in reservations:
        print(
            f"{r.id_reservation} | Client: {r.id_client} | Véhicule: {r.id_vehicule} | "
            f"{r.date_depart} -> {r.date_retour} | Forfait: {r.forfait_km} km | "
            f"Coût estimé: {r.cout_estime:.2f}€"
        )

    print("=" * 50)


def afficher_reservations_client(reservations, id_client: str) -> None:
    print("=" * 50)
    print(f"RÉSERVATIONS DU CLIENT {id_client}".center(50))
    print("=" * 50)

    res = [r for r in reservations if r.id_client == id_client]

    if not res:
        print("Aucune réservation pour ce client.")
        print("=" * 50)
        return

    for r in res:
        print(
            f"{r.id_reservation} | Véhicule: {r.id_vehicule} | "
            f"{r.date_depart} ➔ {r.date_retour} | Forfait: {r.forfait_km} km | "
            f"Coût estimé: {r.cout_estime:.2f}€"
        )

    print("=" * 50)

def demander_id_client(clients) -> str:
    ids = {c.id_client for c in clients}
    while True:
        cid = input("ID du client : ").strip()
        if cid in ids:
            return cid
        print("ID client introuvable. Réessayez.")

def demander_id_vehicule(vehicules) -> str:
    ids = {v.id_vehicule for v in vehicules}
    while True:
        vid = input("ID du véhicule : ").strip()
        if vid in ids:
            return vid
        print("ID véhicule introuvable. Réessayez.")

def demander_date(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        try:
            date.fromisoformat(s)  
            return s
        except ValueError:
            print("Date invalide. Format attendu : AAAA-MM-JJ.")

def demander_forfait_km() -> ForfaitKM:
    print("Forfaits disponibles : 100, 200, 300, +300")
    mapping = {
        "100": ForfaitKM.F100,
        "200": ForfaitKM.F200,
        "300": ForfaitKM.F300,
        "+300": ForfaitKM.F300_PLUS,
    }

    while True:
        s = input("Forfait kilométrique : ").strip()
        if s in mapping:
            return mapping[s]
        print("Forfait invalide. Entrez 100, 200, 300 ou +300.")


def demander_reservation(clients, vehicules, generer_id_cb):

    print("=" * 50)
    print("CRÉER UNE NOUVELLE RÉSERVATION".center(50))
    print("=" * 50)
    print("Clients disponibles :")
    for c in clients:
        print(f"- {c}")

    id_client = demander_id_client(clients)

    print("Véhicules disponibles :")
    for v in vehicules:
        print(f"- {v}")

    id_vehicule = demander_id_vehicule(vehicules)

    date_depart = demander_date("Date de départ (AAAA-MM-JJ) : ")
    date_retour = demander_date("Date de retour (AAAA-MM-JJ) : ")

    forfait = demander_forfait_km()
    vehicule_obj = next(v for v in vehicules if v.id_vehicule == id_vehicule)
    cout_jour, prix_km = TarifsManager.obtenir_tarif(vehicule_obj.cylindree, forfait)

    reservation = Reservation(
        id_reservation=generer_id_cb(),
        id_client=id_client,
        id_vehicule=id_vehicule,
        date_depart=date_depart,
        date_retour=date_retour,
        forfait_km=forfait,
        cout_journalier=cout_jour,
        prix_km_supp=prix_km,
    )

    print("=" * 50)
    print("RÉCAPITULATIF DE LA RÉSERVATION".center(50))
    print("=" * 50)
    print(reservation)
    print("=" * 50)

    confirm = input("Sauvegarder cette réservation ? (o/n) : ").strip().lower()
    if confirm == "o":
        return reservation

    print("Réservation annulée.")
    return None
