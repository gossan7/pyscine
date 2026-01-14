#!/usr/bin/env python3

class Factory:
    

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
    plants = [Plant("Rose", 25, 30),
              Plant("Oak", 200, 365),
              Plant("Cactus", 15, 120),
              Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120)]
    lenght = 0
    for _ in plants:
        lenght += 1
    print("\nTotal plants created:", lenght)


if __name__ == "__main__":
    main()
