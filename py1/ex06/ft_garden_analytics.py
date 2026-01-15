#!/usr/bin/env python3
"""Garden Analytics Platform."""


class Plant:
    """Base class representing a plant."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a Plant.

        Args:
            name: The name of the plant.
            height: The initial height in centimeters.
        """
        if not GardenManager.validate_height(height):
            print(f"Invalid height during construction ({height}) "
                  f"for {name}, setting it to 0")
            height = 0
        self.name = name
        self.height = height

    def grow(self, n: int = 1) -> None:
        """Grow the plant by a specified amount.

        Args:
            n: The amount to grow in centimeters.
        """
        if not GardenManager.validate_height(n):
            print(f"Invalid height: {n}")
        else:
            self.height += n
            print(f"{self.name} grew {n}cm")

    def info(self) -> str:
        """Return a string representation of the plant.

        Returns:
            A formatted string with plant's name and height.
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A plant that produces flowers."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a FloweringPlant.

        Args:
            name: The name of the plant.
            height: The initial height in centimeters.
            color: The color of the flowers.
        """
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def info(self) -> str:
        """Return a string representation of the flowering plant.

        Returns:
            A formatted string with plant details including flower color.
        """
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """A flowering plant that has won prizes."""

    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        """Initialize a PrizeFlower.

        Args:
            name: The name of the plant.
            height: The initial height in centimeters.
            color: The color of the flowers.
            points: The number of prize points.
        """
        super().__init__(name, height, color)
        self.points = points

    def info(self) -> str:
        """Return a string representation of the prize flower.

        Returns:
            A formatted string with plant details including prize points.
        """
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.points}")


class Garden:
    """Represents a garden containing a collection of plants."""

    def __init__(self, owner: str) -> None:
        """Initialize a Garden.

        Args:
            owner: The name of the garden's owner.
        """
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden.

        Args:
            plant: The plant to add to the garden.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, n: int = 1) -> None:
        """Grow all plants in the garden by a specified amount.

        Args:
            n: The amount to grow each plant in centimeters.
        """
        print(f"{self.owner} is helping all plants grow...")
        if not GardenManager.validate_height(n):
            print(f"Invalid height: {n}")
        else:
            for p in self.plants:
                p.grow(n=n)
                self.total_growth += n

    def generate_report(self, manager: 'GardenManager') -> None:
        """Generate and print a comprehensive report about the garden.

        Args:
            manager: The GardenManager instance to use for statistics.
        """
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p.info()}")
        print()
        stats = manager.GardenStats(self)
        type_counts = stats.count_types()
        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {type_counts['regular']} regular, "
              f"{type_counts['flowering']} flowering, "
              f"{type_counts['prize']} prize flowers")
        test_height = self.plants[0].height if self.plants else 0
        print()
        print("Height validation test:", manager.validate_height(test_height))


class GardenManager:
    """Manages multiple gardens and provides analytics capabilities."""

    total_gardens = 0

    class GardenStats:
        """Nested helper class for calculating garden statistics."""

        def __init__(self, garden: Garden) -> None:
            """Initialize GardenStats for a specific garden.

            Args:
                garden: The garden to analyze.
            """
            self.garden = garden

        def count_types(self) -> dict:
            """Count the number of each type of plant in the garden.

            Returns:
                A dictionary with counts for plant types.
            """
            types = {"regular": 0, "flowering": 0, "prize": 0}
            for p in self.garden.plants:
                if isinstance(p, PrizeFlower):
                    types["prize"] += 1
                elif isinstance(p, FloweringPlant):
                    types["flowering"] += 1
                else:
                    types["regular"] += 1
            return types

        def garden_score(self) -> int:
            """Calculate the total score for the garden.

            Returns:
                The total garden score.
            """
            score = 0
            for p in self.garden.plants:
                score += p.height
                if isinstance(p, PrizeFlower):
                    score += p.points
            return score

    def __init__(self) -> None:
        """Initialize a GardenManager with an empty garden collection."""
        self.gardens = dict()

    def add_garden(self, garden: Garden) -> None:
        """Add a garden to the manager's collection.

        Args:
            garden: The garden to add.
        """
        self.gardens[garden.owner] = garden
        GardenManager.total_gardens += 1

    @staticmethod
    def validate_height(h: int) -> bool:
        """Validate that a height value is valid.

        Args:
            h: The height value to validate.

        Returns:
            True if the height is valid, False otherwise.
        """
        return isinstance(h, (int, float)) and h >= 0

    @classmethod
    def create_garden_network(cls, owners: tuple) -> 'GardenManager':
        """Create a new GardenManager with gardens for each owner.

        Args:
            owners: A tuple of owner names.

        Returns:
            A new GardenManager instance with gardens.
        """
        manager = cls()
        for owner in owners:
            manager.add_garden(Garden(owner))
        return manager


def main() -> None:
    """Main function demonstrating the Garden Analytics Platform."""
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network(("Alice",
                                                   "Bob"))

    manager.gardens["Alice"].add_plant(Plant("Oak Tree",
                                             100))

    manager.gardens["Alice"].add_plant(FloweringPlant("Rose",
                                                      25,
                                                      "red"))

    manager.gardens["Alice"].add_plant(PrizeFlower("Sunflower",
                                                   50,
                                                   "yellow",
                                                   10))

    print()
    manager.gardens["Alice"].grow_all()
    print()
    manager.gardens["Alice"].generate_report(manager)

    alice_score = manager.GardenStats(manager.gardens["Alice"]).garden_score()
    bob_score = manager.GardenStats(manager.gardens["Bob"]).garden_score()
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
