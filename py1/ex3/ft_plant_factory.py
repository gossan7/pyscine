#!/usr/bin/env python3

class Factory:
    """Factory class for creating and managing plant instances."""

    def __init__(self):
        """Initialize a Factory with an empty plant list."""
        self.plants = []

    def create_plants(self, args: tuple) -> list:
        """Create multiple plants from a tuple of plant data.

        Args:
            args: A tuple of tuples, each containing (name, height, age).

        Returns:
            A list of created Plant instances.
        """
        self.plants = []
        for arg in args:
            self.plants.append(Plant(*arg))
        return self.plants


class Plant:
    """Represents a plant with name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant.

        Args:
            name: The name of the plant.
            height: The initial height in centimeters.
            age: The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.days = age
        print(f"Created: {name} ({height}cm, {age} days)")

    def age(self, n: int) -> None:
        """Age the plant by a number of days and grow accordingly.

        Args:
            n: The number of days to age the plant.
        """
        self.days += n
        self.grow(n)

    def grow(self, n: int) -> None:
        """Grow the plant by a specified amount.

        Args:
            n: The amount to grow in centimeters.
        """
        self.height += n

    def get_info(self) -> tuple:
        """Get the plant's information.

        Returns:
            A tuple containing (name, height, days).
        """
        return ((self.name, self.height, self.days))


def main():
    """Main function demonstrating the Plant Factory."""
    print("=== Plant Factory Output ===")
    facto = Factory()
    plants = facto.create_plants((("Rose", 25, 30),
                                  ("Oak", 200, 365),
                                  ("Cactus", 15, 120),
                                  ("Sunflower", 80, 45),
                                  ("Fern", 15, 120)))
    print("\nTotal plants created:", len(plants))


if __name__ == "__main__":
    main()
