from dataclasses import dataclass

from model.pilota import Pilota


@dataclass
class Arco:
    d1: Pilota
    d2: Pilota
    peso: int

    def __hash__(self):
        return hash(self.peso)
    def __eq__(self, other):
        return self.d1 == other.d1
    def __str__(self):
        return f"{self.d1.surname} --> {self.d2.surname} ({self.peso})"