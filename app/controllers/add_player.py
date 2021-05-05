"""Handle the main page."""

from app.commands import AddPlayerCommand, NewTournamentCommand, HistoryCommand
from app.views import MainPageView

from .abc import Controller


class AddPlayerController(Controller):
    """Main page."""

    def __init__(self):
        """Init."""
        super().__init__()

        self.view = MainPageView(self.commands)
