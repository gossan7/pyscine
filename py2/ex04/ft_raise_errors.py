#!/usr/bin/env python3

class PlantError(Exception):
    """
    Exception raised when a plant name is invalid.
    """
    def __init__(self, plant):
        if not isinstance(plant, str):
            msg = "Plant name has to be a string!"
        elif len(str) == 0:
            msg = "Plant name cannot be empty!"
        else:
            msg = "Plant error!"
        super().__init__(msg)


class WaterError(Exception):
    """
    Exception raised when the water level is outside the valid range.

    Args:
        water_level (int): The provided water level value.
    """
    def __init__(self, water_level: int):
        too_high = f"Water level {water_level} is too high (max 10)"
        too_low = f"Water level {water_level} is too low (min 1)"
        super().__init__(too_high if water_level > 10 else too_low)


class SunlightError(Exception):
    """
    Exception raised when the sunlight exposure is outside
    the acceptable range.

    Args:
        sunlight_hours (int): Number of sunlight hours provided.
    """
    def __init__(self, sunlight_hours: int):
        too_high = f"Sunlight level {sunlight_hours} is too high (max 12)"
        too_low = f"Sunlight level {sunlight_hours} is too low (min 2)"
        super().__init__(too_high if sunlight_hours > 12 else too_low)


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    """
    Validate plant health conditions.

    This function checks the plant name, water level,
    and sunlight exposure. It raises specific custom
    exceptions if any condition is invalid.

    Args:
        plant_name (str): Name of the plant.
        water_level (int): Water level provided.
        sunlight_hours (int): Hours of sunlight exposure.

    Returns:
        str: A confirmation message if all checks pass.

    Raises:
        PlantError: If the plant name is empty.
        WaterError: If the water level is invalid.
        SunlightError: If the sunlight hours are invalid.
    """
    if len(plant_name) == 0:
        raise PlantError
    if water_level < 1 or water_level > 10:
        raise WaterError(water_level)
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise SunlightError(sunlight_hours)
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """
    Test plant health validation with multiple scenarios.

    This function demonstrates how different invalid
    inputs trigger specific custom exceptions.
    """
    print("=== Garden Plant Health Checker ===")
    tests = [("Testing with good values...", ["tomato", 5, 6]),
             ("Testing empty plant name...", ["", 5, 6]),
             ("Testing bad water level...", ["tomato", 15, 6]),
             ("Testing bad sunlight hours...", ["tomato", 5, 0])]
    for message, args in tests:
        print(f"\n{message}")
        try:
            print(check_plant_health(*args))
        except Exception as e:
            print(f"Error: {e}")
    print("\nAll error raisong tests completed!")


if __name__ == "__main__":
    test_plant_checks()
