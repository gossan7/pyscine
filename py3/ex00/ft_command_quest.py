#!/usr/bin/env python3
import sys


def main():
    print("=== Command Quest ===")
    size = len(sys.argv)
    if size == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if size > 1:
        print(f"Arguments received: {size - 1}")
    i = 0
    for arg in sys.argv[1:]:
        print(f"Argument {i + 1}: {arg}")
        i += 1
    print(f"Total arguments: {size}")


if __name__ == "__main__":
    main()
