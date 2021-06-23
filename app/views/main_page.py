from app.commands import NewTournamentCommand
from .abc import View
from rich.console import Console


class MainPageView(View):
    def __init__(self):
        """Init."""
        super().__init__()
        self.commands.append(NewTournamentCommand)
        self.title = "Main Page"

    def display_body(self):
        """Menu."""
        console = Console()
        console.print(
            ":chess_pawn: Welcome :chess_pawn: \nMenu", style="bold", justify="center"
        )
        print(
            "Be sure to add all the players to the data base before a new tournament."
        )
