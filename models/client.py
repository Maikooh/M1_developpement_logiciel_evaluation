from dataclasses import dataclass
from .base_model import Serializable


@dataclass(frozen=True)
class Client(Serializable):
    id_client: str
    nom: str
    prenom: str
    mail: str
    telephone: str
    adresse: str

    def __str__(self) -> str:
        return f"{self.id_client} - {self.prenom} {self.nom} ({self.mail})"


