#!/usr/bin/env python3

from . import Deck, CreatureCard, SpellCard, ArtifactCard, \
              CardInfo, SpellInfo, GameState


def main():
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
        print(f"Drew: {card_info[CardInfo.NAME.value]}",
              f"({card_info[CardInfo.TYPE.value]})")
        print(f"Play result: {card.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
