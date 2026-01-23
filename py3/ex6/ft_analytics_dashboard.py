#!/usr/bin/env python3


def main():
    """
    Demonstrate list, dict, and set comprehensions through
    a simple game analytics dashboard.
    """
    print("=== Game Analytics Dashboard ===\n")

    players = {'alice': {'score': 2300,
                         'achievement': {'first_kill', 'level_10'},
                         'active': True,
                         'region': 'north'},
               'bob': {'score': 1800,
                       'achievement': {'boss_slayer', 'first_kill'},
                       'active': True,
                       'region': 'east'},
               'charlie': {'score': 2150,
                           'achievement': {'boss_slayer', 'level_10'},
                           'active': True,
                           'region': 'central'},
               'diana': {'score': 2050,
                         'achievement': {'level_10'},
                         'active': False,
                         'region': 'west'}}

    print("=== List Comprehension Examples ===")

    high_scores = [player for player in players
                   if players[player]['score'] > 2000]
    print(f"High scorers (>2000): {high_scores}")

    doubled_scores = [players[player]['score'] * 2 for player in players]
    print(f"Scores doubled: {doubled_scores}")

    active = [player for player in players if players[player]['active']]
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {player: players[player]['score'] for player in players}
    print(f"Player scores: {player_scores}")

    score_categories = {'high': len([player for player in players
                                     if players[player]['score'] >= 2100]),
                        'medium': len([player for player in players
                                       if 1800
                                       <= players[player]['score']
                                       < 2100]),
                        'low': len([player for player in players
                                    if players[player]['score'] < 1800])}
    print(f"Score categories: {score_categories}")

    achievement_counts = {player: len(players[player]['achievement'])
                          for player in players}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {player for player in players}
    print(f"Unique players: {unique_players}")

    unique_achievement = {achievement
                          for player in players
                          for achievement in players[player]['achievement']}
    print(f"Unique achievement: {unique_achievement}")

    active_regions = {players[player]['region']
                      for player in players
                      if players[player]['active']}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len(unique_players)
    print(f"Total players: {total_players}")

    total_achievements = sum(achievement_counts.values())
    print(f"Total unique achievements: {total_achievements}")

    average_score = sum(player_scores.values()) / len(player_scores)
    print(f"Average score: {average_score}")

    top_perf = max(player_scores, key=lambda x: player_scores[x])
    print(f"Top performer: {top_perf} "
          f"({player_scores[top_perf]} points, "
          f"{achievement_counts[top_perf]} achievements)")


if __name__ == "__main__":
    main()
