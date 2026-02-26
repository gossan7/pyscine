#!/usr/bin/env python3

class Plant:
    """Represents a plant with basic garden information."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.days = age


def main() -> None:
    """Main function demonstrating the Garden Data."""
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}:", f"{plant.height}cm,",
              f"{plant.days} days old")


if __name__ == "__main__":
    main()
