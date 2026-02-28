#!/usr/bin/env python3

from typing import Any, List, Dict, Optional, Union, Tuple
from abc import ABC, abstractmethod


class DataStream(ABC):
    """Abstract base class for all data stream types."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.stats: Dict[str, Union[int, float]] = {}
        self.data: Optional[List[Any]] = None

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter data based on optional criteria."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[int, float]]:
        """Return stream statistics."""
        return self.stats


class SensorStream(DataStream):
    """Stream handling environmental sensor data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stats = {
            "avg temp": 0.0,
            "avg humidity": 0.0,
            "avg pressure": 0.0,
        }

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor readings and compute averages."""
        self.data = data_batch
        grouped: Dict[str, List[float]] = {}

        for key, value in data_batch:
            grouped.setdefault(key, []).append(value)

        for key, values in grouped.items():
            self.stats[f"avg {key}"] = sum(values) / len(values)

        return f"{len(data_batch)} readings processed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter sensor data based on temperature threshold."""
        if criteria == "high temp":
            return [
                item for item in data_batch
                if item[0] == "temp" and item[1] >= 35
            ]
        return data_batch


class TransactionStream(DataStream):
    """Stream handling financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stats = {
            "buy": 0,
            "sell": 0,
            "flow": 0,
        }

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transactions and compute net flow."""
        self.data = data_batch

        for key in self.stats:
            self.stats[key] = 0

        for action, value in data_batch:
            self.stats[action] += value

        self.stats["flow"] = self.stats["buy"] - self.stats["sell"]
        return f"{len(data_batch)} operations processed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter large transactions."""
        if criteria == "high trans":
            return [item for item in data_batch if item[1] >= 200]
        return data_batch


class EventStream(DataStream):
    """Stream handling system event logs."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stats = {
            "login": 0,
            "logout": 0,
            "error": 0,
        }

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process system events and count occurrences."""
        self.data = data_batch

        for key in self.stats:
            self.stats[key] = 0

        for event in data_batch:
            self.stats[event] += 1

        return f"{len(data_batch)} events processed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter error events."""
        if criteria == "error":
            return [event for event in data_batch if event == "error"]
        return data_batch


class StreamProcessor:
    """Manager class handling multiple stream types polymorphically."""

    def process(self, stream: DataStream, data_batch: List[Any]) -> str:
        """Process a data batch using the given stream."""
        return stream.process_batch(data_batch)


def format_pairs(data: List[Any]) -> str:
    """Format key-value pairs for display."""
    return ", ".join(f"{key}:{value}" for key, value in data)


def main() -> None:
    """Entry point for the polymorphic stream system."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    processor = StreamProcessor()

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    sensor_data = [
        ("temp", 22.5),
        ("humidity", 65),
        ("pressure", 1013),
    ]

    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print(f"Processing sensor batch: [{format_pairs(sensor_data)}]")
    print(
        f"Sensor analysis: {processor.process(sensor, sensor_data)}, "
        f"avg temp: {sensor.get_stats()['avg temp']}"
    )
    print()

    print("Initializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    transaction_data = [
        ("buy", 100),
        ("sell", 150),
        ("buy", 75),
    ]

    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    print(
        f"Processing transaction batch: "
        f"[{format_pairs(transaction_data)}]"
    )

    print(
        f"Transaction analysis: "
        f"{processor.process(transaction, transaction_data)}, "
        f"net flow: {transaction.get_stats()['flow']:+}"
    )

    print()

    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    event_data = ["login", "error", "logout"]
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    print(f"Processing event batch: [{', '.join(event_data)}]")

    print(
        f"Event analysis: {processor.process(event, event_data)}, "
        f"{event.get_stats()['error']} error detected"
    )

    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    batches: List[Tuple[str, List[Tuple[str, int] | str],
                        SensorStream | TransactionStream | EventStream]] = [
        (
            "Sensor data:",
            [
                ("temp", 40),
                ("temp", 50)
            ],
            sensor
        ),
        (
            "Transaction data:",
            [
                ("buy", 100),
                ("sell", 50),
                ("buy", 200),
                ("sell", 100)
            ],
            transaction,
        ),
        (
            "Event data:",
            [
                "login",
                "logout",
                "login"
            ],
            event
        ),
    ]

    for label, data, stream in batches:
        print(
            label,
            processor.process(stream, data)
        )

    print()

    print("Stream filtering active: High-priority data only")

    sensor_alerts = len(
        sensor.filter_data(batches[0][1], criteria="high temp")
    )

    transaction_alerts = len(
        transaction.filter_data(batches[1][1], criteria="high trans")
    )

    print(
        f"Filtered results: {sensor_alerts} critical sensor alerts, "
        f"{transaction_alerts} large transaction"
    )

    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
