#!/usr/bin/env python3

from ex0.Card import CardInfo
from ex4.TournamentCard import TournamentCard, TournamentInfo
from ex4.TournamentPlatform import TournamentPlatform


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
        info = card.info
        card_id = info[TournamentInfo.CARD_ID.value]
        wins = info[TournamentInfo.WINS.value]
        losses = info[TournamentInfo.LOSSES.value]
        print(f"{card.info[CardInfo.NAME.value]} (ID: {card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {info[TournamentInfo.RATING.value]}")
        print(f"- Record: {wins}-{losses}\n")

    print("Creating tournament match...")

    result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", result)
    print()

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard):
        info = card.info
        wins = info[TournamentInfo.WINS.value]
        losses = info[TournamentInfo.LOSSES.value]
        name = card.info[CardInfo.NAME.value]
        rating = info[TournamentInfo.RATING.value]

        print(
            f"{i + 1}. {name} - Rating: {rating} "
            f"({wins}-{losses})"
        )

    print()

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
