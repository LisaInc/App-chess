from .abc import PageView

from app.commands import NewTournamentCommand


class MainPageView(PageView):
    def __init__(self):
        """Init."""
        super().__init__()
        self.commands.append(NewTournamentCommand)
        self.title = "Main Page"

    def display_body(self):
        """Menu."""
        print("Menu")
        print(
            "Be sure to add all the players to the data base before a new tournament."
        )
