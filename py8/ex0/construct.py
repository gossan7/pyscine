import sys
import os
import site


def in_virtualenv():
    return sys.prefix != sys.base_prefix


def main():
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
    main()
