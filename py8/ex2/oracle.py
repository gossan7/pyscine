import os
from dotenv import load_dotenv

load_dotenv()

CONFIG_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_config():
    config = {}
    for var in CONFIG_VARS:
        value = os.environ.get(var)
        if not value:
            print(f"[WARNING] {var} is not set!")
            value = "<MISSING>"
        config[var] = value
    return config


def check_security(config):
    print("Environment security check:")
    for key, val in config.items():
        if val.lower() in ("your_api_key_here", "<missing>"):
            print(f"[WARNING] {key} may not be configured properly")
        else:
            print(f"[OK] {key} is configured")


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {config['DATABASE_URL']}")
    print("API Access:",
          'Authenticated' if config['API_KEY'] != '<MISSING>'
          else 'Not configured')
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {config['ZION_ENDPOINT']}\n")

    check_security(config)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
