#!/usr/bin/env python3

class SecurePlant():
    """Represents a plant with secure, validated attributes."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a SecurePlant with validation.

        Args:
            name: The name of the plant.
            height: The initial height in centimeters (set to 0 if negative).
            age: The age of the plant in days (set to 0 if negative).
        """
        if height < 0:
            print(f"Invalid start height: {height}cm, was set to 0")
            height = 0
        if age < 0:
            age = 0
            print(f"Invalid start age: {age}cm, was set to 0")
        self.__name = name
        self.__height = height
        self.__days = age
        print(f"Plant created: {name}")

    def set_height(self, new_height) -> None:
        """Set the plant's height with validation.

        Args:
            new_height: The new height in centimeters (rejected if negative).
        """
        if (new_height < 0):
            print(f"Invalid operation attempted: height {new_height}cm",
                  "[REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = new_height
        print(f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age) -> None:
        """Set the plant's age with validation.

        Args:
            new_age: The new age in days (rejected if negative).
        """
        if (new_age < 0):
            print(f"Invalid operation attempted: age {new_age} days",
                  "[REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__days = new_age
        print(f"Age updated: {new_age} days [OK]")

    def get_height(self) -> int:
        """Get the plant's current height.

        Returns:
            The height in centimeters.
        """
        return self.__height

    def get_age(self) -> int:
        """Get the plant's current age.

        Returns:
            The age in days.
        """
        return self.__days

    def get_name(self) -> str:
        """Get the plant's name.

        Returns:
            The name of the plant.
        """
        return self.__name


def main():
    """Main function demonstrating the Garden Security System."""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 0, 0)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    print(f"Current plant: {rose.get_name()}",
          f"({rose.get_height()}cm, {rose.get_age()} days)")


if __name__ == "__main__":
    main()
