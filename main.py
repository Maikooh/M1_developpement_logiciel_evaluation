from __future__ import annotations
import ui
import data_manager


def main() -> None:
    ui.nettoyer_terminal()
    print("=" * 50)
    print("Chargement des données...")
    try:
        clients = data_manager.charger_clients()
        vehicules = data_manager.charger_vehicules()
        reservations = data_manager.charger_reservations()
    except Exception as e:
        print("Erreur lors du chargement :", e)
        ui.pause()
        return

    print(f"✓ {len(clients)} client(s) chargé(s)")
    print(f"✓ {len(vehicules)} véhicule(s) chargé(s)")
    print("=" * 50)

    while True:
        ui.afficher_menu()
        choix = ui.demander_choix_menu()

        if choix == 7:
            ui.nettoyer_terminal()
            print("Merci d'avoir utilisé l'application!")
            break
        ui.nettoyer_terminal()

        try:
            if choix == 1:
                ui.afficher_clients(clients)
                ui.pause()

            elif choix == 2:
                ui.afficher_vehicules(vehicules)
                ui.pause()

            elif choix == 3:
                reservations = data_manager.charger_reservations()

                def next_id() -> str:
                    return data_manager.generer_id_reservation(reservations)

                reservation = ui.demander_reservation(clients, vehicules, next_id)

                if reservation is not None:
                    data_manager.sauvegarder_reservation(reservation)
                    print("✓ Réservation sauvegardée dans reservations.json")
                    print("✓ Réservation enregistrée avec succès !")
                ui.pause()

            elif choix == 4:
                from models.tarifs import TarifsManager

                TarifsManager.afficher_grille()
                ui.pause()

            elif choix == 5:
                reservations = data_manager.charger_reservations()
                ui.afficher_reservations(reservations)
                ui.pause()

            elif choix == 6:
                reservations = data_manager.charger_reservations()
                id_client = input("ID du client à rechercher : ").strip()
                ui.afficher_reservations_client(reservations, id_client)
                ui.pause()

        except Exception as e:
            print("Erreur :", e)
            ui.pause()
        ui.nettoyer_terminal()


if __name__ == "__main__":
    main()
