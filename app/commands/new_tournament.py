"""New tournament command."""

from app.models.tournament import Tournament
from .abc import Command


class NewTournamentCommand(Command):
    """Create a new tournament."""

    key = "new"
    readable_key = key
    description = "Start a new tournament."

    def __init__(self, tournament_info):
        """Init the command and the player to add to the db."""
        self.tournament = (
            Tournament(**tournament_info) if tournament_info else Tournament.auto_init()
        )

    def execute(self, context):
        """Add the player and go to the main page."""
        self.tournament.pairing_for_a_round()
        self.tournament.save()
        context.change_page("play round", Tournament.get(self.tournament.id))
