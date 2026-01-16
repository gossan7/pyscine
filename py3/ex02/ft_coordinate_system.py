#!/usr/bin/env python3
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


def parse_coordinates(coordinates_string: str):
    """
    Parse a player's coordinate string.

    Args:
        coordinates_string (str): coordinates string separated by a comma.
    """
    coordinates = tuple(map(int, coordinates_string.split(",")))
    return coordinates


def calc_distance(base: tuple[int, int, int], pos: tuple[int, int, int]):
    """
    Calculate distance between two 3D points (coordinates)

    Args:
        base (tuple): base position (usually (0, 0, 0))
        pos (tuple): player's position
    """
    distance = math.sqrt(
        (base[0] - pos[0]) ** 2 +
        (base[1] - pos[1]) ** 2 +
        (base[2] - pos[2]) ** 2
    )
    return distance


def main():
    """
    Parse command-line arguments and compute 3D coordinates.

    This function accepts coordinates either as three separate
    command-line arguments or as a single quoted string.
    It validates the input, computes the distance from the
    origin, and demonstrates tuple unpacking.
    """
    print("=== Game Coordinate System ===\n")

    base_coordinates = (0, 0, 0)

    valid_coordinates = (10, 20, 5)
    print(f"Position created: {valid_coordinates}")
    print(f"Distance between {base_coordinates} and {valid_coordinates}:",
          f"{calc_distance(base_coordinates, valid_coordinates):.2f}")
    print()

    valid_coordinates_str = "3,4,0"
    invalid_coordinates_str = "abc,def,ghi"

    try:
        print(f"Parsing coordinates: \"{valid_coordinates_str}\"")

        pos1 = parse_coordinates(valid_coordinates_str)
        print(f"Parsed position: {pos1}")
        print(f"Distance between {base_coordinates} and {pos1}:",
              f"{calc_distance(base_coordinates, pos1):.1f}")
        print()

        print(f"Parsing invalid coordinates: \"{invalid_coordinates_str}\"")

        pos2 = parse_coordinates(invalid_coordinates_str)
        print(f"Parsed position: {pos2}")
        print(f"Distance between {base_coordinates} and {pos2}:",
              f"{calc_distance(base_coordinates, pos2):.1f}")
        print()

    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(
            f"Error details - Type: {e.__class__.__name__}, "
            f"Args: ({repr(str(e))},)"
        )
        print()

    print("Unpacking demonstration:")
    pos1 = (3, 4, 0)
    print_pos(*pos1)


if __name__ == "__main__":
    main()
