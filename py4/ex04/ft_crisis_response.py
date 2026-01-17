#!/usr/bin/env python3

def crisis_handler(file_name: str):
    """
    Handle file access in a crisis-safe manner.

    Attempts to open a file and reports status based on outcome:
    - FileNotFoundError: logs missing archive alert.
    - PermissionError: logs security protocol violation.
    - Other exceptions: logs unexpected system anomaly.
    - Successful access: confirms normal operations.

    Args:
        file_name (str): Name of the file to access.
    """
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")

    try:
        with open(file_name, "r") as archive:
            content = archive.read().strip()
        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly - {e}")
        print("STATUS: Crisis handled, system stable\n")


def main():
    """
    Simulate crisis response operations in the Cyber Archives.

    This function attempts access to several archive files, handling
    missing files, security restrictions, and normal archive recovery.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    test_files = [
        "lost_archive.txt",
        "classified_data.txt",
        "standard_archive.txt"
    ]

    for file in test_files:
        crisis_handler(file)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
