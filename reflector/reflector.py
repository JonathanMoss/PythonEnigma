#!/usr/bin/python3
from enum import Enum


class ReflectorWiring(Enum):

    B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    C = "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    B_THIN = "ENKQAUYWJICOPBLMDXZVFTHRGS"
    C_THIN = "RDOBJNTKVEHMLFCWZAXGYIPSUQ"


class Reflector:

    def __init__(self, reflector_version: ReflectorWiring):
        self._reflector_version = reflector_version
        self._reflector = self._initialise_reflector()

    def _initialise_reflector(self) -> dict:

        rf = {}
        x = 65
        for pair in list(str(self._reflector_version.value)):
            rf.update({
                chr(x): pair
            })
            x += 1

        return rf

    def return_letter(self, incoming_letter: str) -> str:

        return self._reflector.get(incoming_letter, None)


if __name__ == "__main__":

    rf = Reflector(ReflectorWiring.C)
    print(rf.return_letter('A'))
