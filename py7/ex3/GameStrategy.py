#!/usr/bin/env python3

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List


class StrategyResult(Enum):
    """
    Keys used in strategy execution results.
    """
    STRATEGY = "strategy"
    ACTIONS = "actions"


class GameStrategy(ABC):
    """
    Abstract strategy interface defining turn decision logic.
    """

    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
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
    def prioritize_targets(self, available_targets: List) -> List:
        """
        Order targets based on strategy priority.

        :param available_targets: Possible targets
        :return: Ordered list of targets
        """
        pass
