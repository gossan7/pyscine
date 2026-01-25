#!/usr/bin/env python3

from typing import Dict
from . import GameStrategy, CardFactory


class GameEngine:
    """
    Game orchestrator coordinating factory and strategy.
    """

    def __init__(self):
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

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
        hand = [
            self.factory.create_creature(),
            self.factory.create_creature(),
            self.factory.create_spell()
        ]

        self.cards_created += len(hand)

        actions = self.strategy.execute_turn(hand, [])
        self.turns_simulated += 1
        self.total_damage += actions["damage_dealt"]

        return {
            "hand": hand,
            "strategy": self.strategy.get_strategy_name(),
            "actions": actions
        }

    def get_engine_status(self) -> Dict:
        """
        Return engine statistics.
        """
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
