#!/usr/bin/env python3

from enum import Enum
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_rules(self):
        """
        Validates business rules for an AlienContact instance
        after model initialization.

        Rules enforced:
        1. contact_id must start with "AC".
        2. Physical contacts must be verified (is_verified=True).
        3. Telepathic contacts require at least 3 witnesses.
        4. Strong signals (signal_strength > 7.0) must include a
        received message.

        Raises:
            ValueError: If any of the above rules are violated.

        Returns:
            AlienContact: The validated instance if all rules pass.
        """
        if not self.contact_id[:2] == "AC":
            raise ValueError("Contact ID must start with \"AC\"")
        if self.contact_type == ContactType.PHYSICAL \
                and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main():
    """
    Demonstrates the creation and validation of AlienContact instances
    using Pydantic.

    - Creates a valid AlienContact object and prints its details.
    - Attempts to create an invalid AlienContact object to trigger
    validation errors.
    - Displays error messages for expected validation failures.

    This function showcases Pydantic's validation capabilities, including:
    - Enum field enforcement (ContactType)
    - Value constraints on numeric fields (signal_strength,
    duration_minutes, witness_count)
    - Custom model validation rules implemented via `@model_validator`
      (e.g., contact ID format, verification requirements,
      message requirements).
    """
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )

        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")
        print("\n======================================")

    except ValidationError as e:
        print(e)

    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Unknown Sector",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,
            message_received=None,
            is_verified=True
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
