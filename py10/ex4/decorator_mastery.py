#!/usr/bin/env python3

from functools import wraps
from time import time
from typing import Callable, Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def timer(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return timer


def power_validator(min_power: int) -> Callable[[Callable[..., Any]],
                                                Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def validator(*args: Any, **kwargs: Any) -> Any:
            if len(args) < 1:
                return "Insufficient power for this spell"
            elif not isinstance(args[0], int):
                return "Insufficient power for this spell"
            if args[0] < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return validator
    return decorator


def retry_spell(max_attempts: int) -> Callable[[Callable[..., Any]],
                                               Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def retry(*args: Any, **kwargs: Any) -> Any:
            for n in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying...",
                          f"(attempt {n + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return retry
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            return False
        if len(name) < 3:
            return False
        if not all(c.isspace() or c.isalpha() for c in name):
            return False
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def spell(power: int) -> str:
            return f"Successfully cast {spell_name} with {power} power"
        return spell(power)


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        return "Fireball cast!"

    result = fireball()
    print("Result:", result)
    print()

    print("Testing MageGuild...")
    mage = MageGuild()

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))

    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Weak Spark", 5))
    print()

    print("Testing retry spell...")

    @retry_spell(5)
    def lightning() -> None:
        raise ValueError

    result = lightning()
    print("Result:", result)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
