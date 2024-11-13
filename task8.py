from dataclasses import dataclass


class Zapas:
    def __init__(self, domaci, hoste, doba):
        self.domaci = domaci
        self.hoste = hoste
        self.doba = doba


@dataclass
class DZapas:
    domaci : str
    hoste : str
    doba : int

    def print_doma(self):
        print(self.doba)

eufa = DZapas("Sparta", "Slavie", 93)
cl = Zapas("Liverpool", "Arsenal", 87)

print(f"{eufa}")

