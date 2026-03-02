from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List


class Magic(Enum):
    """
    Enumeration of keys used in magic-related action results.
    """
    CASTER = "caster"
    SPELL = "spell"
    TARGETS = "targets"
    MANA_USED = "mana_used"
    CHANNELED = "channeled"
    TOTAL_MANA = "total_mana"


class Magical(ABC):
    """
    Abstract interface defining magical capabilities.
    """

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List[Dict]) -> Dict:
        """
        Cast a spell affecting one or more targets.

        :param spell_name: Name of the spell
        :param targets: List of target identifiers
        :return: Dictionary describing the spell cast
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """
        Channel additional mana.

        :param amount: Mana amount to channel
        :return: Dictionary describing mana channeling
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """
        Retrieve magic-related statistics.

        :return: Dictionary containing magic stats
        """
        pass
