"""Main page command."""

from .abc import Command


class NavigationCommand(Command):
    """Handle the pages navigation."""

    key = "navigation: mainpage - addplayer"
    readable_key = key
    description = "Go to the wanted page."
    possible_path = ["mainpage", "addplayer"]

    def __init__(self, choice: str):
        """Init."""
        self.choice = choice

    @classmethod
    def get_choices(cls):
        """Return all the possible choices."""
        return cls.possible_path

    def execute(self, context):
        """Go to the wanted controller."""
        context.change_page(self.choice)
