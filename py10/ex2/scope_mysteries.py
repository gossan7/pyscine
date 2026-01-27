#!/usr/bin/env python3

from typing import Any, Dict, Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(amount: int):
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def factory(item_name: str):
        nonlocal enchantment_type
        return f"{enchantment_type} {item_name}"
    return factory


def memory_vault() -> Dict[str, Callable]:
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


def main():
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
    main()
