#!/usr/bin/env python3

import alchemy
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion


def main():
    """
    Run the import transmutation demonstration.

    Prints examples of four different Python import styles along with the
    results of calling the imported functions.
    """
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print()

    print("Method 2 - Specific function import:")
    print("create_water():", create_water())
    print()

    print("Method 3 - Aliased import:")
    print("heal():", heal())
    print()

    print("Method 4 - Multiple imports:")
    print("create_earth():", create_earth())
    print("create_fire():", create_fire())
    print("strength_potion():", strength_potion())
    print()

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
