from dataclasses import dataclass
from .base_model import Serializable


@dataclass(frozen=True)
class Vehicule(Serializable):
    id_vehicule: str
    marque: str
    modele: str
    cylindree: int
    kilometrage_actuel: float
    date_mise_en_circulation: str

    def __str__(self) -> str:
        return (
            f"{self.id_vehicule} - {self.marque} {self.modele} "
            f"({self.cylindree} cyl., {self.kilometrage_actuel} km)"
        )
