#!/usr/bin/env python3

from typing import Dict, List
from enum import Enum
from .GameStrategy import GameStrategy


class AggressiveAction(Enum):
    """
    Keys used for aggressive strategy actions.
    """
    CARDS_PLAYED = "cards_played"
    MANA_USED = "mana_used"
    TARGETS_ATTACKED = "targets_attacked"
    DAMAGE_DEALT = "damage_dealt"


class AggressiveStrategy(GameStrategy):
    """
    Concrete strategy prioritizing damage and board presence.
    """

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        """
        Aggressive strategy prioritizes enemy player first.
        """
        return sorted(available_targets)

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """
        Execute an aggressive turn:
        - play low-cost cards
        - attack immediately
        """
        cards_played = []
        damage = 0
        mana_used = 0

        for card in hand:
            cost = card.get_card_info()["cost"]
            if cost <= 3:
                cards_played.append(card.get_card_info()["name"])
                mana_used += cost
                damage += cost

        return {
            AggressiveAction.CARDS_PLAYED.value: cards_played,
            AggressiveAction.MANA_USED.value: mana_used,
            AggressiveAction.TARGETS_ATTACKED.value: ["Enemy Player"],
            AggressiveAction.DAMAGE_DEALT.value: damage
        }
