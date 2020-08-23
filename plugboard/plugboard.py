#!/usr/bin/python3

MIN_STECKER_PAIR = 10
MAX_STECKER_PAIR = 13


class Plugboard:

    def __init__(self, stecker_pairs: dict):

        self._steckerbrett = self._initialise_plugboard()

        if not isinstance(stecker_pairs, dict):
            raise TypeError("Plugboard pairs incorrectly defined")

        if len(stecker_pairs) < MIN_STECKER_PAIR:
            raise ValueError("Not enough plugboard pairs defined")

        if len(stecker_pairs) > MAX_STECKER_PAIR:
            raise ValueError("Too many plugboard pairs defined")

        print(self._steckerbrett)

        self._process_stecker_pairs(stecker_pairs)

        print(self._steckerbrett)

    def return_letter(self, letter: str) -> str:

        return self._steckerbrett.get(letter, None)

    def _process_stecker_pairs(self, stecker_pairs):

        processed_plugs = []

        for key, value in stecker_pairs.items():
            if key not in self._steckerbrett:
                raise KeyError("Incorrect plug defined, not A-Z")

            if not len(value) == 1:
                raise ValueError("Error in plug pair definition, not A-Z")

            if ord(value) < 65 or ord(value) > 90:
                raise ValueError("Error in plug pair definition, not A-Z")

            if key in processed_plugs or value in processed_plugs:
                raise ValueError("Conflicting pair definition")

            self._steckerbrett[key] = value
            processed_plugs.append(key)
            self._steckerbrett[value] = key
            processed_plugs.append(value)

    def _initialise_plugboard(self) -> dict:

        pb = {}
        x = 65  # A
        end = 91  # Z + 1

        while x < end:
            pb.update({
                chr(x): chr(x)
            })
            x += 1

        return pb


if __name__ == "__main__":
    pb = Plugboard({'A': 'B', 'C': 'D'})
    print(pb.return_letter('A'))
    print(pb.return_letter('B'))
