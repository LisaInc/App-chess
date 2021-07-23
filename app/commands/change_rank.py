"""Add player command."""

from .abc import Command
from app.models import Player


class ChangeRankCommand(Command):
    """Change the rank of one or more player."""

    key = "add"
    readable_key = key
    description = "Add a player to the db."

    def __init__(self, player, new_rank):
        """Init the command and the player to add to the db."""
        self.player = player
        self.new_rank = new_rank

    def execute(self, context):
        self.player.rank = self.new_rank
        self.player.save()
        context.change_page("main page")
