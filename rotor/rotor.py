#!/usr/bin/python3
import collections
import re


class RotorConfig:

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

    def set_position(self, position: int):
        """ Set the rotor position, as per the key setting in the msg """

        self._current_index = position

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
                    index + 1: value
                })

    def return_letter(self, letter: str) -> tuple:

        # Current rotor dial position
        print(self._current_ring_letter)
        print(self._current_index)
        print(self._rotor_wiring)


        # Convert letter to rotor index
        input_letter = ord(str(letter).upper()) - 64
        print(input_letter)

        if self._current_ring_letter in self._turnover:
            turnover_next_dial = True
        else:
            turnover_next_dial = False

        # Advance
        self._advance_rotor()
        print(self._rotor)

        return (
            self._rotor.get(input_letter),
            turnover_next_dial
        )

    def __init__(self, rotor: str, ring_setting):

        # Get the rotor version (Walzenlage)
        self._rotor_version = str(rotor).upper()
        if self._rotor_version not in RotorConfig.SETTINGS:
            raise ValueError("Unknown Rotor Version")

        # Get the initial ring setting (Ringstellung), could be an int or char
        if re.match('[A-Z]', ring_setting):
            self._ring_setting = ord(ring_setting) - 64
            print(self._ring_setting)
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

        # Step 2: Extrapolate number of steps from A to key setting
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
                index + 1: value
            })

        self._current_index = self._get_current_index(
            chr(self._ring_setting)) + 1
        self._current_ring_letter = chr(90 - self._current_index)
        print(self._rotor)
        print(self._current_index, self._current_ring_letter)


if __name__ == "__main__":

    rt = Rotor("I", "D")
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
    print(rt.return_letter('A'))
