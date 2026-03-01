#!/usr/bin/env python3

from typing import Dict, List
from random import choice
from . import CreatureCard, SpellCard, ArtifactCard, CardFactory


class FantasyCardFactory(CardFactory):
    """
    Concrete factory creating fantasy-themed cards.
    """

    def __init__(
            self,
            creatures: List[str],
            spells: List[str],
            artifacts: List[str]
    ):
        self.creatures = creatures
        self.spells = spells
        self.artifacts = artifacts

    def create_creature(self, name_or_power=None):
        name = choice(self.creatures)
        power = name_or_power if isinstance(name_or_power, int) else 5
        return CreatureCard(name, power, "Common", power, power)

    def create_spell(self, name_or_power=None):
        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power=None):
        return ArtifactCard("Mana Ring", 2, "Rare", 5, "Gain mana")

    def create_themed_deck(self, size: int) -> Dict:
        deck = []
        for _ in range(size):
            deck.append(self.create_creature())
        return {"deck": deck}

    def get_supported_types(self) -> Dict:
        return {
            "creatures": [c.lower() for c in self.creatures],
            "spells": [s.lower() for s in self.spells],
            "artifacts": [a.lower() for a in self.artifacts]
        }
