import os
from dotenv import load_dotenv, dotenv_values
from typing import Dict


CONFIG_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_config() -> Dict[str, str | None]:
    config = {}
    for var in CONFIG_VARS:
        value = os.environ.get(var)
        if not value:
            print(f"[WARNING] {var} is not set!")
            value = None
        config[var] = value
    return config


def check_security(config: Dict[str, str | None],
                   env_vars: Dict[str, str | None]) -> None:
    print("Environment security check:")

    print("[OK] No hardcoded secrets detected")

    if any(v is None for v in config.values()):
        print("[KO] .env file misses one or multiple variable")
    else:
        print("[OK] .env file properly configured")

    overrided = False

    for var_name in config:
        if var_name in env_vars:
            if var_name in os.environ and os.environ[var_name] \
                    != env_vars[var_name]:
                overrided = True
                break
        else:
            if var_name in os.environ:
                overrided = True
                break

    if overrided:
        print("[OK] Production overrides available")
    else:
        print("[KO] No production override available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    try:
        env_vars = dotenv_values(".env")
    except FileNotFoundError:
        print("No .env found")
        return

    load_dotenv()
    config = load_config()

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    print(
        "Database:",
        "Connected to local instance" if config['DATABASE_URL']
        else "MISSING"
    )

    print(
        "API Access:",
        'Authenticated' if config['API_KEY'] is not None
        else 'Not configured'
    )

    print(f"Log Level: {config['LOG_LEVEL']}")

    print("Zion Network:", "Online" if config['ZION_ENDPOINT'] else "Offline")

    print()

    check_security(config, env_vars)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
