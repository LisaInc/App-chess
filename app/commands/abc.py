"""Command interface."""

from abc import ABC


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

    def execute(self, context):
        """Execute the command."""
        pass
