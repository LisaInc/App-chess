"""Book delete command."""

from .abc import Command
from app import controllers


class AddPlayerCommand(Command):
    """Handle the book deletion."""

    key = "add"
    readable_key = key
    description = "add a player to the db."

    def execute(self, context):
        """Add the player and go to the main page."""
        context.controller = controllers.AddPlayerController()
