#!/usr/bin/env python3

from typing import Dict
from .Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.infos["attack": attack, "health": health]

    def play(self, game_state: Dict):
        if self.is_playable(game_state["avaliable_mana"]):
            raise