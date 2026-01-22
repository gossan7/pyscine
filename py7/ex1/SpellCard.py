#!/usr/bin/env python3

from . import Card, CardInfo, CardError, Play, GameState
from typing import Dict
from enum import Enum


class SpellInfo(Enum):
    EFFECT_TYPE = "effect_type"
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):

    def __init__(self, name, cost, rarity, effect_type: str):
        super().__init__(name, cost, rarity)
        self.infos[SpellInfo.EFFECT_TYPE.value] = effect_type

    def get_effect(self) -> str:
        value = self.info[CardInfo.COST.value]
        effects = {
            SpellInfo.DAMAGE.value: f"Deal {value} damage to target",
            SpellInfo.HEAL.value: f"Heal {value} damage to target",
            SpellInfo.BUFF.value: f"Give {value} attack point to target",
            SpellInfo.DEBUFF.value: f"Take {value} attack point to target"
        }
        return effects[self.info[SpellInfo.EFFECT_TYPE]]

    def play(self, game_state):
        if game_state[GameState.AVAILABLE_MANA.value] \
                < self.info[CardInfo.COST.value]:
            raise CardError(
                f"Not enough mana to play {self.info[CardInfo.NAME.value]}"
            )

        game_state[GameState.AVAILABLE_MANA.value] \
            -= self.info[CardInfo.COST.value]

        return {
            Play.CARD_PLAYED.value: self.info[CardInfo.NAME.value],
            Play.MANA_USED.value: self.info[CardInfo.COST.value],
            Play.EFFECT.value: self.get_effect()
        }

    def resolve_effects(self, target: Dict):
        raise NotImplementedError
