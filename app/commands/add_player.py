"""Add player command."""

from .abc import Command
from app.models import Player


class AddPlayerCommand(Command):
    """Add a plyer to the data base."""

    key = "add"
    readable_key = key
    description = "Add a player to the db."

    def __init__(self, player_info):
        """Init the command and the player to add to the db."""
        self.player = Player(**player_info) if player_info else Player.auto_init()

    def execute(self, context):
        """Add the player and go to the main page."""
        self.player.save()
        context.change_page("main page")
