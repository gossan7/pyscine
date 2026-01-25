#!/usr/bin/env python3

from typing import Dict, List
from .TournamentCard import TournamentCard


class TournamentPlatform:
    """
    Platform managing tournament cards and matches.
    """

    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Register a tournament card.
        """
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        """
        Simulate a match between two cards.
        """
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        self.matches_played += 1

        if card1.attack_points >= card2.attack_points:
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> List:
        """
        Return cards ordered by rating.
        """
        return sorted(
            self.cards.values(),
            key=lambda c: c.rating,
            reverse=True
        )

    def generate_tournament_report(self) -> Dict:
        """
        Generate platform statistics.
        """
        avg_rating = sum(c.rating for c in self.cards.values()) \
            // len(self.cards)

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
