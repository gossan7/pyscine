#!/usr/bin/env python3
from typing import List, Dict, Any


def artifact_sorter(artifacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Sorts a list of artifact dictionaries by their 'power' in descending order.

    Args:
        artifacts (List[Dict[str, Any]]): List of artifacts,
        each with at least a 'power' key.

    Returns:
        List[Dict[str, Any]]: Artifacts sorted from highest to lowest power.
    """
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: List[Dict[str, Any]], min_power: int) \
        -> List[Dict[str, Any]]:
    """
    Filters mages based on a minimum power threshold.

    Args:
        mages (List[Dict[str, Any]]): List of mage
        dictionaries, each with a 'power' key.
        min_power (int): Minimum power required to include the mage.

    Returns:
        List[Dict[str, Any]]: List of mages whose power is
        greater than or equal to min_power.
    """
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    """
    Transforms a list of spell names by wrapping each spell with '*'.

    Args:
        spells (List[str]): List of spell names as strings.

    Returns:
        List[str]: List of transformed spell names, e.g., "* spell *".
    """
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Computes basic statistics (max, min, average) for mage powers.

    Args:
        mages (List[Dict[str, Any]]): List of mage dictionaries,
        each with a 'power' key.

    Returns:
        Dict[str, Any]: Dictionary with 'max_power', 'min_power',
        and 'avg_power' keys.
    """
    powers = list(map(lambda x: x["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)
    }


def main() -> None:
    """
    Demonstrates the functionality of artifact and mage utility functions.

    - Sorts artifacts by power.
    - Filters mages above a specified power threshold.
    - Transforms spell names for display.
    - Computes and prints mage power statistics.
    """
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Wind Dagger", "power": 75, "type": "dagger"},
    ]

    mages = [
        {"name": "Gandalf", "power": 95, "element": "fire"},
        {"name": "Merlin", "power": 80, "element": "water"},
        {"name": "Morgana", "power": 88, "element": "earth"},
        {"name": "Rincewind", "power": 60, "element": "air"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for a in sorted_artifacts:
        print(f"{a['name']} ({a['power']} power)")

    print("\nTesting power filter (min_power=85)...")
    strong_mages = power_filter(mages, 85)
    for m in strong_mages:
        print(f"{m['name']} ({m['power']} power)")

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Average power: {stats['avg_power']}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
