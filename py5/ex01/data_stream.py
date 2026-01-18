#!/usr/bin/env python3


from typing import Any, List, Dict, Optional, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    """Abstract base class for all types of data streams."""

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.stats = {"stream_id": self.stream_id, "processed": 0}

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.stats


class SensorStream(DataStream):

    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        filtered_batch = self.filter_data(data_batch, criteria="temp")
        return (f"{len(data_batch)} readings processed, avg temp: "
                f"{sum(filtered_batch) / len(filtered_batch)}°C")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return [elem[1] for elem in data_batch if elem[0] == criteria]

    def get_stats(self):
        return super().get_stats()


class StreamProcessor():

    def process(self, stream: DataStream, data_batch: List[Any]) -> str:
        return stream.process_batch(data_batch)


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    processor = StreamProcessor()

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    s_data = [("temp", 22.5), ("humidity", 65), ("pressure", 1013)]
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print(f"Processing sensor batch: [{s_data[0][0]}:{s_data[0][1]}, "
          f"{s_data[1][0]}:{s_data[1][1]}, "
          f"{s_data[2][0]}:{s_data[2][1]}]")
    try:
        print("Sensor analysis:", processor.process(sensor, s_data))
    except Exception as e:
        print(e)

    



if __name__ == "__main__":
    main()
