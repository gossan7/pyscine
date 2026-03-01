__version__ = "1.0.0"
__author__ = "vquetier"

__all__ = [
    "Card",
    "CardInfo",
    "GameState",
    "CardError",
    "Play",
    "Attack",
    "CreatureCard",
    "CreatureInfo"
]

from .Card import Card, CardInfo, GameState, \
    CardError, Play, Attack

from .CreatureCard import CreatureCard, CreatureInfo
