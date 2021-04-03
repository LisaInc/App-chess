"""Main page command."""

from .abc import Command
from app import controllers


class MainPageCommand(Command):
    """Handle the main page navigation."""

    key = "main"
    readable_key = key
    description = "return to the main page."

    def execute(self, context):
        """Go to the main page."""
        context.controller = controllers.MainPageController()
