#!/usr/bin/env python3

class SecurePlant():
    def __init__(self, name: str, height: int, age: int) -> None:
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
        if (new_height < 0):
            print(f"Invalid operation attempted: height {new_height}cm",
                  "[REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = new_height
        print(f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age) -> None:
        if (new_age < 0):
            print(f"Invalid operation attempted: age {new_age} days",
                  "[REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__days = new_age
        print(f"Age updated: {new_age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__days

    def get_name(self) -> str:
        return self.__name


def main():
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
