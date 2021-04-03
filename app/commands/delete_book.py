"""Book delete command."""

from app.views import View

from .abc import Command
from .main_page import MainPageCommand


class DeleteBookCommand(Command):
    """Handle the book deletion."""

    key = "delete"
    readable_key = key
    description = "delete the book."

    def execute(self, context):
        """Delete the book and go to the main page."""
        context.controller.book.delete()
        MainPageCommand("").execute(context)
        context.controller.view.messages.append(View.book_deleted)
