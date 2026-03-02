#!/usr/bin/env python3

from typing import Dict, List
from .GameStrategy import GameStrategy, StrategyAction
from ex3 import CardInfo, Card, CreatureCard


class AggressiveStrategy(GameStrategy):
    """
    Concrete strategy prioritizing damage and board presence.
    """

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[Card]) -> List[Card]:
        """
        Aggressive strategy prioritizes enemy player first.
        """
        return sorted(
            available_targets,
            key=lambda x: x.get_card_info()[CardInfo.HEALTH.value]
        )

    def execute_turn(self, hand: List[Card], battlefield: List[Card]) -> Dict:
        """
        Execute an aggressive turn:
        - play low-cost cards
        - attack immediately
        """
        cards_played = []
        damage = 0
        mana_used = 0
        hand.sort(key=lambda x: x.get_card_info()[CardInfo.COST.value])
        available_targets = [card for card in battlefield if card not in hand]
        prioritized = self.prioritize_targets(available_targets)
        attacked_targets = set()

        for card in hand:
            cost = card.get_card_info()[CardInfo.COST.value]
            attack = cost
            if isinstance(card, CreatureCard):
                attack = card.get_card_info()[CardInfo.ATTACK.value]
            cards_played.append(card.get_card_info()[CardInfo.NAME.value])
            enemy = next((
                enemy_card for enemy_card in prioritized
                if enemy_card.get_card_info()[CardInfo.HEALTH.value] > 0),
                None
            )

            if enemy is None:
                break

            attacked_targets.add(
                enemy.get_card_info()[CardInfo.NAME.value]
            )

            enemy.get_card_info()[CardInfo.HEALTH.value] -= attack

            mana_used += cost
            damage += attack

        return {
            StrategyAction.CARDS_PLAYED.value: cards_played,
            StrategyAction.MANA_USED.value: mana_used,
            StrategyAction.TARGETS_ATTACKED.value: list(attacked_targets),
            StrategyAction.DAMAGE_DEALT.value: damage
        }
