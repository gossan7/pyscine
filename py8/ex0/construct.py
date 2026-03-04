import sys
import os
import site


def in_virtualenv() -> bool:
    """
    Determine whether the current Python interpreter is running
    inside a virtual environment.

    Returns:
        bool: True if a virtual environment is active, False otherwise.

    This function compares sys.prefix (the active environment prefix)
    with sys.base_prefix (the base Python installation prefix).
    If they differ, a virtual environment is assumed to be active.
    """
    return sys.prefix != sys.base_prefix


def main() -> None:
    """
    Entry point for the script.

    This function checks whether the script is running inside a
    Python virtual environment and prints diagnostic information
    about the current execution context.

    Behavior:
        - If no virtual environment is detected, it prints warnings
          and instructions for creating and activating one.
        - If a virtual environment is detected, it prints details
          about the environment, including its name, path, and
          site-packages directory.

    Raises:
        Any exception raised during execution will propagate to the
        caller and is expected to be handled by the top-level guard.
    """
    python_path = sys.executable

    if not in_virtualenv():
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\nScripts\nactivate   # On Windows\n")
        print("Then run this program again.")
    else:
        env_path = sys.prefix
        env_name = os.path.basename(env_path)
        site_packages = site.getsitepackages()

        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(site_packages[0])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
