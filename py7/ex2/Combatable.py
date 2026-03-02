from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class Combat(Enum):
    """
    Enumeration of keys used in combat-related action results.
    """
    ATTACKER = "attacker"
    DEFENDER = "defender"
    TARGET = "target"
    DAMAGE = "damage"
    DAMAGE_TAKEN = "damage_taken"
    DAMAGE_BLOCKED = "damage_blocked"
    STILL_ALIVE = "still_alive"
    COMBAT_TYPE = "combat_type"


class Combatable(ABC):
    """
    Abstract interface defining combat capabilities.
    """

    @abstractmethod
    def attack(self, target: Dict) -> Dict:
        """
        Perform an attack on a target.

        :param target: Identifier of the attack target
        :return: Dictionary describing the attack result
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        """
        Defend against incoming damage.

        :param incoming_damage: Amount of damage received
        :return: Dictionary describing the defense result
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        """
        Retrieve combat-related statistics.

        :return: Dictionary containing combat stats
        """
        pass
