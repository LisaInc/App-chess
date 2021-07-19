from art import tprint

from .abc import View
from app.commands.navigation import NavigationCommand


class MainPageView(View):
    def __init__(self, message=None):
        """Init."""
        super().__init__()
        self.commands.append(NavigationCommand)
        if message:
            self.messages.append(message)

    def display_body(self):
        """Menu."""
        tprint("Welcome", font="rnd")
        self.console.print(":chess_pawn: Menu :chess_pawn:", style="bold")
        if self.messages:
            self.display_messages()
        print(
            "Be sure to add all the players to the data base before a new tournament."
        )
