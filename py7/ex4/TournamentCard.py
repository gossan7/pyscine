#!/usr/bin/env python3

from typing import Dict
from enum import Enum
from ex0.Card import Card, CardInfo
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentInfo(Enum):
    """
    Keys used for tournament statistics.
    """
    WINS = "wins"
    LOSSES = "losses"
    RATING = "rating"


class TournamentCard(Card, Combatable, Rankable):
    """
    Card enhanced with combat and ranking capabilities
    for tournament play.
    """

    def __init__(self, card_id: str, name: str, cost: int,
                 rarity: str, attack: int, health: int,
                 rating: int = 1200):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.info[CardInfo.TYPE.value] = "Tournament"

        self.attack_points = attack
        self.health_points = health

        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self, game_state: Dict) -> Dict:
        """
        Tournament cards do not consume mana during matches.
        """
        return {
            "card_played": self.info[CardInfo.NAME.value],
            "mode": "tournament"
        }

    def attack(self, target: Dict) -> Dict:
        """
        Attack another card using its card info dictionary.
        """
        target_health = target["health"] - self.attack_points
        target["health"] = max(0, target_health)

        return {
            "attacker": self.info[CardInfo.NAME.value],
            "target": target["name"],
            "damage": self.attack_points
        }

    def defend(self, incoming_damage: int) -> Dict:
        """
        Defend against incoming damage.
        """
        blocked = incoming_damage // 2
        taken = incoming_damage - blocked
        self.health_points -= taken

        return {
            "defender": self.info[CardInfo.NAME.value],
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health_points > 0
        }

    def get_combat_stats(self) -> Dict:
        """
        Return combat statistics.
        """
        return {
            "attack": self.attack_points,
            "health": self.health_points
        }

    def calculate_rating(self) -> int:
        """
        Simple ELO-like rating calculation.
        """
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> Dict:
        """
        Return ranking statistics.
        """
        return {
            TournamentInfo.WINS.value: self.wins,
            TournamentInfo.LOSSES.value: self.losses,
            TournamentInfo.RATING.value: self.rating
        }

    def get_tournament_stats(self) -> Dict:
        """
        Return full tournament statistics.
        """
        return {
            "id": self.card_id,
            "name": self.info[CardInfo.NAME.value],
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }
