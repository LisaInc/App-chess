"""Navigation command."""

from app import app
from .abc import Command


class NavigationCommand(Command):
    """Handle the pages navigation."""

    key = (
        "Navigation:"
        "\n - Main page"
        "\n - Add : add a new player"
        "\n - New : Start a new tournament"
        "\n - Continue: Continue a tournament saved on the db"
        "\n - Rank: Change the rank of a player"
    )
    readable_key = key
    description = "Go to the wanted page."
    possible_path = ["main page", "add", "new", "continue", "tournament ended", "rank"]

    def __init__(self, choice: str, *arg):
        """Init."""
        self.choice = choice
        if arg:
            self.arg = arg[0]

    @classmethod
    def get_choices(cls):
        """Return all the possible choices."""
        return app.Application.possible_path

    def execute(self, context):
        """Go to the wanted controller."""
        if hasattr(self, "arg"):
            context.change_page(self.choice, self.arg)
        else:
            context.change_page(self.choice)
