#!/usr/bin/env python3

def water_plants(plant_list: list):
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
    print("=== Garden Watering System ===")
    valid_plant_list = ["tomato", "lettuce", "carrots"]
    invalid_plant_list = ["tomato", None]
    print("\nTesting normal watering...")
    water_plants(valid_plant_list)
    print("\nTesting with error...")
    water_plants(invalid_plant_list)
    print("\nCleanup alway happens, even with errors")


if __name__ == "__main__":
    test_watering_system()
