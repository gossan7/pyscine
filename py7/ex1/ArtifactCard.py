from typing import Dict
from enum import Enum
from ex0.Card import Card, CardInfo, CardError, Play, GameState


class ArtifactInfo(Enum):
    """
    Enumeration of artifact-specific information keys stored in a card's info
    dictionary.
    """
    DURABILITY = "durability"
    EFFECT = "effect"


class Artifact(Enum):
    """
    Enumeration of keys used in the dictionary returned by artifact-related
    actions.
    """
    ARTIFACT = "artifact"
    EFFECT = "effect"
    ACTIVATED = "activated"


class ArtifactCard(Card):
    """
    Concrete card implementation representing an artifact.

    Artifacts are permanent cards that provide ongoing or activatable effects
    and remain in play until their durability
    is exhausted or they are destroyed.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        """
        Initialize a new ArtifactCard.

        :param name: Name of the artifact card
        :param cost: Mana cost required to play the card
        :param rarity: Rarity level of the card
        :param durability: Number of activations the artifact can sustain
        :param effect: Description of the artifact's effect
        """
        super().__init__(name, cost, rarity)
        self.info[CardInfo.TYPE.value] = "Artifact"
        self.info[ArtifactInfo.DURABILITY.value] = durability
        self.info[ArtifactInfo.EFFECT.value] = effect

    def play(self, game_state: Dict) -> Dict:
        """
        Play the artifact card by consuming mana and placing it into play.

        :param game_state: Dictionary representing the current game state
        :raises CardError: If there is not enough available mana
        :return: Dictionary describing the play action and its effect
        """
        if game_state[GameState.AVAILABLE_MANA.value] < \
                self.info[CardInfo.COST.value]:
            raise CardError("Not enough mana")

        game_state[GameState.AVAILABLE_MANA.value] -= \
            self.info[CardInfo.COST.value]

        return {
            Play.CARD_PLAYED.value: self.info[CardInfo.NAME.value],
            Play.MANA_USED.value: self.info[CardInfo.COST.value],
            Play.EFFECT.value: self.info[ArtifactInfo.EFFECT.value]
        }

    def activate_ability(self) -> Dict:
        """
        Activate the artifact's ability.

        This method reports the artifact's effect activation but does not
        control turn logic or game flow.

        :return: Dictionary describing the activated artifact effect
        """
        return {
            Artifact.ARTIFACT.value: self.info[CardInfo.NAME.value],
            Artifact.EFFECT.value: self.info[ArtifactInfo.EFFECT.value],
            Artifact.ACTIVATED.value: True
        }
