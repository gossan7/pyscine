#!/usr/bin/env python3

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """
    Create the philosopher's stone.

    Combines a lead-to-gold transmutation with a healing potion.

    Returns:
        str: Description of the philosopher's stone creation.
    """
    return ("Philosopher’s stone created "
            f"using {lead_to_gold()} and {healing_potion()}")


def elixir_of_life() -> str:
    """
    Create the elixir of life.

    Returns:
        str: Description of the elixir of life.
    """
    return "Elixir of life: eternal youth achieved!"
