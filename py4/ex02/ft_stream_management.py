#!/usr/bin/env python3
import sys


def main():
    """
    Demonstrate three-channel communication in the Cyber Archives.

    This function:
    1. Displays a system header.
    2. Collects input from the archivist (ID and status report) using stdin.
    3. Outputs standard messages via sys.stdout.
    4. Outputs alerts via sys.stderr.
    5. Confirms successful communication across all three channels.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {archivist_id}: {status_report}",
          file=sys.stdout)

    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)

    print("[STANDARD] Data transmission complete", file=sys.stdout)

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
