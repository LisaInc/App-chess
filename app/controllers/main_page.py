"""Handle the main page."""

from app.commands import NewTournamentCommand, HistoryCommand
from app.views import MainPageView

from .abc import Controller


class MainPageController(Controller):
    """Main page."""

    def __init__(self):
        """Init."""
        super().__init__()
        self.commands.append(NewTournamentCommand)
        self.commands.append(HistoryCommand)
        self.view = MainPageView(self.commands)
