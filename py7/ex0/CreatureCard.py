#!/usr/bin/env python3

from typing import Dict, Union
from . import Card, CardError, CardInfo, GameState, Play, Attack
from enum import Enum


class CreatureInfo(Enum):
    """Keys used to describe creature card information."""
    ATTACK = "attack"
    HEALTH = "health"


class CreatureCard(Card):
    """Concrete card representing a creature with combat capabilities."""

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        """
        Initialize a creature card.

        :param name: Name of the creature
        :param cost: Mana cost
        :param rarity: Card rarity
        :param attack: Attack power (must be positive)
        :param health: Health points (must be positive)
        """
        super().__init__(name, cost, rarity)

        if attack <= 0:
            raise CardError(f"Attack must be positive: {attack}")
        if health <= 0:
            raise CardError(f"Health must be positive: {health}")

        self.infos[CardInfo.TYPE.value] = "Creature"
        self.infos[CreatureInfo.ATTACK.value] = attack
        self.infos[CreatureInfo.HEALTH.value] = health

    def play(self, game_state: Dict) -> Dict:
        """
        Play the creature card, consuming mana and summoning it.

        :param game_state: Current game state
        :return: Result of playing the card
        """
        try:
            available_mana = game_state[GameState.AVAILABLE_MANA.value]
        except KeyError:
            raise CardError("Game state missing available mana")

        if not self.is_playable(available_mana):
            raise CardError("Not enough mana available")

        game_state[GameState.AVAILABLE_MANA.value] \
            -= self.infos[CardInfo.COST.value]

        return {
            Play.CARD_PLAYED.value: self.infos[CardInfo.NAME.value],
            Play.MANA_USED.value: self.infos[CardInfo.COST.value],
            Play.EFFECT.value: "Creature summoned to battlefield"
        }

    def attack_target(self, target: Dict[str, Union[str, int]],
                      game_state: Dict[str, Union[str, int]]) -> Dict:
        """
        Attack a target creature and resolve combat.

        :param target: Target creature info dictionary
        :param game_state: Current game state
        :return: Combat resolution details
        """
        try:
            target[CreatureInfo.HEALTH.value] \
                -= self.infos[CreatureInfo.ATTACK.value]
        except KeyError:
            raise CardError("Invalid target for attack")

        if target[CreatureInfo.HEALTH.value] <= 0:
            target[CreatureInfo.HEALTH.value] = 0
            game_state[GameState.AVAILABLE_MANA.value] += 2

        return {
            Attack.ATTACKER.value: self.infos[CardInfo.NAME.value],
            Attack.TARGET.value: target[CardInfo.NAME.value],
            Attack.DAMAGE_DEALT.value: self.infos[CreatureInfo.ATTACK.value],
            Attack.COMBAT_RESOLVED.value:
            target[CreatureInfo.HEALTH.value] == 0
        }
