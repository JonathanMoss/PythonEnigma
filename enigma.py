#!/usr/bin/python3
from plugboard.plugboard import Plugboard
from reflector.reflector import Reflector, ReflectorWiring
from rotor.rotor import Rotor

# TODO: Get these from the command line / file
walzenlage = "V III II".split(" ")
ringstellung = list("AKK")
steckerverbindungen = "AO HI MU SN VX ZQ".split(" ")
grundstellung = list("FDV")

# Step 1 - Plugboard
pb_pairs = {}
for pair in steckerverbindungen:
    pb_pairs.update({
        pair[0]: pair[1]
    })
plugboard = Plugboard(pb_pairs)

# Step 2 - Reflector
reflector = Reflector(ReflectorWiring.C)

# Step 3 - Rotors
right_rotor = Rotor(
    walzenlage[2],
    ringstellung[2],
    grundstellung[2]
)

middle_rotor = Rotor(
    walzenlage[1],
    ringstellung[1],
    grundstellung[1]
)
#
# left_rotor = Rotor(
#     walzenlage[0],
#     ringstellung[0],
#     grundstellung[0]
# )

# while True:
#     input("Enter a letter")
