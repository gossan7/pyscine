#!/usr/bin/env python3

def water_plants(plant_list: list):
    """
    Simulate watering a list of plants.

    This function attempts to water each plant in the provided list.
    It demonstrates the use of try, except, and finally blocks to
    handle errors and ensure cleanup operations are always executed.

    Args:
        plant_list (list): A list containing plant identifiers.

    Returns:
        bool: True if watering completes successfully, False otherwise.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            print(f"Watering {plant[0:]}")
    except Exception:
        print(f"Error: Cannot water {plant} - invalid plant!")
        return False
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")
    return True


def test_watering_system():
    """
    Test the garden watering system with valid and invalid plant lists.

    This function demonstrates how the watering system behaves
    during normal operation and when an error occurs.
    """
    print("=== Garden Watering System ===")
    valid_plant_list = ["tomato", "lettuce", "carrots"]
    invalid_plant_list = ["tomato", None]
    print("\nTesting normal watering...")
    water_plants(valid_plant_list)
    print("\nTesting with error...")
    water_plants(invalid_plant_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
