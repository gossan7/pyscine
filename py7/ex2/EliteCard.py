#!/usr/bin/env python3

from typing import Dict, List
from enum import Enum
from ex0.Card import Card, CardInfo, GameState
from .Combatable import Combatable, Combat
from .Magical import Magical, Magic


class EliteInfo(Enum):
    """
    Enumeration of elite-card-specific attributes.
    """
    ATTACK = "attack"
    HEALTH = "health"
    MANA = "mana"


class EliteCard(Card, Combatable, Magical):
    """
    Concrete card implementing multiple interfaces:
    Card, Combatable, and Magical.

    Elite cards combine combat and magic capabilities.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana: int):
        """
        Initialize an EliteCard.

        :param name: Card name
        :param cost: Mana cost to play
        :param rarity: Card rarity
        :param attack: Attack power
        :param health: Health points
        :param mana: Initial mana pool
        """
        super().__init__(name, cost, rarity)
        self.info[CardInfo.TYPE.value] = "Elite"
        self.info[EliteInfo.ATTACK.value] = attack
        self.info[EliteInfo.HEALTH.value] = health
        self.info[EliteInfo.MANA.value] = mana

    def play(self, game_state: Dict) -> Dict:
        """
        Play the elite card by consuming mana and entering play.

        :param game_state: Current game state
        :return: Dictionary describing the play action
        """
        game_state[GameState.AVAILABLE_MANA.value] -= \
            self.info[CardInfo.COST.value]

        return {
            "card_played": self.info[CardInfo.NAME.value],
            "mana_used": self.info[CardInfo.COST.value]
        }

    def attack(self, target: str) -> Dict:
        """
        Attack a target using combat power.

        :param target: Target identifier
        :return: Dictionary describing the attack
        """
        return {
            Combat.ATTACKER.value: self.info[CardInfo.NAME.value],
            Combat.TARGET.value: target,
            Combat.DAMAGE.value: self.info[EliteInfo.ATTACK.value],
            Combat.COMBAT_TYPE.value: "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        """
        Defend against incoming damage.

        :param incoming_damage: Damage received
        :return: Dictionary describing defense resolution
        """
        blocked = incoming_damage // 2
        taken = incoming_damage - blocked
        self.info[EliteInfo.HEALTH.value] -= taken

        return {
            Combat.DAMAGE_TAKEN.value: taken,
            Combat.DAMAGE_BLOCKED.value: blocked,
            Combat.STILL_ALIVE.value:
                self.info[EliteInfo.HEALTH.value] > 0
        }

    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        """
        Cast a spell using the card's mana pool.

        :param spell_name: Spell name
        :param targets: Spell targets
        :return: Dictionary describing the spell cast
        """
        mana_used = len(targets) * 2
        self.info[EliteInfo.MANA.value] -= mana_used

        return {
            Magic.CASTER.value: self.info[CardInfo.NAME.value],
            Magic.SPELL.value: spell_name,
            Magic.TARGETS.value: targets,
            Magic.MANA_USED.value: mana_used
        }

    def channel_mana(self, amount: int) -> Dict:
        """
        Channel additional mana into the card.

        :param amount: Mana to channel
        :return: Dictionary describing mana gain
        """
        self.info[EliteInfo.MANA.value] += amount
        return {
            Magic.CHANNELED.value: amount,
            Magic.TOTAL_MANA.value: self.info[EliteInfo.MANA.value]
        }

    def get_combat_stats(self) -> Dict:
        """
        Retrieve combat statistics.

        :return: Dictionary of combat stats
        """
        return {
            "attack": self.info[EliteInfo.ATTACK.value],
            "health": self.info[EliteInfo.HEALTH.value]
        }

    def get_magic_stats(self) -> Dict:
        """
        Retrieve magic statistics.

        :return: Dictionary of magic stats
        """
        return {
            "mana": self.info[EliteInfo.MANA.value]
        }
