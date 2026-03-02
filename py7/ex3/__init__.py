__version__ = "1.0.0"
__author__ = "vquetier"

__all__ = [
    "GameStrategy",
    "CardFactory",
    "AggressiveStrategy",
    "FantasyCardFactory",
    "GameEngine",
    "GameReport",
    "TurnReport"
]

from .GameStrategy import GameStrategy
from .CardFactory import CardFactory
from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine, GameReport, TurnReport
