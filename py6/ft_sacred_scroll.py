#!/usr/bin/env python3

import alchemy


def main() -> None:
    """
    Run the sacred scroll demonstration.

    Tests direct module access, package-level access controlled by
    __init__.py, and displays package metadata.
    """
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")

    print(
        "alchemy.elements.create_fire():",
        alchemy.elements.create_fire()
    )

    print(
        "alchemy.elements.create_water():",
        alchemy.elements.create_water()
    )

    print(
        "alchemy.elements.create_earth():",
        alchemy.elements.create_earth()
    )

    print(
        "alchemy.elements.create_air():",
        alchemy.elements.create_air()
    )

    print()

    print("Testing package-level access (controlled by __init__.py):")

    print(
        "alchemy.create_fire():",
        alchemy.create_fire()
    )

    print(
        "alchemy.create_water():",
        alchemy.create_water()
    )

    print("alchemy.create_earth(): ", end="")

    try:
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")

    print("alchemy.create_air(): ", end="")
    try:
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
