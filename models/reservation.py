from dataclasses import dataclass
from datetime import date
from .base_model import Serializable
from .tarifs import ForfaitKM

@dataclass
class Reservation(Serializable):
    id_reservation: str
    id_client: str
    id_vehicule: str
    date_depart: str
    date_retour: str
    forfait_km: ForfaitKM
    cout_journalier: float
    prix_km_supp: float
    cout_estime: float = 0.0
    def __post_init__(self):
        self.cout_estime = self._calculer_cout_estime()
    def _calculer_cout_estime(self) -> float:

        d1 = date.fromisoformat(self.date_depart)
        d2 = date.fromisoformat(self.date_retour)

        nb_jours = (d2 - d1).days

        if nb_jours < 1:
            nb_jours = 1

        return self.cout_journalier * nb_jours
    def to_dict(self) -> dict:
        """
        convertir enum -> str
        """
        data = super().to_dict()
        data["forfait_km"] = str(self.forfait_km)
        return data

    @classmethod
    def from_dict(cls, data: dict):
        """
        convertir : str -> Enum.
        """

        mapping = {
            "100": ForfaitKM.F100,
            "200": ForfaitKM.F200,
            "300": ForfaitKM.F300,
            "+300": ForfaitKM.F300_PLUS,
        }

        d = dict(data)
        fk = str(d["forfait_km"])

        if fk not in mapping:
            raise ValueError(f"Forfait invalide : {fk}")

        d["forfait_km"] = mapping[fk]
        d.pop("cout_estime", None)

        return cls(**d)