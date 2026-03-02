__version__ = "1.0.0"
__author__ = "vquetier"

__all__ = [
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

from .Deck import Deck, DeckInfo, DeckError
from .SpellCard import SpellCard, Spell, SpellInfo
from .ArtifactCard import ArtifactCard, Artifact, ArtifactInfo
