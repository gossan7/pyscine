from typing import Dict, List
from enum import Enum
from ex2.Combatable import Combat
from ex4.TournamentCard import TournamentCard, TournamentInfo


class TournamentResult(Enum):
    WINNER = "winner"
    LOSER = "loser"
    WINNER_RATING = "winner_rating"
    LOSER_RATING = "loser_rating"


class TournamentReport(Enum):
    TOTAL_CARDS = "total_cards"
    MATCHES_PLAYED = "matches_played"
    AVG_RATING = "avg_rating"
    PLATFORM_STATUS = "platform_status"


class TournamentPlatform:
    """
    Platform managing tournament cards and matches.
    """

    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Register a tournament card.
        """
        id = card.info[TournamentInfo.CARD_ID.value]
        assert isinstance(id, str)
        self.cards[id] = card
        return id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        """
        Simulate a match between two cards.
        """
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        self.matches_played += 1

        card1_alive = True
        card2_alive = True

        while card1_alive and card2_alive:
            res = card1.attack(card2.info)
            card2_alive = res[Combat.STILL_ALIVE.value]
            res = card2.attack(card1.info)
            card1_alive = res[Combat.STILL_ALIVE.value]

        if not card2_alive:
            card1.update_wins(1)
            card2.update_losses(1)

            winner_id = card1_id
            loser_id = card2_id
            winner_rating = card1.info[TournamentInfo.RATING.value]
            loser_rating = card2.info[TournamentInfo.RATING.value]

        else:
            card2.update_wins(1)
            card1.update_losses(1)

            winner_id = card1_id
            loser_id = card2_id
            winner_rating = card1.info[TournamentInfo.RATING.value]
            loser_rating = card2.info[TournamentInfo.RATING.value]

        return {
            TournamentResult.WINNER.value: winner_id,
            TournamentResult.LOSER.value: loser_id,
            TournamentResult.WINNER_RATING.value: winner_rating,
            TournamentResult.LOSER_RATING.value: loser_rating
        }

    def get_leaderboard(self) -> List[TournamentCard]:
        """
        Return cards ordered by rating.
        """
        return sorted(
            self.cards.values(),
            key=lambda c: c.info[TournamentInfo.RATING.value],
            reverse=True
        )

    def generate_tournament_report(self) -> Dict:
        """
        Generate platform statistics.
        """
        ratings = [
            int(c.info[TournamentInfo.RATING.value])
            for c in self.cards.values()
        ]

        avg_rating = round(sum(ratings) / len(self.cards))

        return {
            TournamentReport.TOTAL_CARDS.value: len(self.cards),
            TournamentReport.MATCHES_PLAYED.value: self.matches_played,
            TournamentReport.AVG_RATING.value: avg_rating,
            TournamentReport.PLATFORM_STATUS.value: "active"
        }
