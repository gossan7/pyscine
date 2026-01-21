#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Dict


class 


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str):
        self.infos = {"name": name, "cost": cost, "rarity": rarity}

    @abstractmethod
    def play(self, game_state: Dict):
        pass

    def get_card_info(self):
        return self.infos

    def is_playable(self, avaliable_mana: int):
        return False if avaliable_mana < self.infos["cost"] else True
