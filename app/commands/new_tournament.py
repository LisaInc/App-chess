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
        self.tournament = (
            Tournament(**tournament_info) if tournament_info else Tournament.auto_init()
        )

    def execute(self, context):
        """Add the player and go to the main page."""
        if self.tournament:
            self.tournament.save()
        context.change_page("play_a_round")
