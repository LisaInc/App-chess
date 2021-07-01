"""Play a round command."""

from .abc import Command
from app.models import 


class PlayARound(Command):
    """Handle all the match with the score of a round."""

    key = "round"
    readable_key = key
    description = "Play the next round."

    def __init__(self, tounament):
        """Init the command and the player to add to the db."""
        pass

    def execute(self, context):
        """Add the player and go to the main page."""
        pass
