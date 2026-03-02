#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard, CreatureInfo
from ex2.EliteCard import EliteCard


def main() -> None:
    """
    Demonstration script for Exercise 2: Ability System.
    """
    print("=== DataDeck Ability System ===\n")

    elite = EliteCard(
        "Arcane Warrior",
        4,
        "Epic",
        attack=5,
        health=10,
        mana=8
    )

    enemy = CreatureCard(
        "Enemy",
        5,
        "Common",
        attack=5,
        health=5
    )
    enemy_info = enemy.get_card_info()

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    print("Playing Arcane Warrior (Elite Card):\n")

    print("Combat phase:")
    print("Attack result:",
          elite.attack(enemy_info))
    attack = enemy_info[CreatureInfo.ATTACK.value]
    print("Defense result:",
          elite.defend(attack))

    print("\nMagic phase:")

    enemy1 = CreatureCard(
        "Enemy1",
        5,
        "Common",
        attack=5,
        health=5
    )

    enemy2 = CreatureCard(
        "Enemy2",
        5,
        "Common",
        attack=5,
        health=5
    )

    print("Spell cast:",
          elite.cast_spell(
              "Fireball",
              [enemy1.get_card_info(), enemy2.get_card_info()])
          )

    print("Mana channel:",
          elite.channel_mana(3))

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
