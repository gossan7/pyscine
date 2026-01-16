#!/usr/bin/env python3


def main():
    """
    Analyze and compare player achievements using set operations.

    This function demonstrates how to use Python sets to:
    - Store unique achievements
    - Find common achievements between players
    - Identify rare achievements owned by only one player
    - Compare unique and shared achievements between players
    """
    print("=== Achievement Tracker System ===")

    alice = {
        'first_kill',
        'level_10',
        'treasure_hunter',
        'speed_demon',
    }

    bob = {
        'first_kill',
        'level_10',
        'boss_slayer',
        'collector',
    }

    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist',
    }

    all_achievement = alice.union(bob).union(charlie)

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {all_achievement}")
    print(f"Total unique achievements: {len(all_achievement)}")

    common = alice.intersection(bob).intersection(charlie)

    rare = alice.union(bob).union(charlie)
    rare = rare.difference(alice.intersection(bob))
    rare = rare.difference(bob.intersection(charlie))
    rare = rare.difference(charlie.intersection(alice))

    print(f"\nCommon to all players: {common}")
    print(f"Rare achievements (1 player): {rare}")
    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
