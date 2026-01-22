#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class CardInfo(Enum):
    """Keys used to describe card information."""
    NAME = "name"
    COST = "cost"
    RARITY = "rarity"
    TYPE = "type"
    ATTACK = "attack"
    HEALTH = "health"


class GameState(Enum):
    """Keys used in the game state dictionary."""
    AVAILABLE_MANA = "available_mana"


class Play(Enum):
    """Keys used in the result of playing a card."""
    CARD_PLAYED = "card_played"
    MANA_USED = "mana_used"
    EFFECT = "effect"


class Attack(Enum):
    """Keys used in combat resolution results."""
    ATTACKER = "attacker"
    TARGET = "target"
    DAMAGE_DEALT = "damage_dealt"
    COMBAT_RESOLVED = "combat_resolved"


class CardError(Exception):
    """Custom exception raised for card-related errors."""
    pass


class Card(ABC):
    """Abstract base class representing a generic card."""

    def __init__(self, name: str, cost: int, rarity: str):
        """
        Initialize common card attributes.

        :param name: Name of the card
        :param cost: Mana cost of the card
        :param rarity: Rarity of the card
        """
        self.infos = {
            CardInfo.NAME.value: name,
            CardInfo.COST.value: cost,
            CardInfo.RARITY.value: rarity
        }

    @abstractmethod
    def play(self, game_state: Dict):
        """
        Play the card using the provided game state.

        :param game_state: Current game state
        :return: Dictionary describing the result of the play
        """
        raise NotImplementedError

    def get_card_info(self) -> Dict:
        """
        Return all card information.

        :return: Dictionary containing card attributes
        """
        return self.infos

    def is_playable(self, avaliable_mana: int) -> bool:
        """
        Check whether the card can be played with the given mana.

        :param avaliable_mana: Amount of available mana
        :return: True if playable, False otherwise
        """
        return avaliable_mana >= self.infos[CardInfo.COST.value]
