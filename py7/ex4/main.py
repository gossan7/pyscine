#!/usr/bin/env python3

from . import TournamentPlatform, TournamentCard


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    dragon = TournamentCard(
        "dragon_001", "Fire Dragon", 5, "Legendary", 6, 10, 1200
    )
    wizard = TournamentCard(
        "wizard_001", "Ice Wizard", 4, "Rare", 4, 8, 1150
    )

    platform.register_card(dragon)
    platform.register_card(wizard)

    for card in (dragon, wizard):
        info = card.get_rank_info()
        print(f"{card.info['name']} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {info['rating']}")
        print(f"- Record: {info['wins']}-{info['losses']}\n")

    print("Creating tournament match...")

    result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", result)
    print()

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        print(
            f"{i}. {card.info['name']} - Rating: {card.rating} "
            f"({card.wins}-{card.losses})"
        )
    print()

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
