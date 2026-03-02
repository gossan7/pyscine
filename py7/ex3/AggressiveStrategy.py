from typing import Dict, List
from ex0.Card import Card, CardInfo
from ex0.CreatureCard import CreatureCard
from .GameStrategy import GameStrategy, StrategyAction


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

        def get_card_cost(card: Card):
            creature_cost = 1
            if isinstance(card, CreatureCard):
                creature_cost = 0
            cost = card.get_card_info()[CardInfo.COST.value]
            return (creature_cost, cost)

        hand = hand.copy()
        hand.sort(key=lambda x: get_card_cost(x))

        available_targets = [card for card in battlefield if card not in hand]
        prioritized = self.prioritize_targets(available_targets)

        attacked_targets = set()

        for card in hand:
            cost = card.get_card_info()[CardInfo.COST.value]
            attack = cost
            if isinstance(card, CreatureCard):
                attack = card.get_card_info()[CardInfo.ATTACK.value]
            enemy = next((
                enemy_card for enemy_card in prioritized
                if enemy_card.get_card_info()[CardInfo.HEALTH.value] > 0),
                None
            )

            if enemy is None:
                break

            cards_played.append(card.get_card_info()[CardInfo.NAME.value])

            attacked_targets.add(
                enemy.get_card_info()[CardInfo.NAME.value]
            )

            enemy.get_card_info()[CardInfo.HEALTH.value] -= attack

            if enemy.get_card_info()[CardInfo.HEALTH.value] < 0:
                attack += enemy.get_card_info()[CardInfo.HEALTH.value]

            mana_used += cost
            damage += attack

        return {
            StrategyAction.CARDS_PLAYED.value: cards_played,
            StrategyAction.MANA_USED.value: mana_used,
            StrategyAction.TARGETS_ATTACKED.value: list(attacked_targets),
            StrategyAction.DAMAGE_DEALT.value: damage
        }
