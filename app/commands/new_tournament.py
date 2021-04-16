"""Book delete command."""

from app.views import View

from .abc import Command
from .main_page import MainPageCommand


class NewTournamentCommand(Command):
    """Handle the book deletion."""

    key = "new"
    readable_key = key
    description = "add a player to the db."

    def execute(self, context):
        """Add the player and go to the main page."""
        context.controller.book.delete()
        MainPageCommand("").execute(context)
        context.controller.view.messages.append(View.book_deleted)