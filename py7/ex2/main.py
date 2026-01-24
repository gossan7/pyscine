#!/usr/bin/env python3

from .EliteCard import EliteCard


def main():
    """
    Demonstration script for Exercise 2: Ability System.
    """
    print("=== DataDeck Ability System ===\n")

    elite = EliteCard(
        "Arcane Warrior",
        4,
        "Epic",
        5,
        10,
        5
    )

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    print("Playing Arcane Warrior (Elite Card):\n")

    print("Combat phase:")
    print("Attack result:",
          elite.attack("Enemy"))
    print("Defense result:",
          elite.defend(5))

    print("\nMagic phase:")
    print("Spell cast:",
          elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:",
          elite.channel_mana(3))

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
