from typing import Dict
from enum import Enum
from ex0.Card import Card, CardInfo, CardError, GameState, Play
from ex2.Combatable import Combatable, Combat
from ex4.Rankable import Rankable


class TournamentInfo(Enum):
    """
    Keys used for tournament statistics.
    """
    WINS = "wins"
    LOSSES = "losses"
    RATING = "rating"
    ATTACK = "attack"
    HEALTH = "health"
    MANA = "mana"
    CARD_ID = "id"


class TournamentCard(Card, Combatable, Rankable):
    """
    Card enhanced with combat and ranking capabilities
    for tournament play.
    """

    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        rating: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.info[CardInfo.TYPE.value] = "Tournament"
        self.info[CardInfo.ATTACK.value] = attack
        self.info[CardInfo.HEALTH.value] = health
        self.info[TournamentInfo.WINS.value] = 0
        self.info[TournamentInfo.LOSSES.value] = 0
        self.info[TournamentInfo.RATING.value] = rating
        self.info[TournamentInfo.CARD_ID.value] = card_id

    def play(self, game_state: Dict) -> Dict:
        """
        Play the tournament card
        """
        try:
            available_mana = game_state[GameState.AVAILABLE_MANA.value]
        except KeyError:
            raise CardError("Game state missing available mana")

        if not self.is_playable(available_mana):
            raise CardError("Not enough mana available")

        game_state[GameState.AVAILABLE_MANA.value] \
            -= self.info[CardInfo.COST.value]

        return {
            Play.CARD_PLAYED.value: self.info[CardInfo.NAME.value],
            Play.MANA_USED.value: self.info[CardInfo.COST.value],
        }

    def attack(self, target: Dict) -> Dict:
        """
        Attack another card using its card info dictionary.
        """

        attack = self.info[CardInfo.ATTACK.value]
        target_health = target[CardInfo.HEALTH.value] - attack

        if target_health < 0:
            attack += target_health

        target[CardInfo.HEALTH.value] = max(0, target_health)
        still_alive = target[CardInfo.HEALTH.value] > 0

        return {
            Combat.ATTACKER.value: self.info[CardInfo.NAME.value],
            Combat.TARGET.value: target["name"],
            Combat.DAMAGE.value: attack,
            Combat.STILL_ALIVE.value: still_alive
        }

    def defend(self, incoming_damage: int) -> Dict:
        """
        Defend against incoming damage.
        """
        health = self.info[CardInfo.HEALTH.value]
        assert isinstance(health, int)

        blocked = incoming_damage // 2
        taken = incoming_damage - blocked
        health -= taken

        self.info[CardInfo.HEALTH.value] = health

        return {
            Combat.DEFENDER.value: self.info[CardInfo.NAME.value],
            Combat.DAMAGE_TAKEN.value: taken,
            Combat.DAMAGE_BLOCKED.value: blocked,
            Combat.STILL_ALIVE.value: health > 0
        }

    def get_combat_stats(self) -> Dict:
        """
        Return combat statistics.
        """
        return {
            CardInfo.ATTACK.value: self.info[CardInfo.ATTACK.value],
            CardInfo.HEALTH.value: self.info[CardInfo.HEALTH.value]
        }

    def calculate_rating(self) -> int:
        """
        Simple ELO-like rating calculation.
        """
        rating = self.info[TournamentInfo.RATING.value]
        assert isinstance(rating, int)
        return rating

    def update_wins(self, wins: int) -> None:
        rating = self.info[TournamentInfo.RATING.value]
        curr_wins = self.info[TournamentInfo.WINS.value]

        assert isinstance(rating, int)
        assert isinstance(curr_wins, int)

        rating += wins * 16
        curr_wins += wins

        self.info[TournamentInfo.WINS.value] = curr_wins
        self.info[TournamentInfo.RATING.value] = rating

    def update_losses(self, losses: int) -> None:
        rating = self.info[TournamentInfo.RATING.value]
        curr_losses = self.info[TournamentInfo.LOSSES.value]

        assert isinstance(rating, int)
        assert isinstance(curr_losses, int)

        rating -= losses * 16
        curr_losses += losses

        self.info[TournamentInfo.LOSSES.value] = curr_losses
        self.info[TournamentInfo.RATING.value] = rating

    def get_rank_info(self) -> Dict:
        """
        Return ranking statistics.
        """
        return {
            TournamentInfo.WINS.value:
            self.info[TournamentInfo.WINS.value],

            TournamentInfo.LOSSES.value:
            self.info[TournamentInfo.LOSSES.value],

            TournamentInfo.RATING.value:
            self.info[TournamentInfo.RATING.value]
        }

    def get_tournament_stats(self) -> Dict:
        """
        Return full tournament statistics.
        """
        return {
            CardInfo.NAME.value:
            self.info[CardInfo.NAME.value],

            TournamentInfo.CARD_ID.value:
            self.info[TournamentInfo.CARD_ID.value],

            TournamentInfo.WINS.value:
            self.info[TournamentInfo.WINS.value],

            TournamentInfo.LOSSES.value:
            self.info[TournamentInfo.LOSSES.value],

            TournamentInfo.RATING.value:
            self.info[TournamentInfo.RATING.value]
        }
