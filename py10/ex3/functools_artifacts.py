#!/usr/bin/env python3

from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Dict, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError("Unsupported opperation")

    f = ops[operation]

    return reduce(f, spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="Fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="Ice"),
        "lightning_enchant": partial(base_enchantment,
                                     power=50, element="Lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast(spell: Any):
        return "Unknown spell type"

    @cast.register
    def _(power: int):
        return f"Deals {power} damage!"

    @cast.register
    def _(enchantment: str):
        return f"Enchants item with '{enchantment}'"

    @cast.register
    def _(spells: list):
        results = [cast(s) for s in spells]
        return results

    return cast


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} spell hits {target} with {power} power"


def main():
    spell_powers = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print("Sum:", spell_reducer(spell_powers, "add"))
    print("Product:", spell_reducer(spell_powers, "multiply"))
    print("Max:", spell_reducer(spell_powers, "max"))
    print("Min:", spell_reducer(spell_powers, "min"))

    print("\nTesting partial enchanter...")

    enchanter = partial_enchanter(base_enchantment)
    print(enchanter["fire_enchant"](target="Dragon"))
    print(enchanter["ice_enchant"](target="Goblin"))
    print(enchanter["lightning_enchant"](target="Orc"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(25))
    print(spell("Flaming Sword"))
    print(spell([10, "Ice Shield", 5]))


if __name__ == "__main__":
    main()
