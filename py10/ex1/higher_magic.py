#!/usr/bin/env python3

from typing import Callable, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    Combines two spells into a single callable that executes both.

    Args:
        spell1 (Callable): The first spell function.
        spell2 (Callable): The second spell function.

    Returns:
        Callable: A function that, when called, returns a tuple of the
                  results of spell1 and spell2 with the same arguments.
    """
    return lambda *x: (spell1(*x), spell2(*x))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Amplifies the effect of a spell by multiplying
    its output by a given factor.

    Args:
        base_spell (Callable): The spell function to amplify.
        multiplier (int): Factor to multiply the spell's output.

    Returns:
        Callable: A function that returns the amplified result of base_spell.
    """
    return lambda *x: base_spell(*x) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Creates a spell that only executes if a condition is met.

    Args:
        condition (Callable): Function that returns
        True if the spell should cast.
        spell (Callable): The spell function to execute if condition is True.

    Returns:
        Callable: A function that casts the spell or returns "Spell fizzled".
    """
    return lambda *x: spell(*x) if condition(*x) else "Spell fizzled"


def spell_sequence(spells: List[Callable]) -> Callable:
    """
    Executes a sequence of spells in order and returns their results.

    Args:
        spells (List[Callable]): List of spell functions to execute in order.

    Returns:
        Callable: A function that returns a list of results
        of all spells in the sequence.
    """
    return lambda *x: [spell(*x) for spell in spells]


def main() -> None:
    """
    Demonstrates higher-order spell functions.

    - Combines two spells using `spell_combiner`.
    - Amplifies a spell's output using `power_amplifier`.
    - Uses `conditional_caster` to cast a spell based on a condition.
    - Executes multiple spells in order using `spell_sequence`.

    Prints the results of each demonstration to the console.
    """
    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def lightning(target):
        return f"Lightning strikes {target}"

    def base_damage(target):
        return 10

    def is_enemy(target):
        return target in ("Dragon", "Goblin")

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", combined("Dragon"))

    print("\nTesting power amplifier...")
    mega_damage = power_amplifier(base_damage, 3)

    print(
        "Original:", base_damage("Dragon"),
        "Amplified:", mega_damage("Dragon")
    )

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(is_enemy, fireball)
    print("Casting on Dragon:", safe_fireball("Dragon"))
    print("Casting on Elf:", safe_fireball("Elf"))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning])
    results = sequence("Dragon")
    print("Sequence results:", results)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
