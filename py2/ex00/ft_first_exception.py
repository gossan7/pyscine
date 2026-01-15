#!/usr/bin/env python3

def check_temperature(temp_str: str):
    """
    Check whether a temperature value is valid for plants.

    The function attempts to convert the input string to an integer.
    It prints an error message if the value is not a number or if the
    temperature is outside the acceptable range (0–40°C).

    Args:
        temp_str (str): The temperature value as a string.

    Returns:
          int | None: The temperature as an integer if valid, otherwise None.
    """
    try:
        n = int(temp_str)
        if n > 40:
            print(f"Error: {n}°C is too hot for plants (max 40°C)")
            return None
        elif n < 0:
            print(f"Error: {n}°C is too cold for plants (min 0°C)")
            return None
        else:
            print(f"Temperature {n}°C is perfect for plants!")
        return n
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input():
    """
    Test the check_temperature function with predefined values.

    This function simulates different temperature inputs to demonstrate
    how check_temperature handles valid and invalid cases.
    """
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]
    for test in tests:
        print(f"\nTesting temperature: {test}")
        check_temperature(test)
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
