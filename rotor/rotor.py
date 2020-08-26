#!/usr/bin/python3
import collections
import re


class RotorConfig:
    """ The settings for each of the 8 rotors """

    SETTINGS = {
        'I': {
            'wire': "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            'turnover': ("Q", )
        },
        'II': {
            'wire': "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            'turnover': ('E', )
        },
        'III': {
            'wire': "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            'turnover': ('V', )
        },
        'IV': {
            'wire': "ESOVPZJAYQUIRHXLNFTGKDCMWB",
            'turnover': ('J', )
        },
        'V': {
            'wire': "VZBRGITYUPSDNHLXAWMJQOFECK",
            'turnover': ('Z', )
        },
        'VI': {
            'wire': "JPGVOUMFYQBENHZRDKASXLICTW",
            'turnover': ('Z', 'M')
        },
        'VII': {
            'wire': "NZJHGRCXMYSWBOUFAIVLPEKQDT",
            'turnover': ('Z', 'M')
        },
        'VIII': {
            'wire': "FKQHTLXOCBJSPDZRAMEWNIUYGV",
            'turnover': ('Z', 'M')
        }
    }


class Rotor:

    def _advance_rotor(self, apply_to_rotor=True):

        # Advance the rotor wiring
        d = collections.deque(list(self._rotor_wiring))
        d.rotate(1)
        self._rotor_wiring = "".join(d)

        # Extrapolate to the rotor object
        if apply_to_rotor:
            self._rotor = {}
            for index, value in enumerate(list(self._rotor_wiring)):
                self._rotor.update({
                    chr(index + 65): value
                })

            if self._window_letter == "Z":
                self._window_letter = "A"
            else:
                self._window_letter = chr(ord(self._window_letter) + 1)

    def return_letter(self, letter: str) -> tuple:

        if self._window_letter in self._turnover:
            turnover_next_dial = True
        else:
            turnover_next_dial = False

        # Advance
        self._advance_rotor()

        return (
            self._rotor.get(letter),
            turnover_next_dial
        )

    def __init__(self, rotor: str, ring_setting, initial_setting):

        # Get the initial setting (Grundstellung)
        if not re.match('[A-Z]', initial_setting):
            raise ValueError('Invalid initial setting')
        else:
            self._initial_setting = str(initial_setting).upper()

        # Get the rotor version (Walzenlage)
        self._rotor_version = str(rotor).upper()
        if self._rotor_version not in RotorConfig.SETTINGS:
            raise ValueError("Unknown Rotor Version")

        # Get the initial ring setting (Ringstellung), could be an int or char
        if re.match('[A-Z]', ring_setting):
            self._ring_setting = ord(ring_setting) - 64

        else:
            if not isinstance(ring_setting, int):
                ring_setting = int(ring_setting)
            self._ring_setting = 65 + int(ring_setting) - 1

        self._rotor = {}
        self._rotor_wiring = RotorConfig.SETTINGS[self._rotor_version].get(
                    'wire'
                )

        self._turnover = RotorConfig.SETTINGS[self._rotor_version].get(
            'turnover'
        )

        self._initialise_rotor()

    def _get_current_index(self, letter: str):

        for index, value in enumerate(list(self._rotor_wiring)):
            if value == letter:
                return index

    def _initialise_rotor(self):

        # Step 1: Get the dot (A) Position
        dot_position = 0
        for index, value in enumerate(list(self._rotor_wiring)):
            if value == "A":
                dot_position = index

        # Step 2: Setup the Ringstellung
        rotor_wiring_list = list(self._rotor_wiring)
        for step in range(self._ring_setting - ord('A')):
            for index, value in enumerate(rotor_wiring_list):

                if value == "Z":
                    rotor_wiring_list[index] = "A"
                else:
                    rotor_wiring_list[index] = chr(ord(value) + 1)

                self._rotor_wiring = "".join(rotor_wiring_list)
            dot_position += 1

        # Step 3: Place the key setting at the dot position
        while not self._get_current_index(chr(self._ring_setting)) == dot_position:
            self._advance_rotor(False)

        # Step 4: Create the rotor
        for index, value in enumerate(list(self._rotor_wiring)):
            self._rotor.update({
                chr(index + 65): value
            })

        # Set the initial setting (Grundstellung)
        self._window_letter = "A"
        window_letter_num = ord(self._window_letter) - 64
        initial_setting = ord(self._initial_setting) - 64
        steps = initial_setting - window_letter_num % 26
        for step in range(steps):
            self._advance_rotor(True)


if __name__ == "__main__":

    rt = Rotor("I", "03", "Z")
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
