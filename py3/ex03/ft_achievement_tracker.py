#!/usr/bin/env python3


def main():
    print("=== Achievemt Tracker System ===")
    all = {'boss_slayer', 'collector', 'first_kill', 'level_10',
           'perfectionist', 'speed_demon', 'treasure_hunter'}
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievements Analytics ===")
    print(f"All unique achievements: {all}")
    print(f"Total unique achievements: {len(all)}")
    common = alice & bob & charlie
    rare = (alice | bob | charlie) - \
           (alice & bob) - \
           (alice & charlie) - \
           (bob & charlie)
    print(f"\nCommon to all players: {common}")
    print(f"Rare achievements (1 player): {rare}")
    print(f"\nAlice vs Bob common: {alice & bob}")
    print(f"Alice unique: {(alice | bob) - bob}")
    print(f"Bob unique: {(alice | bob) - alice}")


if __name__ == "__main__":
    main()
