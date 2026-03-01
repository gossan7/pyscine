#!/usr/bin/env python3

from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def test_late() -> None:
    print("Testing late import technique:")
    from alchemy.grimoire.spellbook import record_spell
    print("record_spell(\"Lightning\", \"air\"):",
          record_spell("Lightning", "air"))
    print()


def main():
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")

    print(
        "validate_ingredients(\"fire air\"):",
        validate_ingredients("fire air")
    )

    print(
        "validate_ingredients(\"dragon scales\"):",
        validate_ingredients("dragon scales")
    )

    print()

    print("Testing spell recording with validation:")

    print(
        "record_spell(\"Fireball\", \"fire air\"):",
        record_spell("Fireball", "fire air")
    )

    print(
        "record_spell(\"Dark Magic\", \"shadow\"):",
        record_spell("Dark Magic", "shadow")
    )

    print()

    test_late()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
