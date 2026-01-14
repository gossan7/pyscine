#!/usr/bin/env python3

def check_temperature(temp_str: str):
    try:
        n = int(temp_str)
        if n > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
            return None
        elif n < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
            return None
        else:
            print(f"Temperature {temp_str}°C is perfect for plants!")
        return n
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]
    for test in tests:
        print(f"\nTesting temperature: {test}")
        check_temperature(test)


if __name__ == "__main__":
    test_temperature_input()
