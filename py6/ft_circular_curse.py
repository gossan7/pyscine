#!/usr/bin/env python3

from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def test_late():
    print("Testing late import technique:")
    from alchemy.grimoire.spellbook import record_spell
    print("record_spell(\"Lightning\", \"air\"): "
          f"{record_spell("Lightning", "air")}")
    print()


def main():
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print("validate_ingredients(\"fire air\"): "
          f"{validate_ingredients("fire air")}")
    print("validate_ingredients(\"dragon scales\"): "
          f"{validate_ingredients("dragon scales")}")
    print()

    print("Testing spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"): "
          f"{record_spell("Fireball", "fire air")}")
    print("record_spell(\"Dark Magic\", \"shadow\"): "
          f"{record_spell("Dark Magic", "shadow")}")
    print()

    test_late()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
