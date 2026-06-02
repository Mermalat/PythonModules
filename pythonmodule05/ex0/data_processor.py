from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self._items: list[tuple[int, str]] = []
        self._next_rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._items.pop(0)

    def _store(self, value: str) -> None:
        self._items.append((self._next_rank, value))
        self._next_rank += 1


NumericData = int | float | list[int | float]
TextData = str | list[str]
LogData = dict[str, str] | list[dict[str, str]]


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        if type(data) in (int, float):
            return True
        if isinstance(data, list):
            return all(type(item) in (int, float) for item in data)
        return False

    def ingest(self, data: NumericData) -> None:  # type: ignore[override]
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: TextData) -> None:  # type: ignore[override]
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._store(item)
        else:
            self._store(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._is_log_entry(data)
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and self._is_log_entry(item)
                for item in data
            )
        return False

    def ingest(self, data: LogData) -> None:  # type: ignore[override]
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                self._store(self._format_log(item))
        else:
            self._store(self._format_log(data))

    def _is_log_entry(self, data: dict[Any, Any]) -> bool:
        return all(isinstance(key, str) and isinstance(value, str)
                   for key, value in data.items())

    def _format_log(self, data: dict[str, str]) -> str:
        if "log_level" in data and "log_message" in data:
            return f"{data['log_level']}: {data['log_message']}"
        return ", ".join(f"{key}: {value}" for key, value in data.items())


def print_output(label: str, processor: DataProcessor, count: int) -> None:
    for _ in range(count):
        rank, value = processor.output()
        print(f"{label} value {rank}: {value}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as exc:
        print(f"Got exception: {exc}")
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    print_output("Numeric", numeric, 3)

    text = TextProcessor()
    print("Testing Text Processor...")
    print(f"Trying to validate input '42': {text.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    print_output("Text", text, 1)

    logs = LogProcessor()
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {logs.validate('Hello')}")
    print(f"Processing data: {log_data}")
    logs.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = logs.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
