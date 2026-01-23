#!/usr/bin/env python3

from . import Card, CardInfo, CardError, Play, GameState
from typing import Dict
from enum import Enum


class ArtifactInfo(Enum):
    DURABILITY = "durability"
    EFFECT = "effect"


class Artifact(Enum):
    ARTIFACT = "artifact"
    EFFECT = "effect"
    ACTIVATED = "activated"


class ArtifactCard(Card):
    def __init__(self, name, cost, rarity, durability, effect):
        super().__init__(name, cost, rarity)
        self.info[CardInfo.TYPE.value] = "Artifact"
        self.info[ArtifactInfo.DURABILITY.value] = durability
        self.info[ArtifactInfo.EFFECT.value] = effect

    def play(self, game_state: Dict) -> Dict:
        if game_state[GameState.AVAILABLE_MANA.value] \
                < self.info[CardInfo.COST.value]:
            raise CardError("Not enough mana")

        game_state[GameState.AVAILABLE_MANA.value] \
            -= self.info[CardInfo.COST.value]

        return {
            Play.CARD_PLAYED.value: self.info[CardInfo.NAME.value],
            Play.MANA_USED.value: self.info[CardInfo.COST.value],
            Play.EFFECT.value: self.info[ArtifactInfo.EFFECT.value]
        }

    def activate_ability(self) -> Dict:
        return {
            Artifact.ARTIFACT.value: self.info[CardInfo.NAME.value],
            Artifact.EFFECT.value: self.info[ArtifactInfo.EFFECT.value],
            Artifact.ACTIVATED: True
        }
