from typing import Dict, List
from enum import Enum
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex3.GameStrategy import GameStrategy, StrategyAction
from ex3.CardFactory import CardFactory


class GameReport(Enum):
    TURN_SIMULATED = "turns_simulated"
    STRATEGY_USED = "strategy_used"
    TOTAL_DAMAGE = "total_damage"
    CARDS_CREATED = "cards_created"


class TurnReport(Enum):
    HAND = "hand"
    STRATEGY = "strategy"
    ACTIONS = "actions"


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
            CreatureCard("Enemy Player", 0, "Common", 2, 8)
        ]

        actions = strategy.execute_turn(hand, self.battle_field)

        self.cards_created += len(hand)

        self.turns_simulated += 1
        self.total_damage += actions[StrategyAction.DAMAGE_DEALT.value]

        return {
            TurnReport.HAND.value: hand,
            TurnReport.STRATEGY.value: strategy.get_strategy_name(),
            TurnReport.ACTIONS.value: actions
        }

    def get_engine_status(self) -> Dict:
        """
        Return engine statistics.
        """
        strategy = self.strategy
        assert isinstance(strategy, GameStrategy)

        return {
            GameReport.TURN_SIMULATED.value: self.turns_simulated,
            GameReport.STRATEGY_USED.value: strategy.get_strategy_name(),
            GameReport.TOTAL_DAMAGE.value: self.total_damage,
            GameReport.CARDS_CREATED.value: self.cards_created
        }
