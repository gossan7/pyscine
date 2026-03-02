from enum import Enum
from typing import Dict
from ex0.Card import Card, CardInfo, CardError, Play, GameState
from ex0.CreatureCard import CreatureInfo


class SpellInfo(Enum):
    """
    Enumeration of spell-specific information stored in a card's info
    dictionary.
    """
    EFFECT_TYPE = "effect_type"
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class Spell(Enum):
    """
    Enumeration of keys used in dictionaries returned by spell-related
    actions.
    """
    SPELL = "spell"
    EFFECT_TYPE = "effect_type"
    EFFECT_VALUE = "effect_value"
    TARGET = "target"
    RESOLVED = "resolved"


class SpellCard(Card):
    """
    Concrete card implementation representing a spell.

    Spells apply one-time effects such as damage, healing, buffs, or
    debuffs and are consumed when played.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        """
        Initialize a new SpellCard.

        :param name: Name of the spell card
        :param cost: Mana cost required to play the spell
        :param rarity: Rarity level of the card
        :param effect_type: Type of effect applied by the spell
        """
        super().__init__(name, cost, rarity)
        self.info[CardInfo.TYPE.value] = "Spell"
        self.info[SpellInfo.EFFECT_TYPE.value] = effect_type

    def get_effect(self) -> str:
        """
        Generate a human-readable description of the spell's effect.

        :return: Description string representing the spell effect
        """
        value = self.info[CardInfo.COST.value]
        effects: Dict[str, str] = {
            SpellInfo.DAMAGE.value: f"Deal {value} damage to target",
            SpellInfo.HEAL.value: f"Heal {value} damage to target",
            SpellInfo.BUFF.value: f"Give {value} attack point to target",
            SpellInfo.DEBUFF.value: f"Take {value} attack point to target"
        }
        effect_type = self.info[SpellInfo.EFFECT_TYPE.value]
        assert isinstance(effect_type, str)
        return effects[effect_type]

    def play(self, game_state: Dict) -> Dict:
        """
        Play the spell card by consuming mana and resolving its effect.

        :param game_state: Dictionary representing the current game state
        :raises CardError: If there is not enough available mana
        :return: Dictionary describing the play action and its effect
        """
        if game_state[GameState.AVAILABLE_MANA.value] < \
                self.info[CardInfo.COST.value]:
            raise CardError(
                f"Not enough mana to play {self.info[CardInfo.NAME.value]}"
            )

        game_state[GameState.AVAILABLE_MANA.value] -= \
            self.info[CardInfo.COST.value]

        return {
            Play.CARD_PLAYED.value: self.info[CardInfo.NAME.value],
            Play.MANA_USED.value: self.info[CardInfo.COST.value],
            Play.EFFECT.value: self.get_effect()
        }

    def resolve_effects(self, target: Dict) -> Dict:
        """
        Apply the spell's effect to a target entity.

        This method mutates the target's stats based on the spell's
        effect type and reports the outcome.

        :param target: Dictionary representing the target's attributes
        :return: Dictionary describing the resolved spell effect
        """
        if self.info[SpellInfo.EFFECT_TYPE.value] == SpellInfo.BUFF.value:
            target[CreatureInfo.ATTACK.value] += \
                self.info[CardInfo.COST.value]

        elif self.info[SpellInfo.EFFECT_TYPE.value] == SpellInfo.DEBUFF.value:
            target[CreatureInfo.ATTACK.value] -= \
                self.info[CardInfo.COST.value]

            if target[CreatureInfo.ATTACK.value] < 1:
                target[CreatureInfo.ATTACK.value] = 1

        elif self.info[SpellInfo.EFFECT_TYPE.value] == SpellInfo.HEAL.value:
            target[CreatureInfo.HEALTH.value] += \
                self.info[CardInfo.COST.value]

        elif self.info[SpellInfo.EFFECT_TYPE.value] == SpellInfo.DAMAGE.value:
            target[CreatureInfo.HEALTH.value] -= \
                self.info[CardInfo.COST.value]

            if target[CreatureInfo.HEALTH.value] < 0:
                target[CreatureInfo.HEALTH.value] = 0

        return {
            Spell.SPELL.value: self.info[CardInfo.NAME.value],
            Spell.TARGET.value: target[CardInfo.NAME.value],

            Spell.EFFECT_TYPE.value:
                self.info[SpellInfo.EFFECT_TYPE.value],

            Spell.EFFECT_VALUE.value:
                self.info[CardInfo.COST.value],

            Spell.RESOLVED.value:
                target[CreatureInfo.HEALTH.value] == 0
        }
