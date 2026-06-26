import os
import site
import sys


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def get_environment_name() -> str:
    return os.path.basename(sys.prefix)


def get_package_paths() -> list[str]:
    try:
        return site.getsitepackages()
    except AttributeError:
        return [site.getusersitepackages()]


def show_activation_instructions() -> None:
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("Then run this program again.")


def show_virtual_environment() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_environment_name()}")
    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting", end=" ")
    print("the global system.")
    print("Package installation path:")
    for package_path in get_package_paths():
        print(package_path)


def show_global_environment() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    show_activation_instructions()
    print("Global package locations:")
    for package_path in get_package_paths():
        print(package_path)


def main() -> None:
    if is_virtual_environment():
        show_virtual_environment()
    else:
        show_global_environment()


if __name__ == "__main__":
    main()
