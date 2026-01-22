#!/usr/bin/env python3

from . import Card
from enum import Enum
from typing import Dict, List
from random import shuffle


class Types(Enum):
    


class CardInfo(Enum):
    """Keys used to describe card information."""
    NAME = "name"
    COST = "cost"
    RARITY = "rarity"
    TYPE = "type"


class SpellInfo(CardInfo):
    EFFECT_TYPE = "effect_type"


class ArtifactInfo(CardInfo):
    DURABILITY = "durability"
    EFFECT = "effect"


class DeckInfo(Enum):
    TOTAL_CARDS = "total_cards"
    CREATURES = "creatures"
    SPELLS = "spells"
    ARTIFACTS = "artifacts"
    AVG_COST = "avg_cost"


class CardError(Exception):
    """Custom exception raised for card-related errors."""
    def __init__(self, msg: str):
        super().__init__(f"CardError: {msg}")


class Deck:
    def __init__(self):
        self.cards: List[Card] = []
        self.stats: Dict[str, int] = {
            DeckInfo.TOTAL_CARDS.value: 0,
            DeckInfo.CREATURES.value: 0,
            DeckInfo.SPELLS.value: 0,
            DeckInfo.ARTIFACTS.value: 0,
            DeckInfo.AVG_COST.value: 0
        }

    def add_card(self, card: Card):
        self.cards.append(card)
        card_info = card.get_card_info()
        if card_info[CardInfo.TYPE.value] == 

    def 
