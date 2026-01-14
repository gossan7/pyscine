#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self):
        super().__init__("Plant name cannot be empty!")


class WaterError(Exception):
    def __init__(self, water_level: int):
        too_high = f"Water level {water_level} is too high (max 10)"
        too_low = f"Water level {water_level} is too low (min 1)"
        super().__init__(too_high if water_level > 10 else too_low)


class SunlightError(Exception):
    def __init__(self, sunlight_hours: int):
        too_high = f"Water level {sunlight_hours} is too high (max 12)"
        too_low = f"Water level {sunlight_hours} is too low (min 2)"
        super().__init__(too_high if sunlight_hours > 12 else too_low)


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if len(plant_name) == 0:
        raise PlantError
    if water_level < 1 or water_level > 10:
        raise WaterError(water_level)
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise SunlightError(sunlight_hours)
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
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
