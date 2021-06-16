"""Main page command."""

from .abc import Command


class MainPageCommand(Command):
    """Handle the main page navigation."""

    key = "main"
    readable_key = key
    description = "Return to the main page."

    def execute(self, context):
        """Go to the main page."""
        context.change_page("mainpage")
