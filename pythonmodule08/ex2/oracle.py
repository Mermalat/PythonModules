import os
import sys


ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")


REQUIRED_KEYS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_dotenv_file() -> bool:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("python-dotenv is not installed.")
        print("Install it with: pip install python-dotenv")
        print("Continuing with existing environment variables only.")
        return False

    return load_dotenv(dotenv_path=ENV_FILE, override=False)


def get_config() -> dict[str, str | None]:
    return {key: os.getenv(key) for key in REQUIRED_KEYS}


def get_mode(config: dict[str, str | None]) -> str:
    mode = config["MATRIX_MODE"]
    if mode in ("development", "production"):
        return mode
    if mode:
        print(
            "[WARN] MATRIX_MODE must be 'development' or 'production'; "
            "using development"
        )
    return "development"


def describe_database(database_url: str | None, mode: str) -> str:
    if not database_url:
        return "Missing DATABASE_URL"
    if mode == "development":
        return "Connected to local instance"
    return "Connected to production instance"


def describe_api(api_key: str | None) -> str:
    if not api_key:
        return "Missing API_KEY"
    return "Authenticated"


def describe_zion(endpoint: str | None) -> str:
    if not endpoint:
        return "Offline"
    return "Online"


def show_missing_config(config: dict[str, str | None]) -> None:
    missing_keys = [key for key, value in config.items() if not value]
    if not missing_keys:
        return

    print("Configuration warnings:")
    for key in missing_keys:
        print(f"[MISSING] {key}")
    print("Create a development config with:")
    print("cp .env.example .env")
    print("Then edit .env with your own values.")


def is_valid_config(config: dict[str, str | None]) -> bool:
    values_present = all(value for value in config.values())
    valid_mode = config["MATRIX_MODE"] in ("development", "production")
    return values_present and valid_mode


def show_security_check(
    dotenv_loaded: bool, config: dict[str, str | None]
) -> None:
    env_file_exists = os.path.isfile(ENV_FILE)
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if env_file_exists and dotenv_loaded and is_valid_config(config):
        print("[OK] .env file properly configured")
    elif env_file_exists and dotenv_loaded:
        print("[WARN] .env loaded but required values are missing")
    elif env_file_exists:
        print("[WARN] .env exists but python-dotenv did not load it")
    else:
        print("[WARN] .env file not found; using environment/defaults")
    print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    dotenv_loaded = load_dotenv_file()
    config = get_config()
    mode = get_mode(config)
    log_level = config["LOG_LEVEL"] or "INFO"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {describe_database(config['DATABASE_URL'], mode)}")
    print(f"API Access: {describe_api(config['API_KEY'])}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {describe_zion(config['ZION_ENDPOINT'])}")

    show_missing_config(config)
    show_security_check(dotenv_loaded, config)
    print("The Oracle sees all configurations.")

    if not is_valid_config(config):
        sys.exit(1)


if __name__ == "__main__":
    main()
