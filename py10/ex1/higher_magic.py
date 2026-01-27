#!/usr/bin/env python3

from typing import Callable, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda *x: (spell1(*x), spell2(*x))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda *x: base_spell(*x) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda *x: spell(*x) if condition(*x) else "Spell fizzled"


def spell_sequence(spells: List[Callable]) -> Callable:
    return lambda *x: [spell(*x) for spell in spells]


def main():
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
    print("Original:", base_damage("Dragon"),
          "Amplified:", mega_damage("Dragon"))

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(is_enemy, fireball)
    print("Casting on Dragon:", safe_fireball("Dragon"))
    print("Casting on Elf:", safe_fireball("Elf"))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning])
    results = sequence("Dragon")
    print("Sequence results:", results)


if __name__ == "__main__":
    main()
