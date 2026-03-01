#!/usr/bin/env python3

from .elements import create_fire, create_water, create_air, create_earth


def healing_potion() -> str:
    """
    Brew a healing potion.

    Combines fire and water elements to create a healing potion.

    Returns:
        str: Description of the healing potion.
    """
    return (f"Healing potion brewed with {create_fire()} "
            f"and {create_water()}")


def strength_potion() -> str:
    """
    Brew a strength potion.

    Combines earth and fire elements to create a strength potion.

    Returns:
        str: Description of the strength potion.
    """
    return (f"Strength potion brewed with {create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    """
    Brew an invisibility potion.

    Combines air and water elements to create an invisibility potion.

    Returns:
        str: Description of the invisibility potion.
    """
    return (f"Invisibility potion brewed with {create_air()} "
            f"and {create_water()}")


def wisdom_potion() -> str:
    """
    Brew a wisdom potion.

    Combines all four elemental creations into a single potion.

    Returns:
        str: Description of the wisdom potion.
    """
    return "Wisdom potion brewed with all elements: " + create_fire() \
        + create_water() \
        + create_earth() \
        + create_air()
