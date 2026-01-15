#!/usr/bin/env python3

class GardenError(Exception):
    """
    Base exception class for garden-related errors.

    All custom garden exceptions should inherit from this class.
    """
    def __init__(self, *args):
        super().__init__(*args)


class PlantError(GardenError):
    """
    Exception raised when a plant-related issue occurs.

    Args:
        plant (str): The name of the affected plant.
    """
    def __init__(self, plant: str):
        super().__init__(f"The {plant} is wilting")


class WaterError(GardenError):
    """
    Exception raised when there is a water supply issue.
    """
    def __init__(self):
        super().__init__("Not enough water in the tank")


def plant_error():
    """
    Raise a PlantError for demonstration purposes.
    """
    raise PlantError("tomato")


def water_error():
    """
    Raise a WaterError for demonstration purposes.
    """
    raise WaterError


def test_custom_errors():
    """
    Demonstrate custom garden exception handling.

    This function raises and catches different custom exceptions,
    showing both specific and base-class error handling.
    """
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
