"""Handle the main page."""

from app.views import NewTournamentView

from .abc import Controller


class NewTournamentController(Controller):
    """Main page."""

    def __init__(self):
        """Init."""
        super().__init__()

        self.view = NewTournamentView(self.commands)
