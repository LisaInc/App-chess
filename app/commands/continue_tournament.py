"""Continue a tournament command."""

from .abc import Command
from app.models import Tournament


class ContinueCommand(Command):
    """Continue a tournament."""

    key = "continue"
    readable_key = key
    description = "Play the next round."

    def __init__(self, tournament_id):
        """Init the command and the player to add to the db."""
        self.tournament = Tournament.get(tournament_id)

    def execute(self, context):
        """Add the player and go to the main page."""
        current_round = self.tournament.rounds[-1]
        currrent_nb_round = len(self.tournament.rounds)
        if currrent_nb_round < self.tournament.nb_rounds:
            if current_round.is_ended():
                current_round.add_endtime()
                self.tournament.pairing_for_a_round()
                self.tournament.save()
            context.change_page("play round", self.tournament.id)
        else:
            self.tournament.save()
            context.change_page("tournament ended", self.tournament.id)
