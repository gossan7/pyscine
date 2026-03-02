#!/usr/bin/env python3

from . import Deck, SpellCard, ArtifactCard, \
    SpellInfo

from ex0.Card import CardInfo, GameState
from ex0.CreatureCard import CreatureCard


def main() -> None:
    """
    Entry point for the Deck Builder demonstration.

    Creates a deck with different card types, displays deck statistics,
    draws and plays each card, and highlights polymorphic behavior.
    """
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")

    deck = Deck()
    game_state = {GameState.AVAILABLE_MANA.value: 10}

    deck.add_card(SpellCard(
        "Lightning Bolt",
        3,
        "Common",
        SpellInfo.DAMAGE.value
    ))

    deck.add_card(ArtifactCard(
        "Mana Crystal",
        2,
        "Rare",
        10,
        "Permanent: +1 mana per turn"
    ))

    deck.add_card(CreatureCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5
    ))

    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")

    for _ in range(3):
        card = deck.draw_card()
        card_info = card.get_card_info()
        print(
            f"Drew: {card_info[CardInfo.NAME.value]}",
            f"({card_info[CardInfo.TYPE.value]})"
        )
        print(f"Play result: {card.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
