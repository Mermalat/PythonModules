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

    def remaining(self) -> int:
        return len(self._items)

    def total_processed(self) -> int:
        return self._next_rank

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


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processor = self._find_processor(element)
            if processor is None:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )
                continue
            try:
                processor.ingest(element)
            except ValueError as exc:
                print(f"DataStream error - {exc}: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for processor in self._processors:
            print(
                f"{processor.name}: total {processor.total_processed()} "
                f"items processed, remaining {processor.remaining()} "
                "on processor"
            )

    def _find_processor(self, data: Any) -> DataProcessor | None:
        for processor in self._processors:
            if processor.validate(data):
                return processor
        return None


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    numeric = NumericProcessor()
    print("Registering Numeric Processor")
    stream.register_processor(numeric)
    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()

    print("Registering other data processors")
    text = TextProcessor()
    logs = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(logs)
    print("Send the same batch again")
    stream.process_stream(data)
    stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    logs.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
