#!/usr/bin/env python3

from typing import Any, Dict, Callable


def mage_counter() -> Callable:
    """
    Creates a simple counter for tracking the number of mage actions.

    Returns:
        Callable: A function that increments and returns the current count
                  each time it is called.
    """
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """
    Creates an accumulator to track the total power of a
    spell over multiple casts.

    Args:
        initial_power (int): Starting power value for the accumulator.

    Returns:
        Callable: A function that adds a given amount to the accumulated power
                and returns the updated total.
    """
    def accumulator(amount: int):
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """
    Creates a factory function to apply a specific enchantment to items.

    Args:
        enchantment_type (str): Type of enchantment
        (e.g., "Flaming", "Frozen").

    Returns:
        Callable: A function that, given an item name,
                returns a string combining
                the enchantment type and the item name.
    """
    def factory(item_name: str):
        nonlocal enchantment_type
        return f"{enchantment_type} {item_name}"
    return factory


def memory_vault() -> Dict[str, Callable]:
    """
    Creates a simple key-value memory vault
    with store and recall functionality.

    Returns:
        Dict[str, Callable]: A dictionary with two functions:
            - 'store'(key, value): Stores a value under the given key.
            - 'recall'(key) -> bool: Returns True if
            the key exists, False otherwise.
    """
    d = {}

    def store(key: Any, value: Any):
        nonlocal d
        d[key] = value

    def recall(key: Any) -> bool:
        nonlocal d
        return key in d

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    """
    Demonstrates the functionality of mage counters, spell accumulators,
    enchantment factories, and memory vaults.

    - Tests mage_counter by incrementing and printing counts.
    - Tests spell_accumulator by adding power values and printing totals.
    - Tests enchantment_factory by creating enchanted item names.
    - Tests memory_vault by storing values and checking key existence.
    """
    print("Testing mage counter...")
    counter = mage_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(10)
    print("Add 5:", accumulator(5))
    print("Add 7:", accumulator(7))
    print("Add 3:", accumulator(3))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print(flaming("Axe"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    store = vault["store"]
    recall = vault["recall"]

    store("spell", "Fireball")
    store("potion", "Healing")
    print("Recall 'spell':", recall("spell"))
    print("Recall 'potion':", recall("potion"))
    print("Recall 'ring':", recall("ring"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
