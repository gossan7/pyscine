#!/usr/bin/env python3

class Plant:
    """Represents a plant with basic garden information."""

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

    def get_info(self) -> tuple[str, int, int]:
        """Get the plant's information.

        Returns:
            A tuple containing (name, height, days).
        """
        return ((self.name, self.height, self.days))


def main() -> None:
    """Main function demonstrating the Plant Growth."""
    rose = Plant("Rose", 25, 30)
    day_1 = rose.get_info()
    print("=== Day 1 ===")
    print(f"{day_1[0]}:", f"{day_1[1]}cm,", f"{day_1[2]} days old")
    rose.age(6)
    day_7 = rose.get_info()
    print("=== Day 7 ===")
    print(f"{day_7[0]}:", f"{day_7[1]}cm,", f"{day_7[2]} days old")
    print(f"Growth this week: {day_7[1] - day_1[1]:+}cm")


if __name__ == "__main__":
    main()
