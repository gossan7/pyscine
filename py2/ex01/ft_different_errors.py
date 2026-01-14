#!/usr/bin/env python3

def garden_operations(flag="All"):
    match flag:
        case "ValueError":
            int("abc")
        case "ZeroDivisionError":
            42 / 0
        case "FileNotFoundError":
            open("inexistent_file")
        case "KeyError":
            dictionnary = {"key": "value"}
            dictionnary["inexistent_key"]
        case "All":
            int("abc")
            42 / 0
            open("inexistent_file")
            dictionnary = {"key": "value"}
            dictionnary["inexistent_key"]


def test_error_types():
    print("=== Garden Error Types Demo ===")

    tests = ["ValueError", "ZeroDivisionError",
             "FileNotFoundError", "KeyError"]

    for test in tests:
        print(f"\nTesting {test}...")
        try:
            garden_operations(test)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, KeyError) as e:
            print(f"Caught {test}: {e}")

    print("\nTesting multiple errors together")
    try:
        garden_operations()
    except (ValueError, ZeroDivisionError,
            FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully")


if __name__ == "__main__":
    test_error_types()
