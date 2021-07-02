"""Continue a tournament command."""

from .abc import Command

# from app.models import


class ContinueCommand(Command):
    """Choose a tournament to continue."""

    key = "continue"
    readable_key = key
    description = "Play the next round."

    def __init__(self, tounamet):
        """Init the command and the player to add to the db."""
        pass

    def execute(self, context):
        """Add the player and go to the main page."""
        pass
