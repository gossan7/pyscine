#!/usr/bin/env python3

def main() -> None:
    """
    Demonstrate secure vault operations in the Cyber Archives.

    This function:
    1. Uses the 'with' statement to safely read from a classified vault file.
    2. Uses the 'with' statement to safely write new security protocols to a
    vault file.
    3. Ensures that all vaults are automatically sealed after operations.
    4. Logs every step of the secure extraction and preservation process.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    try:
        with open("classified_data.txt", "r") as vault:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            for line in vault:
                print(f"[CLASSIFIED] {line}", end="")

    except FileNotFoundError as e:
        print(f"Error: {e}")

    print("\n\nSECURE PRESERVATION:")
    try:
        with open("security_protocols.txt", "w") as vault:
            vault.write("New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")

    except FileNotFoundError as e:
        print(f"Error: {e}")

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
