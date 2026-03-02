from abc import ABC, abstractmethod
from typing import Dict
from ex0.Card import Card


class CardFactory(ABC):
    """
    Abstract factory interface for card creation.
    """

    @abstractmethod
    def create_creature(self, name_or_power=None) -> Card:
        """
        Create a creature card.

        :param name_or_power: Optional customization
        :return: Creature card
        """
        pass

    @abstractmethod
    def create_spell(self, name_or_power=None) -> Card:
        """
        Create a spell card.

        :param name_or_power: Optional customization
        :return: Spell card
        """
        pass

    @abstractmethod
    def create_artifact(self, name_or_power=None) -> Card:
        """
        Create an artifact card.

        :param name_or_power: Optional customization
        :return: Artifact card
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict:
        """
        Create a themed deck.

        :param size: Deck size
        :return: Dictionary containing the deck
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict:
        """
        Return supported card types.

        :return: Dictionary of supported types
        """
        pass
