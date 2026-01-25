#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """
    Abstract interface defining ranking behavior for tournament entities.
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate and return the current rating.
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update the number of wins.
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update the number of losses.
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        """
        Return ranking information.
        """
        pass
