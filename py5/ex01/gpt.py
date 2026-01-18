#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Optional


# === Abstract Base Class ===
class DataStream(ABC):
    """Abstract base class for a data stream."""

    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data (must be implemented by subclass)."""
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        """Default filter: returns data unmodified. Can be overridden."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Default stats: return stream ID and total items."""
        return {"stream_id": self.stream_id, "total_items": 0}


# === Specialized Stream Classes ===
class SensorStream(DataStream):
    """Stream for environmental sensor data."""

    def process_batch(self, data_batch: List[Dict[str, float]]) -> str:
        # Example: calculate average temperature if available
        temps = [d.get("temp", 0) for d in data_batch if "temp" in d]
        avg_temp = sum(temps) / len(temps) if temps else 0
        return f"{len(data_batch)} readings processed, avg temp: {avg_temp:.1f}°C"

    def filter_data(self, data_batch: List[Dict[str, float]], criteria: Optional[str] = None) -> List[Dict[str, float]]:
        # Example filter: keep only readings with temp > 25
        if criteria == "high_temp":
            return [d for d in data_batch if d.get("temp", 0) > 25]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "stream_type": "Environmental", "total_items": 0}


class TransactionStream(DataStream):
    """Stream for financial transactions."""

    def process_batch(self, data_batch: List[Dict[str, int]]) -> str:
        net_flow = sum(d.get("amount", 0) for d in data_batch)
        return f"{len(data_batch)} operations, net flow: {net_flow} units"

    def filter_data(self, data_batch: List[Dict[str, int]], criteria: Optional[str] = None) -> List[Dict[str, int]]:
        # Example: keep only transactions with amount > 100 if high-priority
        if criteria == "high_value":
            return [d for d in data_batch if d.get("amount", 0) > 100]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "stream_type": "Financial", "total_items": 0}


class EventStream(DataStream):
    """Stream for system events."""

    def process_batch(self, data_batch: List[str]) -> str:
        error_count = sum(1 for e in data_batch if e.lower() == "error")
        return f"{len(data_batch)} events processed, {error_count} errors detected"

    def filter_data(self, data_batch: List[str], criteria: Optional[str] = None) -> List[str]:
        # Example: keep only critical events
        if criteria == "critical":
            return [e for e in data_batch if e.lower() in ("error", "critical")]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "stream_type": "System Events", "total_items": 0}


# === Stream Processor ===
class StreamProcessor:
    """Handles multiple DataStream types polymorphically."""

    def process_stream(self, stream: DataStream, data_batch: List[Any], filter_criteria: Optional[str] = None):
        """Process a stream batch with optional filtering."""
        try:
            filtered_batch = stream.filter_data(data_batch, filter_criteria)
            result = stream.process_batch(filtered_batch)
            stats = stream.get_stats()
            print(f"[{stream.stream_id}] Result: {result}")
            print(f"[{stream.stream_id}] Stats: {stats}\n")
        except Exception as e:
            print(f"[{stream.stream_id}] ERROR: {e}")


# === Main Demo ===
def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    # Create streams
    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    processor = StreamProcessor()

    # Example batches
    sensor_data = [{"temp": 22.5, "humidity": 65}, {"temp": 27.0}, {"temp": 23.0}]
    transaction_data = [{"amount": 100}, {"amount": 150}, {"amount": 75}]
    event_data = ["login", "error", "logout"]

    print("=== Processing Individual Streams ===\n")
    processor.process_stream(sensor_stream, sensor_data)
    processor.process_stream(transaction_stream, transaction_data)
    processor.process_stream(event_stream, event_data)

    print("=== Polymorphic Stream Processing ===\n")
    # Process all streams polymorphically with filtering
    mixed_batches = [
        (sensor_stream, sensor_data, "high_temp"),
        (transaction_stream, transaction_data, "high_value"),
        (event_stream, event_data, "critical")
    ]

    for stream, batch, criteria in mixed_batches:
        processor.process_stream(stream, batch, criteria)

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
