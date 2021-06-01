"""Book delete command."""

from .abc import Command
from app.models import Player
from app import controllers

from datetime import date


class AddPlayerCommand(Command):
    """Handle the book deletion."""

    key = "add"
    readable_key = key
    description = "Add a player to the db."

    def __init__(self, player_info):
        self.player = Player(**player_info) if player_info else Player.auto_init()

    def execute(self, context):
        """Add the player and go to the main page."""
        context.controller = controllers.AddPlayerController()
