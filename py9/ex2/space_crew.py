#!/usr/bin/env python3

from enum import Enum
from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission_rules(self):
        """
    Validates mission-specific business rules after model initialization.

    Rules enforced:
    1. The mission_id must start with 'M'.
    2. The crew must include at least one member with rank CAPTAIN
    or COMMANDER.
    3. For missions longer than 365 days, at least 50% of the crew must have
       5 or more years of experience.
    4. All crew members must be active.

    Raises:
        ValueError: If any of the rules are violated.

    Returns:
        SpaceMission: The validated instance if all rules pass.
    """
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            member.rank in {Rank.CAPTAIN, Rank.COMMANDER}
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = [
                m for m in self.crew if m.years_experience >= 5
            ]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions require at least 50% experienced crew"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """
    Demonstrates the creation and validation of SpaceMission instances
    with crew members using Pydantic.

    - Creates a valid SpaceMission object including a list of CrewMember
    objects and prints its details.
    - Attempts to create an invalid SpaceMission object to trigger
    validation errors.
    - Displays error messages for expected validation failures.

    This function illustrates Pydantic's validation features, including:
    - Field constraints (min/max lengths, numeric ranges)
    - Enum validation for crew ranks
    - List constraints (crew size)
    - Custom model validation rules via `@model_validator`, e.g.:
        * Mission ID must start with 'M'
        * Mission must include at least one Captain or Commander
        * Long missions require at least 50% experienced crew
        * All crew members must be active
    """
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=38,
                    specialization="Navigation",
                    years_experience=10
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=6
                ),
            ],
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) -",
                member.specialization
            )

        print("\n=========================================")

    except ValidationError as e:
        print(e)

    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M_BAD",
            mission_name="Failed Test Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="CM010",
                    name="Bob Lee",
                    rank=Rank.OFFICER,
                    age=35,
                    specialization="Logistics",
                    years_experience=8
                )
            ],
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
