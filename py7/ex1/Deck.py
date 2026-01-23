#!/usr/bin/env python3

from . import Card, CardInfo
from enum import Enum
from typing import Dict, List
from random import shuffle


class DeckError(Exception):
    def __init__(self, msg: str):
        super().__init__(f"DeckError: {msg}")


class DeckInfo(Enum):
    TOTAL_CARDS = "total_cards"
    AVG_COST = "avg_cost"


class Deck:
    def __init__(self):
        self.cards: List[Card] = []
        self.stats: Dict[str, int] = {
            DeckInfo.TOTAL_CARDS.value: 0,
            DeckInfo.AVG_COST.value: 0
        }

    def add_card(self, card: Card):
        self.cards.append(card)
        card_info = card.get_card_info()
        type_key = card_info[CardInfo.TYPE.value].lower() + "s"
        self.stats.setdefault(type_key, 0)
        self.stats[type_key] += 1
        self.stats[DeckInfo.AVG_COST.value] \
            *= self.stats[DeckInfo.TOTAL_CARDS.value]
        self.stats[DeckInfo.AVG_COST.value] += card_info[CardInfo.COST.value]
        self.stats[DeckInfo.TOTAL_CARDS.value] += 1
        self.stats[DeckInfo.AVG_COST.value] \
            /= self.stats[DeckInfo.TOTAL_CARDS.value]

    def remove_card(self, card_name: str):
        found = False
        for i, card in enumerate(self.cards):
            card_info = card.get_card_info()
            if card_info[CardInfo.NAME.value] == card_name:
                self.stats[DeckInfo.AVG_COST.value] \
                    *= self.stats[DeckInfo.TOTAL_CARDS.value]
                self.stats[DeckInfo.AVG_COST.value] \
                    -= card_info[CardInfo.COST.value]
                self.stats[DeckInfo.TOTAL_CARDS.value] -= 1
                if self.stats[DeckInfo.TOTAL_CARDS.value]:
                    self.stats[DeckInfo.AVG_COST.value] \
                        /= self.stats[DeckInfo.TOTAL_CARDS.value]
                self.cards.pop(i)
                found = True
                break
        if not found:
            raise DeckError(f"No such card in deck: {card_name}")

    def shuffle(self):
        shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            raise DeckError("No card in deck")
        return self.cards.pop(0)

    def get_deck_stats(self):
        return self.stats
