#!/usr/bin/env python3

from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    Abstract base class defining a common interface for all data processors.
    Subclasses must implement validation and processing
    logic for their data type.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the given data and return a result string.

        :param data: Input data to be processed
        :return: Processed result as a string
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate whether the given data is compatible with the processor.

        :param data: Input data to validate
        :return: True if data is valid, False otherwise
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the processed result for output.

        :param result: Result string from process()
        :return: Formatted output string
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Processor for numeric data collections.
    Expects a list of integers.
    """

    def process(self, data: List[int]) -> str:
        """
        Process a list of integers by computing count, sum, and average.
        """
        if not self.validate(data):
            raise ValueError(f"Invalid numeric data: \'{data}\'")
        return (
            f"Processed {len(data)} numeric values, sum = {sum(data)}, "
            f"avg = {sum(data) / len(data):.1f}"
        )

    def validate(self, data: List[int]) -> bool:
        """
        Validate that the data is a list of integers.
        """
        try:
            for n in data:
                if not isinstance(n, int):
                    return False

        except Exception:
            return False

        return True


class TextProcessor(DataProcessor):
    """
    Processor for textual data.
    """

    def process(self, data: str) -> str:
        """
        Process text by counting characters and words.
        """
        if not self.validate(data):
            raise ValueError(f"Invalid text data: \"{data}\"")
        return (
            f"Processed text: {len(data)} characters, "
            f"{len(data.split(' '))} words"
        )

    def validate(self, data: str) -> bool:
        """
        Validate that the data is a string.
        """
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    """
    Processor for log entries.
    Supports INFO and ERROR log levels.
    """

    def process(self, data: str) -> str:
        """
        Process a log entry and format it based on severity.
        """
        if not self.validate(data):
            raise ValueError(f"Invalid log data: \"{data}\"")
        log_data = data.split(":", 1)
        return (
            f"[{'ALERT' if log_data[0] == 'ERROR' else 'INFO'}] "
            f"{log_data[0]} level detected:{log_data[1]}"
        )

    def validate(self, data: str) -> bool:
        """
        Validate that the log entry starts with INFO or ERROR.
        """
        if not isinstance(data, str):
            return False

        log_type = data.split(":", 1)[0]
        if log_type == "ERROR" or log_type == "INFO":
            return True

        return False


def check_data(data: Any, processor: DataProcessor) -> str:
    """
    Process data using the given DataProcessor and format the output.

    :param data: Input data
    :param processor: A concrete DataProcessor instance
    :return: Formatted processing result
    """
    result = processor.process(data)
    return processor.format_output(result)


def main() -> None:
    """
    Demonstration of polymorphism in python.

    Returns
    -------
    int
        An error code.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric_processor = NumericProcessor()
    numeric_data = [1, 2, 3, 4, 5]
    try:
        print(f"Processing data: {numeric_data}")
        s = check_data(numeric_data, numeric_processor)
        print("Validation: Numeric data verified")
        print(s)
        print()

    except ValueError as e:
        print(e)

    print("Initializing Text Processor...")
    text_processor = TextProcessor()
    text_data = "Hello Nexus World"
    try:
        print(f"Processing data: \"{text_data}\"")
        s = check_data(text_data, text_processor)
        print("Validation: Text data verified")
        print(s)
        print()

    except ValueError as e:
        print(e)

    print("Initializing Log Processor...")
    log_processor = LogProcessor()
    log_data = "ERROR: Connection timeout"
    try:
        print(f"Processing data: \"{log_data}\"")
        s = check_data(log_data, log_processor)
        print("Validation: Log entry verified")
        print(s)
        print()

    except ValueError as e:
        print(e)

    print("=== Polymorphic Processing Demo ===\n")
    data_and_processors = [
        ([1, 2, 3], numeric_processor),
        ("Hello World", text_processor),
        ("INFO: System ready", log_processor)
    ]

    print("Processing multiple data types through same interface...")
    result = 1
    for data, processor in data_and_processors:
        try:
            print(f"Result {result}: {check_data(data, processor)}")

        except ValueError as e:
            print(e)

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
