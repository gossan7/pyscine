#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.days = age

    def print_infos(self) -> None:
        print(self.name, f"({self.__class__.__name__}):",
              f"{self.height}cm,", f"{self.days} days,",
              self.get_characteristic())

    def get_characteristic(self) -> str:
        return None


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(self.name, "is blooming beautifully!")

    def get_characteristic(self) -> str:
        return f"{self.color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def shade(self):
        shade = ((self.height * self.trunk_diameter) / 1000) * 3
        print(f"{self.name} provides {shade:.0f} square meters of shade")

    def get_characteristic(self) -> str:
        return f"{self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_characteristic(self) -> str:
        return f"{self.harvest_season} harvest"


def main() -> None:
    flowers = [Flower("Rose", 25, 30, "red"),
               Flower("Sunflower", 80, 45, "yellow")]
    trees = [Tree("Oak", 500, 1825, 50),
             Tree("Pine", 620, 2100, 45)]
    vegetables = [Vegetable("Tomato", 80, 90, "summer", "vitamin c"),
                  Vegetable("Carrot", 30, 75, "autumn", "vitamin a")]
    print("=== Garden Plant Types ===")
    print("\n=== Flowers ===")
    for flower in flowers:
        flower.print_infos()
        flower.bloom()
        print()
    print("\n=== Trees ===")
    for tree in trees:
        tree.print_infos()
        tree.shade()
        print()
    print("\n=== Vegetables ===")
    for vegetable in vegetables:
        vegetable.print_infos()
        vegetable.print_nutrition()
        print()


if __name__ == "__main__":
    main()
