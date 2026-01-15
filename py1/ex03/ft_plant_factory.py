#!/usr/bin/env python3

class Factory:
    def __init__(self):
        self.plants = []

    def create_plants(self, args: tuple) -> list:
        self.plants = []
        for arg in args:
            self.plants.append(Plant(*arg))
        return self.plants


class Plant:
    """Represents a plant with name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.days = age
        print(f"Created: {name} ({height}cm, {age} days)")

    def age(self, n: int) -> None:
        self.days += n
        self.grow(n)

    def grow(self, n: int) -> None:
        self.height += n

    def get_info(self) -> tuple:
        return ((self.name, self.height, self.days))


def main():
    print("=== Plant Factory Output ===")
    facto = Factory()
    plants = [facto.create_plants(("Rose", 25, 30),
              ("Oak", 200, 365),
              ("Cactus", 15, 120),
              ("Sunflower", 80, 45),
              ("Fern", 15, 120))]
    print("\nTotal plants created:", len(plants))


if __name__ == "__main__":
    main()
