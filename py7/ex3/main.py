#!/usr/bin/env python3

from ex3 import GameEngine, AggressiveStrategy, FantasyCardFactory, \
    TurnReport

from ex0.Card import CardInfo


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    engine.configure_engine(factory, strategy)

    print("\nSimulating aggressive turn...")

    turn = engine.simulate_turn()

    hand_str = ", ".join([
        f"{c.get_card_info()[CardInfo.NAME.value]} "
        f"({c.get_card_info()[CardInfo.COST.value]})"
        for c in turn[TurnReport.HAND.value]
    ])

    print(f"Hand: [{hand_str}]")

    print("\nTurn execution:")
    print("Strategy:", turn[TurnReport.STRATEGY.value])
    print("Actions:", turn[TurnReport.ACTIONS.value])

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern:",
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
