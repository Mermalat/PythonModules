from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = [
            f'"item_{rank}": "{self._escape_json(value)}"'
            for rank, value in data
        ]
        print("{" + ", ".join(pairs) + "}")

    def _escape_json(self, value: str) -> str:
        escaped = ""
        for char in value:
            if char == "\\":
                escaped += "\\\\"
            elif char == '"':
                escaped += '\\"'
            elif char == "\n":
                escaped += "\\n"
            elif char == "\r":
                escaped += "\\r"
            elif char == "\t":
                escaped += "\\t"
            else:
                escaped += char
        return escaped


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            output: list[tuple[int, str]] = []
            for _ in range(nb):
                if processor.remaining() == 0:
                    break
                output.append(processor.output())
            if output:
                plugin.process_output(output)

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
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    first_batch = [
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
    print(f"Send first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
