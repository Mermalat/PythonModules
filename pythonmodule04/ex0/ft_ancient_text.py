import sys
from typing import IO


def display_file(file_name: str) -> None:
    archive_file: IO[str]

    print("=== Cyber Archives Recovery ===")
    print("Accessing file '" + file_name + "'")
    try:
        archive_file = open(file_name)
    except Exception as error:
        print(f"Error opening file '{file_name}': {error}")
        return

    try:
        content: str = archive_file.read()
        print("---\n" + content + "---")
    except Exception as error:
        print(f"Error reading file '{file_name}': {error}")

    archive_file.close()
    print("File '" + file_name + "' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    display_file(sys.argv[1])


main()
