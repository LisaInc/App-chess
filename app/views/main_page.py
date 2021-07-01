from art import *

from app.commands import NewTournamentCommand
from .abc import View


class MainPageView(View):
    def __init__(self):
        """Init."""
        super().__init__()
        self.commands.append(NewTournamentCommand)
        self.title = "Main Page"

    def display_body(self):
        """Menu."""
        tprint("Welcome", font="rnd")
        self.console.print(
            ":chess_pawn: Welcome :chess_pawn: \nMenu", style="bold", justify="center"
        )
        print(
            "Be sure to add all the players to the data base before a new tournament."
        )
