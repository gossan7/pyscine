from ex0 import CreatureCard, Info, GameState


def main():
    """Demonstrate the Card Foundation architecture."""
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    game_state = {
        GameState.AVAILABLE_MANA.value: 6
    }

    fire_dragon = CreatureCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5
    )

    print("CreatureCard Info:")
    fire_dragon_infos = fire_dragon.get_card_info()
    print(fire_dragon_infos)
    print()

    print(
        f"Playing {fire_dragon_infos[Info.NAME.value]}",
        f"with {game_state[GameState.AVAILABLE_MANA.value]} mana available:"
    )
    print(
        "Playable:",
        fire_dragon.is_playable(game_state[GameState.AVAILABLE_MANA.value])
    )
    print(f"Play result: {fire_dragon.play(game_state)}\n")

    goblin_warrior = CreatureCard(
        "Goblin Warrior",
        5,
        "Common",
        5,
        7
    )

    goblin_warrior_infos = goblin_warrior.get_card_info()

    print(
        f"{fire_dragon_infos[Info.NAME.value]} attacks",
        f"{goblin_warrior_infos[Info.NAME.value]}:"
    )

    print(
        "Attack result:",
        fire_dragon.attack_target(goblin_warrior.get_card_info(), game_state)
    )

    print(
        "Testing insufficient mana",
        f"({game_state[GameState.AVAILABLE_MANA.value]} available):"
    )

    print(
        "Playable:",
        fire_dragon.is_playable(game_state[GameState.AVAILABLE_MANA.value])
    )

    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
