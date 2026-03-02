from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List
from ex0.Card import Card


class StrategyAction(Enum):
    """
    Keys used for strategy strategy actions.
    """
    CARDS_PLAYED = "cards_played"
    MANA_USED = "mana_used"
    TARGETS_ATTACKED = "targets_attacked"
    DAMAGE_DEALT = "damage_dealt"


class GameStrategy(ABC):
    """
    Abstract strategy interface defining turn decision logic.
    """

    @abstractmethod
    def execute_turn(self, hand: List[Card], battlefield: List[Card]) -> Dict:
        """
        Execute a full turn using the strategy.

        :param hand: Cards in hand
        :param battlefield: Cards already in play
        :return: Dictionary describing the turn execution
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Return the strategy name.

        :return: Strategy identifier
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Card]) -> List:
        """
        Order targets based on strategy priority.

        :param available_targets: Possible targets
        :return: Ordered list of targets
        """
        pass
