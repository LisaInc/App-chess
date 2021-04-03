"""Book update controller."""

from app.models import Book
from app.views import BookUpdateView
from app.commands import BookDetailsCommand

from .abc import Controller


class BookUpdateController(Controller):
    """Handle the book update."""

    def __init__(self, book: Book):
        """Init."""
        super().__init__()
        self.book = book
        self.commands.extend([BookDetailsCommand])
        self.view = BookUpdateView(self.commands, book=self.book)
