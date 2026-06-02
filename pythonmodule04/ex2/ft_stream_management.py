import sys
from typing import IO


def print_error(message: str) -> None:
    sys.stderr.write("[STDERR] " + message + "\n")
    sys.stderr.flush()


def recover_file(file_name: str) -> tuple[bool, str]:
    archive_file: IO[str]

    print("=== Cyber Archives Recovery & Preservation ===")
    print("Accessing file '" + file_name + "'")
    try:
        archive_file = open(file_name)
    except Exception as error:
        sys.stdout.flush()
        print_error(f"Error opening file '{file_name}': {error}")
        return False, ""

    try:
        content = archive_file.read()
        print("---\n" + content + "---")
    except Exception as error:
        sys.stdout.flush()
        print_error(f"Error reading file '{file_name}': {error}")
        content = ""

    archive_file.close()
    print("File '" + file_name + "' closed.")
    return True, content


def transform_data(content: str) -> str:
    transformed = ""

    for character in content:
        if character == "\n":
            transformed += "#\n"
        else:
            transformed += character
    if content != "" and content[-1] != "\n":
        transformed += "#"
    return transformed


def save_data(file_name: str, content: str) -> None:
    archive_file: IO[str]

    print("Saving data to '" + file_name + "'")
    try:
        archive_file = open(file_name, "w")
    except Exception as error:
        sys.stdout.flush()
        print_error(f"Error opening file '{file_name}': {error}")
        print("Data not saved.")
        return

    try:
        archive_file.write(content)
        print("Data saved in file '" + file_name + "'.")
    except Exception as error:
        sys.stdout.flush()
        print_error(f"Error writing file '{file_name}': {error}")
        print("Data not saved.")

    archive_file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    recovered = recover_file(sys.argv[1])
    if not recovered[0]:
        return

    content = recovered[1]
    transformed = transform_data(content)
    print("Transform data:")
    print("---\n" + transformed + "---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file_name = sys.stdin.readline()
    if new_file_name != "" and new_file_name[-1] == "\n":
        new_file_name = new_file_name[:-1]
    if new_file_name == "":
        print("Not saving data.")
        return
    save_data(new_file_name, transformed)

main()
