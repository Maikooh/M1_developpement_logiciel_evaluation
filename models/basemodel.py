"""Description. 

Ce fichier contient les classes d'héritage pour les méthodes communes."""

from dataclasses import asdict


class Serializable:
    """Classe de base pour la sérialisation dict <-> objet."""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
