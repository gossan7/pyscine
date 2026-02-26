#!/usr/bin/env python3

class GardenError(Exception):
    """
    Base exception class for all garden-related errors.

    This class allows grouping all custom garden exceptions
    under a common parent type.
    """

    def __init__(self, *args) -> None:
        super().__init__(*args)


class PlantError(GardenError):
    """
    Exception raised when a plant name is invalid.
    """

    def __init__(self, plant) -> None:
        if not isinstance(plant, str):
            msg = "Plant name has to be a string!"

        elif len(plant) == 0:
            msg = "Plant name cannot be empty!"

        else:
            msg = "Plant error!"

        super().__init__(msg)


class WaterError(GardenError):
    """
    Exception raised when the water level is outside the valid range.

    Args:
        water_level (int): The provided water level value.
    """

    def __init__(self, water_level: int) -> None:
        too_high = f"Water level {water_level} is too high (max 10)"
        too_low = f"Water level {water_level} is too low (min 1)"
        super().__init__(too_high if water_level > 10 else too_low)


class GardenManager:
    """
    Manage plants and their care within a garden system.

    This class allows adding plants, watering them, and
    checking their health while handling possible errors.
    """

    def __init__(self) -> None:
        """
        Initialize an empty garden manager.
        """
        self.plants: dict[str, dict[str, int]] = dict()

    def add_plants(self, plants: list[str]) -> None:
        """
        Add a list of plants to the garden.

        Each plant must be a non-empty string. Invalid plants
        raise a PlantError and stop the addition process.

        Args:
            plants (list): List of plant names.
        """
        try:
            for plant in plants:
                if not isinstance(plant, str) or len(plant) == 0:
                    raise PlantError(plant)

                self.plants[plant] = {"water": 0, "sun": 8}
                print(f"Added {plant} successfully")

        except Exception as e:
            print("Error adding plant:", e)

    def water_plants(self, watering: dict[str, int]) -> None:
        """
        Water plants according to the provided watering plan.

        Demonstrates use of try / except / finally to ensure
        cleanup always occurs.

        Args:
            watering (dict): Mapping of plant names to water amounts.
        """
        print("Opening watering system")
        try:
            for plant in watering:
                self.plants[plant]["water"] += watering[plant]
                print(f"Watering {plant} - success")
            return

        except Exception as e:
            print("Error watering plants:", e)
            return

        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        """
        Check the health status of all plants in the garden.

        Raises a WaterError if any plant has an invalid water level.
        """
        try:
            for plant in self.plants:
                if not self.plants[plant]["water"] - 1 in range(10):
                    raise WaterError(self.plants[plant]["water"])

                print(
                    f"{plant}: healthy "
                    f"(water: {self.plants[plant]['water']}, "
                    f"sun: {self.plants[plant]['sun']})"
                )

        except Exception as e:
            print(f"Error checking {plant}: {e}")


def test_garden_management() -> None:
    """
    Demonstrate the garden management system behavior.

    This function tests plant addition, watering,
    health checks, and error recovery.
    """
    manager = GardenManager()

    print("=== Garden Management System ===")
    print()
    print("Adding plants to garden...")

    manager.add_plants(["tomato", "lettuce", ""])

    print()
    print("Watering plants...")

    manager.water_plants({"tomato": 5, "lettuce": 15})

    print()
    print("Checking plant health...")

    manager.check_health()

    print()
    print("Testing error recovery...")

    try:
        raise WaterError(0)

    except GardenError:
        print("Caught GardenError: Not enough water in tank")

    finally:
        print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    try:
        test_garden_management()

    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
