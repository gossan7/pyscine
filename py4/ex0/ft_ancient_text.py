#!/usr/bin/env python3


def main() -> None:
    """
    Recover and display the contents of an ancient text fragment.

    This function attempts to open the file 'ancient_fragment.txt',
    simulating access to a secure storage vault. If the file exists,
    its contents are read and displayed line by line, then the
    connection is properly closed. If the file does not exist, an
    appropriate error message is shown.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file_name = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file_name}")
    try:
        file = open(file_name)
        print("Connection established...\n")

        print("RECOVERED DATA:")
        for line in file:
            print(line, end="")

        file.close()
        print("\n\nData recovery complete. Storage unit disconnected.")

    except Exception:
        print("ERROR: Storage vault not found.",
              "Run data generator first.")
        return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
