#!/usr/bin/env python3

def garden_operations(flag="All"):
    """
    Trigger specific Python exceptions based on the provided flag.

    Depending on the flag value, this function deliberately raises
    common Python errors for demonstration and testing purposes.

    Args:
        flag (str): The name of the exception to trigger.
            Supported values are:
            - "ValueError"
            - "ZeroDivisionError"
            - "FileNotFoundError"
            - "KeyError"
            - "All" (default): triggers all errors sequentially
    """
    match flag:
        case "ValueError":
            int("abc")
        case "ZeroDivisionError":
            42 / 0
        case "FileNotFoundError":
            open("missing.txt")
        case "KeyError":
            dictionnary = {"key": "value"}
            dictionnary["missing_plant"]
        case "All":
            int("abc")
            42 / 0
            open("inexistent_file")
            dictionnary = {"key": "value"}
            dictionnary["inexistent_key"]


def test_error_types():
    """
    Test and demonstrate handling of multiple Python exception types.

    This function calls garden_operations with different flags,
    catches the raised exceptions, and confirms that the program
    continues running after each error.
    """
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
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
