#!/usr/bin/env python3


def main():
    """
    Create a new archive file 'new_discovery.txt' and inscribe
    three preservation entries. Display a log of the creation
    and inscription process to the terminal, then close the file
    to seal the archive.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    file_name = "new_discovery.txt"
    strings = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]

    print(f"Initializing new storage unit: {file_name}")
    try:
        file = open(file_name, "w")
    except OSError as e:
        print(f"ERROR: Could not create archive '{file_name}': {e}")
        return
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")
    for string in strings:
        print(string)
        file.write(string + "\n")

    file.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
