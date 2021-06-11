"""New tournament command."""
from app.models.tournament import Tournament
from .abc import Command


class NewTournamentCommand(Command):
    """Create a new tournament."""

    key = "new"
    readable_key = key
    description = "Start a new tournament."
    tournament = None

    def __init__(self, tournament_info):
        """Init the command and the player to add to the db."""
        if tournament_info:
            self.tournament = Tournament(**tournament_info)

    def execute(self, context):
        """Add the player and go to the main page."""
        if self.tournament:
            self.player.save()
        context.change_page("mainpage")
