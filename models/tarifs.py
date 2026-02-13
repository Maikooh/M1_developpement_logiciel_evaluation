from enum import Enum


class ForfaitKM(Enum):
    """
    Enumération des forfaits kilométriques.
    """

    F100 = 100
    F200 = 200
    F300 = 300
    F300_PLUS = 301  # +300

    def __str__(self) -> str:
        if self == ForfaitKM.F300_PLUS:
            return "+300"
        return str(self.value)


class TarifsManager:
    TARIFS = {
        4: {
            ForfaitKM.F100: (35.00, 0.25),
            ForfaitKM.F200: (50.00, 0.20),
            ForfaitKM.F300: (65.00, 0.15),
            ForfaitKM.F300_PLUS: (80.00, 0.10),
        },
        5: {
            ForfaitKM.F100: (45.00, 0.30),
            ForfaitKM.F200: (60.00, 0.25),
            ForfaitKM.F300: (75.00, 0.20),
            ForfaitKM.F300_PLUS: (95.00, 0.15),
        },
        6: {
            ForfaitKM.F100: (60.00, 0.40),
            ForfaitKM.F200: (80.00, 0.35),
            ForfaitKM.F300: (100.00, 0.30),
            ForfaitKM.F300_PLUS: (120.00, 0.25),
        },
    }

    @classmethod
    def obtenir_tarif(cls, cylindree: int, forfait: ForfaitKM) -> tuple[float, float]:
        if cylindree not in cls.TARIFS:
            raise ValueError(
                f"Cylindrée invalide : {cylindree} (attendu 4, 5 ou 6)"
            )

        if forfait not in cls.TARIFS[cylindree]:
            raise ValueError(
                f"Forfait invalide : {forfait}"
            )

        return cls.TARIFS[cylindree][forfait]

    @classmethod
    def afficher_grille(cls) -> None:

        print(50*"=" )
        print("GRILLE TARIFAIRE".center(70))
        print(50* "=")
        print(
            f"{'Cylindrée':<12}"
            f"{'Forfait':<10}"
            f"{'Coût/jour':<12}"
            f"{'Prix km supp.'}"
        )
        print("-" * 70)

        for cylindree, forfaits in cls.TARIFS.items():
            for forfait, (cout_jour, prix_km) in forfaits.items():

                cyl_txt = f"{cylindree} cylindres"

                print(
                    f"{cyl_txt:<12}"
                    f"{str(forfait):<10}"
                    f"{cout_jour:<12.2f}€"
                    f"{prix_km:.2f}€/km"
                )

            print(50 * "-" )

