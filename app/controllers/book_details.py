"""Book details controller."""

from app.models import Book
from app.views import BookDetailsView
from app.commands import MainPageCommand, DeleteBookCommand

from .abc import Controller


class BookDetailsController(Controller):
    """Handle the book details."""

    def __init__(self, book: Book):
        """Init."""
        super().__init__()
        self.book = book
        self.commands.extend([MainPageCommand, DeleteBookCommand])
        self.view = BookDetailsView(self.commands, book=self.book)
