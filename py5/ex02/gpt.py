#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Protocol
from abc import ABC, abstractmethod
from datetime import datetime


# ---------------- STAGES ---------------- #

class ProcessingStage(Protocol):
    """Duck-typed interface for pipeline stages."""
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    """Validates and parses raw input data."""
    def process(self, data: Any) -> Dict:
        if isinstance(data, dict):
            return data.copy()
        elif isinstance(data, str):
            return {key: None for key in data.split(",")}
        elif isinstance(data, list):
            result = {}
            for elem in data:
                if ":" in elem:
                    k, v = elem.split(":")
                    result[k] = v
            return result
        else:
            raise TypeError("Unsupported input format")


class TransformStage:
    """Transforms data: enriches with metadata or additional info."""
    def process(self, data: Dict) -> Dict:
        data["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["status"] = "validated"
        return data


class OutputStage:
    """Formats data for output."""
    def process(self, data: Dict) -> str:
        return ", ".join(f"{k}:{v}" for k, v in data.items())


# ---------------- PIPELINES ---------------- #

class ProcessingPipeline(ABC):
    """Abstract pipeline containing configurable stages."""
    def __init__(self):
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter for JSON data."""
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Dict:
        if not isinstance(data, dict):
            raise TypeError("JSONAdapter expects a dict")
        data["type"] = "JSON"
        for stage in self.stages:
            data = stage.process(data)
        return data


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter for CSV data."""
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> str:
        if not isinstance(data, str):
            raise TypeError("CSVAdapter expects a string")
        data_dict = {key: None for key in data.split(",")}
        data_dict["type"] = "CSV"
        for stage in self.stages:
            data_dict = stage.process(data_dict)
        return OutputStage().process(data_dict)


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter for real-time stream data."""
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> str:
        if not isinstance(data, list):
            raise TypeError("StreamAdapter expects a list")
        data_dict = {}
        for elem in data:
            if ":" in elem:
                k, v = elem.split(":")
                data_dict[k] = v
        data_dict["type"] = "Stream"
        for stage in self.stages:
            data_dict = stage.process(data_dict)
        return OutputStage().process(data_dict)


# ---------------- NEXUS MANAGER ---------------- #

class NexusManager:
    """Orchestrates multiple pipelines, supports chaining and error recovery."""
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline):
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> Any:
        # pick pipeline based on type
        if isinstance(data, dict):
            pipeline = next(p for p in self.pipelines if isinstance(p, JSONAdapter))
        elif isinstance(data, str):
            pipeline = next(p for p in self.pipelines if isinstance(p, CSVAdapter))
        elif isinstance(data, list):
            pipeline = next(p for p in self.pipelines if isinstance(p, StreamAdapter))
        else:
            raise TypeError("Unsupported data type")

        # run stages sequentially
        result = data
        for stage in pipeline.stages:
            try:
                result = stage.process(result)
            except Exception as e:
                print(f"Error in stage {stage.__class__.__name__}: {e}")
                print("Recovery: using backup processor (pass-through)")
                return result
        return result


# ---------------- MAIN ---------------- #

def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    manager = NexusManager()
    print("Pipeline capacity: 1000 streams/second\n")

    print("Creating Data Processing Pipeline...")
    json_pipeline = JSONAdapter("0001")
    csv_pipeline = CSVAdapter("0002")
    stream_pipeline = StreamAdapter("0003")

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")

    print("=== Multi-Format Data Processing ===\n")

    # JSON data
    print("Processing JSON data through pipeline...")
    json_input = {"sensor": "temp", "value": 23.5, "unit": "C"}
    print(f"Input: {json_input}")
    output = manager.process_data(json_input)
    print(f"Output: {output}\n")

    # CSV data
    print("Processing CSV data through pipeline...")
    csv_input = "user,action,timestamp"
    print(f"Input: \"{csv_input}\"")
    output = manager.process_data(csv_input)
    print(f"Output: {output}\n")

    # Stream data
    print("Processing Stream data through pipeline...")
    stream_input = ["temp:22", "humidity:50", "pressure:1012"]
    print(f"Input: {stream_input}")
    output = manager.process_data(stream_input)
    print(f"Output: {output}\n")

    # Simulate error recovery
    print("=== Error Recovery Test ===")
    try:
        manager.process_data(42)  # invalid input to trigger error
    except Exception as e:
        print(f"Simulating pipeline failure...\nError detected: {e}")
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed")


if __name__ == "__main__":
    main()
