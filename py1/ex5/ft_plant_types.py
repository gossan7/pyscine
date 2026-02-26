#!/usr/bin/env python3

class Plant():
    """Base class representing a plant with common attributes."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant.

        Args:
            name: The name of the plant.
            height: The height in centimeters.
            age: The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.days = age

    def __str__(self) -> str:
        return f"{self.name} ({self.__class__.__name__}): " + \
            f"{self.height}cm, {self.days} days"


class Flower(Plant):
    """Represents a flower with a specific color."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a Flower.

        Args:
            name: The name of the flower.
            height: The height in centimeters.
            age: The age of the flower in days.
            color: The color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display a blooming message for the flower."""
        print(self.name, "is blooming beautifully!")

    def __str__(self) -> str:
        return super().__str__() + self.get_characteristic()

    def get_characteristic(self) -> str:
        """Get the flower's characteristic.

        Returns:
            A string describing the flower's color.
        """
        return f", {self.color} color"


class Tree(Plant):
    """Represents a tree with a trunk diameter."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a Tree.

        Args:
            name: The name of the tree.
            height: The height in centimeters.
            age: The age of the tree in days.
            trunk_diameter: The diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def shade(self) -> None:
        """Calculate and display the shade area provided by the tree."""
        shade = ((self.height * self.trunk_diameter) / 1000) * 3
        print(f"{self.name} provides {shade:.0f} square meters of shade")

    def __str__(self) -> str:
        return super().__str__() + self.get_characteristic()

    def get_characteristic(self) -> str:
        """Get the tree's characteristic.

        Returns:
            A string describing the tree's trunk diameter.
        """
        return f", {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Represents a vegetable with harvest season and nutritional value."""

    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """Initialize a Vegetable.

        Args:
            name: The name of the vegetable.
            height: The height in centimeters.
            age: The age of the vegetable in days.
            harvest_season: The season when the vegetable is harvested.
            nutritional_value: The primary nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_nutrition(self) -> None:
        """Display the vegetable's nutritional value."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def __str__(self) -> str:
        return super().__str__() + self.get_characteristic()

    def get_characteristic(self) -> str:
        """Get the vegetable's characteristic.

        Returns:
            A string describing the vegetable's harvest season.
        """
        return f", {self.harvest_season} harvest"


def main() -> None:
    """Main function demonstrating garden plant types."""

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Sunflower", 80, 45, "yellow")
    ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 620, 2100, 45)
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 75, "autumn", "vitamin A")
    ]

    print("=== Garden Plant Types ===")

    print("\n=== Flowers ===")
    for flower in flowers:
        print(flower)
        flower.bloom()
        print()

    print("\n=== Trees ===")
    for tree in trees:
        print(tree)
        tree.shade()
        print()

    print("\n=== Vegetables ===")
    for vegetable in vegetables:
        print(vegetable)
        vegetable.print_nutrition()
        print()


if __name__ == "__main__":
    main()
