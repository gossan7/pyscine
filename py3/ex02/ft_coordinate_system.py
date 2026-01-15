#!/usr/bin/env python3
import sys
import math


def print_pos(x: int, y: int, z: int):
    """
    Display a player's position in 3D space.

    Args:
        x (int): X coordinate.
        y (int): Y coordinate.
        z (int): Z coordinate.
    """
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main():
    """
    Parse command-line arguments and compute 3D coordinates.

    This function accepts coordinates either as three separate
    command-line arguments or as a single quoted string.
    It validates the input, computes the distance from the
    origin, and demonstrates tuple unpacking.
    """
    print("=== Game Coordinate System ===\n")
    size = len(sys.argv)

    if size == 2:
        args = sys.argv[1].split(" ")
        if len(args) != 3:
            print(
                "Invalid args. Usage: python3 ft_coordinate_system.py x y z"
                " / \"x y z\""
            )
    elif size == 4:
        args = sys.argv[1:]
    else:
        print(
            "Invalid args. Usage: python3 ft_coordinate_system.py x y z"
            " / \"x y z\""
        )
        return

    try:
        print(f"Parsing coordinates: {args}")
        new_pos = tuple(int(arg) for arg in args)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(
            f"Error details - Type: {e.__class__.__name__}, "
            f"Args: (\"{e}\")"
        )
        return

    print(f"Parsed position: {new_pos}")
    base_pos = (0, 0, 0)

    distance = math.sqrt(
        (base_pos[0] - new_pos[0]) ** 2 +
        (base_pos[1] - new_pos[1]) ** 2 +
        (base_pos[2] - new_pos[2]) ** 2
    )

    print(f"Distance between {base_pos} ans {new_pos}: {distance:.2f}\n")

    print("Unpacking demonstration:")
    print_pos(*new_pos)


if __name__ == "__main__":
    main()
