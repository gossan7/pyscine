#!/usr/bin/env python3

from typing import Any, List, Dict, Optional, Union, Protocol
from abc import ABC, abstractmethod
from datetime import datetime, time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Dict:
        if isinstance(data, dict):
            adapter = JSONAdapter("0001")
        elif isinstance(data, str):
            adapter = CSVAdapter("0002")
        elif isinstance(data, List):
            adapter = StreamAdapter("0003")
        else:
            raise TypeError("Invalid data format")
        return adapter.process(data)


class TransformStage:
    def process(self, data: Any) -> Dict:
        if not isinstance(data, dict):
            raise TypeError("Invalid data format")
        data["date_time"] = datetime.now()
        return data


class OutputStage:
    def process(self, data: Any) -> str:
        return " ".join([str(key) + ":" + str(data[key]) for key in data])


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data):
        if not isinstance(data, dict):
            raise TypeError("Invalid data format")
        data["type"] = "JSON"
        return data


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data):
        if not isinstance(data, str):
            raise TypeError("Invalid data format")
        data = {key: None for key in data.split(",")}
        data["type"] = "CSV"
        return data


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data):
        if not isinstance(data, List):
            raise TypeError("Invalid data format")
        new_data = dict()
        for elem in data:
            if not isinstance(elem, str):
                raise TypeError("Invalid data format")
            split = elem.split(":")
            if len(split) != 2:
                raise TypeError("Invalid data format")
            new_data[split[0]] = split[1]
        new_data["type"] = "Stream"
        data = new_data
        return data


class NexusManager:
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())

    def process_data(self, data: Any):
        if len(self.pipelines) == 0:
            raise Exception("No pipeline in NexusManager")
        if len(self.pipelines) == 1:
            pipeline = self.pipelines.pop()
            for stage in pipeline.stages:
                data = stage.process(data)
            return data
        else:
            size = len(pipeline)
            for i in range(size):
                pipeline = self.pipelines.pop(0)
                if i == 0:
                    data = pipeline.stages[0].process(data)
                elif i == len(self.pipelines) - 1:
                    data = pipeline.stages[1].process(data)
                    return pipeline.stages[2].process(data)
                data = pipeline.stages[1].process(data)


def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    manager = NexusManager()
    print("Pipeline capacity: 1000 streams/second\n")

    print("Creating Data Processing Pipeline...")
    manager.add_pipeline(JSONAdapter("0001"))
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")

    print("=== Multi-Format Data Processing ===\n")

    print("Processing JSON data through pipeline...")
    input = {"sensor": "temp", "value": 23.5, "unit": "C"}
    print(f"Input: {input}")
    print("Transofrm: Enriched with metadata and validation")
    output = manager.process_data(input)
    print(f"Output: {output}")


if __name__ == "__main__":
    main()
