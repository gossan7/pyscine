#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class PlantError(GardenError):
    def __init__(self, plant: str):
        super().__init__(f"The {plant} is wilting")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank")


def plant_error():
    raise PlantError("tomato")


def water_error():
    raise WaterError


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
