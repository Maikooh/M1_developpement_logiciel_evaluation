from __future__ import annotations
import json
from pathlib import Path
from typing import Any, List
from models.client import Client
from models.vehicule import Vehicule
from models.reservation import Reservation

DATA_DIR = Path("./enonce")
CLIENTS_FILE = DATA_DIR / "clients.json"
VEHICULES_FILE = DATA_DIR / "vehicules.json"
RESERVATIONS_FILE = DATA_DIR / "reservations.json"


def _lire_json(path: Path) -> Any:
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON invalide dans {path} : {e}") from e
    except OSError as e:
        raise OSError(f"Erreur de lecture du fichier {path} : {e}") from e


def _ecrire_json(path: Path, data: Any) -> None:
    try:
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except OSError as e:
        raise OSError(f"Erreur d'écriture du fichier {path} : {e}") from e


def charger_clients(path: Path = CLIENTS_FILE) -> List[Client]:
    raw = _lire_json(path)
    if not isinstance(raw, list):
        raise ValueError(f"Format inattendu dans {path} : attendu une liste")
    return [Client.from_dict(item) for item in raw]


def charger_vehicules(path: Path = VEHICULES_FILE) -> List[Vehicule]:
    raw = _lire_json(path)
    if not isinstance(raw, list):
        raise ValueError(f"Format inattendu dans {path} : attendu une liste")
    return [Vehicule.from_dict(item) for item in raw]


def charger_reservations(path: Path = RESERVATIONS_FILE) -> List[Reservation]:
    raw = _lire_json(path)
    if raw == []:
        return []
    if not isinstance(raw, list):
        raise ValueError(f"Format inattendu dans {path} : attendu une liste")
    return [Reservation.from_dict(item) for item in raw]


def generer_id_reservation(reservations: List[Reservation]) -> str:
    max_num = 0
    for r in reservations:
        rid = r.id_reservation.strip()
        if rid.startswith("R"):
            suffix = rid[1:]
            if suffix.isdigit():
                n = int(suffix)
                if n > max_num:
                    max_num = n

    return f"R{max_num + 1:04d}"


def sauvegarder_reservation(
    reservation: Reservation, path: Path = RESERVATIONS_FILE
) -> None:
    reservations = charger_reservations(path)
    reservations.append(reservation)

    raw = [r.to_dict() for r in reservations]
    _ecrire_json(path, raw)


def filtrer_reservations_par_client(
    id_client: str, path: Path = RESERVATIONS_FILE
) -> List[Reservation]:
    reservations = charger_reservations(path)
    return [r for r in reservations if r.id_client == id_client]
