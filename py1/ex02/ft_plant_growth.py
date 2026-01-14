#!/usr/bin/env python3

class Plant:
    """Represents a plant with basic garden information."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.days = age

    def age(self, n: int) -> None:
        """Increase plant age by n days and grow height by n cm."""
        self.days += n
        self.grow(n)

    def grow(self, n: int) -> None:
        """Increase plant height by n cm."""
        self.height += n

    def get_info(self) -> tuple:
        """Return the plant's current name, height, and age."""
        return ((self.name, self.height, self.days))


def main():
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
