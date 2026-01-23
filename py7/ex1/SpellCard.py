#!/usr/bin/env python3

from . import Card, CardInfo, CardError, Play, GameState, CreatureInfo
from typing import Dict
from enum import Enum


class SpellInfo(Enum):
    EFFECT_TYPE = "effect_type"
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class Spell(Enum):
    SPELL = "spell"
    EFFECT_TYPE = "effect_type"
    EFFECT_VALUE = "effect_value"
    TARGET = "target"
    RESOLVED = "resolved"


class SpellCard(Card):

    def __init__(self, name, cost, rarity, effect_type: str):
        super().__init__(name, cost, rarity)
        self.info[CardInfo.TYPE.value] = "Spell"
        self.info[SpellInfo.EFFECT_TYPE.value] = effect_type

    def get_effect(self) -> str:
        value = self.info[CardInfo.COST.value]
        effects = {
            SpellInfo.DAMAGE.value: f"Deal {value} damage to target",
            SpellInfo.HEAL.value: f"Heal {value} damage to target",
            SpellInfo.BUFF.value: f"Give {value} attack point to target",
            SpellInfo.DEBUFF.value: f"Take {value} attack point to target"
        }
        return effects[self.info[SpellInfo.EFFECT_TYPE.value]]

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

        if self.info[SpellInfo.EFFECT_TYPE.value] == SpellInfo.BUFF.value:
            target[CreatureInfo.ATTACK.value] += self.info[CardInfo.COST.value]
        elif self.info[SpellInfo.EFFECT_TYPE.value] == SpellInfo.DEBUFF.value:
            target[CreatureInfo.ATTACK.value] -= self.info[CardInfo.COST.value]
            if target[CreatureInfo.ATTACK.value] < 1:
                target[CreatureInfo.ATTACK.value] = 1
        elif self.info[SpellInfo.EFFECT_TYPE.value] == SpellInfo.HEAL.value:
            target[CreatureInfo.HEALTH.value] += self.info[CardInfo.COST.value]
        elif self.info[SpellInfo.EFFECT_TYPE.value] == SpellInfo.DAMAGE.value:
            target[CreatureInfo.HEALTH.value] += self.info[CardInfo.COST.value]
            if target[CreatureInfo.HEALTH.value] < 0:
                target[CreatureInfo.HEALTH.value] = 0
        return {
            Spell.SPELL.value: self.infos[CardInfo.NAME.value],
            Spell.TARGET.value: target[CardInfo.NAME.value],
            Spell.EFFECT_TYPE.value: self.info[SpellInfo.EFFECT_TYPE.value],
            Spell.EFFECT_VALUE: self.info[CardInfo.COST.value],
            Spell.RESOLVED.value:
            target[CreatureInfo.HEALTH.value] == 0
        }
