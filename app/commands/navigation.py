"""Main page command."""

from app import app
from .abc import Command


class NavigationCommand(Command):
    """Handle the pages navigation."""

    key = "navigation:" "\n - mainpage" "\n - addplayer" "\n - newtournament\n"
    readable_key = key
    description = "Go to the wanted page."
    possible_path = ["mainpage", "addplayer", "newtournament"]

    def __init__(self, choice: str):
        """Init."""
        self.choice = choice

    @classmethod
    def get_choices(cls):
        """Return all the possible choices."""
        return app.Application.possible_path

    def execute(self, context):
        """Go to the wanted controller."""
        context.change_page(self.choice)
