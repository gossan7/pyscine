from enum import Enum
from typing import Dict, List
from random import shuffle
from ex0.Card import Card, CardInfo


class DeckError(Exception):
    """
    Exception raised for errors related to deck operations.
    """

    def __init__(self, msg: str):
        """
        Initialize a DeckError with a descriptive message.

        :param msg: Description of the deck-related error
        """
        super().__init__(f"DeckError: {msg}")


class DeckInfo(Enum):
    """
    Enumeration of keys used for storing deck statistics.
    """
    TOTAL_CARDS = "total_cards"
    AVG_COST = "avg_cost"


class Deck:
    """
    Deck management class responsible for storing, organizing, and
    manipulating a collection of cards.

    The deck supports adding, removing, shuffling, drawing cards, and
    reporting aggregated statistics.
    """

    def __init__(self) -> None:
        """
        Initialize an empty deck with no cards and default statistics.
        """
        self.cards: List[Card] = []
        self.stats: Dict[str, float] = {
            DeckInfo.TOTAL_CARDS.value: 0,
            DeckInfo.AVG_COST.value: 0
        }

    def add_card(self, card: Card) -> None:
        """
        Add a card to the deck and update deck statistics.

        :param card: Card instance to be added to the deck
        """
        self.cards.append(card)
        card_info = card.get_card_info()

        type_key = card_info[CardInfo.TYPE.value].lower() + "s"
        self.stats.setdefault(type_key, 0)
        self.stats[type_key] += 1

        self.stats[DeckInfo.AVG_COST.value] *= \
            self.stats[DeckInfo.TOTAL_CARDS.value]

        self.stats[DeckInfo.AVG_COST.value] += \
            card_info[CardInfo.COST.value]

        self.stats[DeckInfo.TOTAL_CARDS.value] += 1

        self.stats[DeckInfo.AVG_COST.value] /= \
            self.stats[DeckInfo.TOTAL_CARDS.value]

    def remove_card(self, card_name: str) -> None:
        """
        Remove a card from the deck by its name and update statistics.

        :param card_name: Name of the card to remove
        :raises DeckError: If the card is not found in the deck
        """
        found = False

        for i, card in enumerate(self.cards):
            card_info = card.get_card_info()

            if card_info[CardInfo.NAME.value] == card_name:

                self.stats[DeckInfo.AVG_COST.value] *= \
                    self.stats[DeckInfo.TOTAL_CARDS.value]

                self.stats[DeckInfo.AVG_COST.value] -= \
                    card_info[CardInfo.COST.value]

                self.stats[DeckInfo.TOTAL_CARDS.value] -= 1

                if self.stats[DeckInfo.TOTAL_CARDS.value]:

                    self.stats[DeckInfo.AVG_COST.value] /= \
                        self.stats[DeckInfo.TOTAL_CARDS.value]

                self.cards.pop(i)
                found = True
                break

        if not found:
            raise DeckError(f"No such card in deck: {card_name}")

    def shuffle(self) -> None:
        """
        Shuffle the deck randomly.
        """
        shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        Draw and remove the top card from the deck.

        :raises DeckError: If the deck is empty
        :return: The drawn Card instance
        """
        if not self.cards:
            raise DeckError("No card in deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict[str, float]:
        """
        Retrieve aggregated statistics about the deck.

        :return: Dictionary containing deck statistics
        """
        return self.stats
