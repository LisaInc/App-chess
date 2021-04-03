"""Command interface."""

from abc import ABC
from typing import Any


class Command(ABC):
    """Absctract command."""

    key = ""
    readable_key = key
    description = ""

    def __init__(self, choice: str):
        """Init."""
        pass

    @classmethod
    def get_choices(cls):
        """Return the possible choices."""
        return [cls.key]

    def execute(self, context: Any):
        """Execute the command."""
        pass
