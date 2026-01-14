#!/usr/bin/env python3
import sys


def main():
    print("=== Player Score Analytics ===")
    players = len(sys.argv) - 1
    if players == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return
    try:
        scores = [int(arg) for arg in sys.argv[1:]]
    except Exception as e:
        print(f"Error in args: {e}")
        return
    print(f"Total players: {players}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / players:.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
