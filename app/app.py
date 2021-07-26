"""App module."""

from app.views import (
    View,
    AddPlayerView,
    MainPageView,
    NewTournamentView,
    PlayARoundView,
    ContinueView,
    TournamentEndedView,
    ChangeRankView,
    HistoryView,
)


class Application:
    """Application context.

    Use the strategy pattern.
    Attrs:
    - view (View): the "strategy". Handle a page in the application.
    - running (bool): True if the application is running else False.
    """

    possible_path = {
        "main page": MainPageView,
        "add": AddPlayerView,
        "new": NewTournamentView,
        "continue": ContinueView,
        "play round": PlayARoundView,
        "tournament ended": TournamentEndedView,
        "rank": ChangeRankView,
        "history": HistoryView,
    }

    def __init__(self):
        """Initialize the main page."""
        self.view: View = MainPageView()
        self.running = True

    def run(self):
        """Run the application."""
        while self.running:
            self.view.display()
            command = self.view.get_command()
            command.execute(context=self)

    def change_page(self, choice, *arg):
        """Change the view of the app."""
        self.view = self.possible_path[choice](*arg)
