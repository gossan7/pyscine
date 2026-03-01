__version__ = "1.0.0"
__author__ = "vquetier"

__all__ = [
    "Card",
    "CardInfo",
    "CardError",
    "CreatureCard",
    "CreatureInfo",
    "GameState",
    "EliteCard"
]

from ex1 import Card, CardInfo, CardError, CreatureCard, \
    CreatureInfo, GameState
from .EliteCard import EliteCard
