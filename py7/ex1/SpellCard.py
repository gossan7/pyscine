#!/usr/bin/env python3

from . import Card, CardInfo, CardError, Play
from typing import Dict
from enum import Enum


class SpellInfo(Enum):
    EFFECT_TYPE = "effect_type"


class SpellCard(Card):
    def __init__(self, name, cost, rarity, effect_type: str):
        super().__init__(name, cost, rarity)
        self.infos[SpellInfo.EFFECT_TYPE.value] = effect_type

    def play(self, game_state):
        info = self.get_card_info()
        return {
            Play.CARD_PLAYED.value: self.
        }

    def resolve_effects(self, target: Dict):
        raise NotImplementedError