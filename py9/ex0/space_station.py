#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    """
    Demonstrates the creation and validation of
    SpaceStation instances using Pydantic.

    - Creates a valid SpaceStation object and prints its details.
    - Attempts to create an invalid SpaceStation object to trigger a
    validation error.
    - Catches and displays the validation error message.

    This function showcases Pydantic's data validation capabilities, including
    type enforcement, value constraints, and optional fields.
    """
    print("Space Station Data Validation")
    print("========================================")

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now()
    )

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print("Status:", 'Operational' if station.is_operational
                     else 'Non-operational')
    print("\n========================================")

    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="BAD01",
            name="Bad Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now()
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
