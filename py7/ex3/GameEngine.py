#!/usr/bin/env python3

from typing import Dict, List
from ex3.GameStrategy import GameStrategy, StrategyAction
from ex3.CardFactory import CardFactory
from ex3 import Card, CreatureCard


class GameEngine:
    """
    Game orchestrator coordinating factory and strategy.
    """

    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.battle_field: List[Card] = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """
        Configure engine with factory and strategy.
        """
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        """
        Simulate a single game turn.
        """
        factory = self.factory
        strategy = self.strategy

        assert isinstance(factory, CardFactory)
        assert isinstance(strategy, GameStrategy)

        hand = [
            factory.create_creature("Fire Dragon"),
            factory.create_creature("Goblin Warrior"),
            factory.create_spell("Lightning Bolt")
        ]

        self.battle_field = [
            CreatureCard("Enemy Player", 0, "Common", 2, 10)
        ]

        self.cards_created += len(hand)

        actions = strategy.execute_turn(hand, self.battle_field)
        self.turns_simulated += 1
        self.total_damage += actions[StrategyAction.DAMAGE_DEALT.value]

        return {
            "hand": hand,
            "strategy": strategy.get_strategy_name(),
            "actions": actions
        }

    def get_engine_status(self) -> Dict:
        """
        Return engine statistics.
        """
        strategy = self.strategy
        assert isinstance(strategy, GameStrategy)

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
