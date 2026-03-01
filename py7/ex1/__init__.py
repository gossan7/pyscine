__version__ = "1.0.0"
__author__ = "vquetier"

__all__ = [
    "Card",
    "CardInfo",
    "CardError",
    "Play",
    "GameState",
    "CreatureCard",
    "CreatureInfo",
    "Deck",
    "DeckInfo",
    "DeckError",
    "SpellCard",
    "Spell",
    "SpellInfo",
    "ArtifactCard",
    "Artifact",
    "ArtifactInfo"
]

from ex0.Card import Card, CardInfo, CardError, Play, GameState
from ex0.CreatureCard import CreatureCard, CreatureInfo
from .Deck import Deck, DeckInfo, DeckError
from .SpellCard import SpellCard, Spell, SpellInfo
from .ArtifactCard import ArtifactCard, Artifact, ArtifactInfo
