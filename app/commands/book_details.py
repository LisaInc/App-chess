"""Book details command."""

from app import controllers
from app.models import Book

from .abc import Command


class BookDetailsCommand(Command):
    """Handle the book details command."""

    key = "book-"
    readable_key = "book-<number>"
    description = "display the book details."

    def __init__(self, choice: str):
        """Init."""
        book_id = int(choice.replace(self.key, ""))
        self.book = Book.get(id=book_id)

    @classmethod
    def get_choices(cls):
        """Return the possible choices."""
        return [f"{cls.key}{index}" for index in range(1, len(Book.list()) + 1)]

    def execute(self, context):
        """Go to the book details."""
        controller = controllers.BookDetailsController
        context.controller = controller(book=self.book)  # type: ignore
