#!/usr/bin/env python3

from . import Card
from typing import Dict


class SpellCard(Card):
    def __init__(self, name, cost, rarity, effetc_type: str):
        super().__init__(name, cost, rarity)
    
    def play(self, game_state):
        return super().play(game_state)
    
    def resolve_effects(self, target: Dict):
        raise NotImplementedError