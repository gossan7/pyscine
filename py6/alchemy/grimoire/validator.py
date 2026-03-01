#!/usr/bin/env python3


def validate_ingredients(ingredients: str) -> str:
    """
    Check if ingredients are valid.

    Args:
        ingredients (str): Space-separated string of elements.

    Returns:
        str: Success or error message.
    """
    valid = {"fire", "water", "earth", "air"}
    split = ingredients.split(" ")
    if any(ing in valid for ing in split):
        return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
