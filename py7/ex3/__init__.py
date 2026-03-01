__version__ = "1.0.0"
__author__ = "vquetier"

__all__ = [
    "Card",
    "CardError",
    "CardInfo",
    "CreatureCard",
    "GameState",
    "EliteCard",
    "Spell",
    "SpellCard",
    "SpellInfo",
    "Artifact",
    "ArtifactCard",
    "ArtifactInfo",
    "GameStrategy",
    "CardFactory",
    "AggressiveStrategy",
    "FantasyCardFactory",
    "GameEngine"
]

from ex2 import Card, CardError, CardInfo, \
    CreatureCard, GameState, EliteCard

from ex1 import Spell, SpellCard, SpellInfo, Artifact, \
    ArtifactCard, ArtifactInfo

from .GameStrategy import GameStrategy
from .CardFactory import CardFactory
from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine
