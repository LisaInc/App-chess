from art import tprint

from .abc import View


class MainPageView(View):
    def __init__(self):
        """Init."""
        super().__init__()

    def display_body(self):
        """Menu."""
        tprint("Welcome", font="rnd")
        self.console.print(":chess_pawn: Menu :chess_pawn:", style="bold")
        print(
            "Be sure to add all the players to the data base before a new tournament."
        )
