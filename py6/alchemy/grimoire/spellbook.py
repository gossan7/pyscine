#!/usr/bin/env python3

from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Record a spell if its ingredients are valid.

    Calls `validate_ingredients` to check the provided ingredients. If the
    ingredients are valid, the spell is recorded; otherwise, it is rejected.

    Args:
        spell_name (str): The name of the spell being recorded.
        ingredients (str): Space-separated list of ingredients for the spell.

    Returns:
        str: Message indicating whether the spell was recorded or rejected,
             including the validation result.
    """
    validation = validate_ingredients(ingredients)
    if validation.split(" ")[-1] == "VALID":
        return f"Spell recorded: {spell_name} {validation}"
    return f"Spell rejected: {spell_name} {validation}"
