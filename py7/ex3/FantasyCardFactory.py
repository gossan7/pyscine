from typing import Dict
from random import choice
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """
    Concrete factory creating fantasy-themed cards.
    """

    def __init__(self) -> None:
        self.creatures = [
            (
                "Fire Dragon",
                5,
                "Legendary",
                7,
                5
            ),
            (
                "Goblin Warrior",
                2,
                "Common",
                1,
                5
            )
        ]

        self.spells = [
            (
                "Lightning Bolt",
                3,
                "Rare",
                "damage"
            ),
            (
                "Fireball",
                4,
                "Rare",
                "damage"
            )
        ]

        self.artifacts = [
            (
                "Mana Ring",
                2,
                "Rare",
                5,
                "+10 Available mana"
            )
        ]

    def create_creature(self, name_or_power=None) -> CreatureCard:
        match name_or_power:
            case int():
                args = next((
                    arg for arg in self.creatures
                    if arg[3] == name_or_power), None
                )

            case str():
                args = next((
                    arg for arg in self.creatures
                    if arg[0] == name_or_power), None
                )

            case None:
                args = choice(self.creatures)

            case _:
                raise ValueError("name_or_power should be int | str | None")

        if args is None:
            raise ValueError(
                f"No CreatureCard has the name_or_power {name_or_power}")

        return CreatureCard(*args)

    def create_spell(self, name_or_power=None) -> SpellCard:
        match name_or_power:
            case int():
                args = next((
                    arg for arg in self.spells
                    if arg[3] == name_or_power), None
                )

            case str():
                args = next((
                    arg for arg in self.spells
                    if arg[0] == name_or_power), None
                )

            case None:
                args = choice(self.spells)

            case _:
                raise ValueError("name_or_power should be int | str | None")

        if args is None:
            raise ValueError(
                f"No SpellCard has the name_or_power {name_or_power}")

        return SpellCard(*args)

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        match name_or_power:
            case int():
                args = next((
                    arg for arg in self.artifacts
                    if arg[3] == name_or_power), None
                )

            case str():
                args = next((
                    arg for arg in self.artifacts
                    if arg[0] == name_or_power), None
                )

            case None:
                args = choice(self.artifacts)

            case _:
                raise ValueError("name_or_power should be int | str | None")

        if args is None:
            raise ValueError(
                f"No ArtifactCard has the name_or_power {name_or_power}")

        return ArtifactCard(*args)

    def create_themed_deck(self, size: int) -> Dict:
        deck = []

        possible_cards = [
            self.create_creature,
            self.create_spell,
            self.create_artifact
        ]

        for _ in range(size):
            create_card = choice(possible_cards)
            deck.append(create_card())

        return {"deck": deck}

    def get_supported_types(self) -> Dict:
        return {
            'creatures': ["dragon", "goblin"],
            'spells': ["fireball", "lightning_bolt"],
            'artifacts': ["mana_ring"]
        }
