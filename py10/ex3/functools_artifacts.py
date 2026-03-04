#!/usr/bin/env python3

from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Dict, Any


def spell_reducer(spells: list[int], operation: str) -> Any:
    """
    Reduces a list of spell power values using a specified operation.

    Args:
        spells (list[int]): List of integer spell powers.
        operation (str): Operation to perform: "add", "multiply",
        "max", or "min".

    Returns:
        int: The result of reducing the spell powers with the chosen operation.

    Raises:
        ValueError: If an unsupported operation is provided.
    """
    ops: Dict[str, Callable[[int, int], int]] = {
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
    """
    Creates partial functions for common enchantments with
    preset power and element.

    Args:
        base_enchantment (Callable): The base enchantment
        function to partially apply.

    Returns:
        Dict[str, Callable]: Dictionary mapping enchantment
        names to partial functions
                             (fire_enchant, ice_enchant, lightning_enchant).
    """
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="Fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="Ice"),
        "lightning_enchant": partial(base_enchantment,
                                     power=50, element="Lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Computes the nth Fibonacci number using memoization to cache results.

    Args:
        n (int): The index of the Fibonacci sequence to compute.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    """
    Creates a singledispatch function to handle spells of different types.

    Returns:
        Callable: A dispatch function that:
            - Returns a damage message if input is int.
            - Returns an enchantment message if input is str.
            - Returns a list of results if input is a list.
            - Returns "Unknown spell type" for other types.
    """
    @singledispatch
    def cast(spell: Any):
        """
        Default handler for spells of unknown types.

        Args:
            spell (Any): The spell input of unknown type.

        Returns:
            str: A default message indicating the spell type is unrecognized.
        """
        return "Unknown spell type"

    @cast.register
    def _(power: int):
        """
        Handles integer spell inputs representing damage values.

        Args:
            power (int): The amount of damage the spell deals.

        Returns:
            str: Message indicating how much damage the spell deals.
        """
        return f"Deals {power} damage!"

    @cast.register
    def _(enchantment: str):
        """
        Handles string spell inputs representing enchantments.

        Args:
            enchantment (str): The enchantment to apply.

        Returns:
            str: Message indicating the item has been enchanted.
        """
        return f"Enchants item with '{enchantment}'"

    @cast.register
    def _(spells: list):
        """
        Handles list inputs containing multiple spells of any supported types.

        Args:
            spells (list): List of spells (int, str, or nested lists).

        Returns:
            list: A list of results for each spell in the input list.
        """
        results = [cast(s) for s in spells]
        return results

    return cast


def base_enchantment(power: int, element: str, target: str) -> str:
    """
    Base function for applying an elemental spell to a target.

    Args:
        power (int): Spell power.
        element (str): Element type (e.g., Fire, Ice, Lightning).
        target (str): Target of the spell.

    Returns:
        str: Formatted string describing the spell effect on the target.
    """
    return f"{element} spell hits {target} with {power} power"


def main() -> None:
    """
    Demonstrates various higher-order spell utilities.

    - Uses spell_reducer to aggregate spell powers.
    - Uses partial_enchanter to create preset elemental spells.
    - Demonstrates memoized Fibonacci calculation.
    - Demonstrates a singledispatch spell dispatcher for different input types.
    """
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
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
