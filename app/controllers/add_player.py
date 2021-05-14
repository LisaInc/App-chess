"""Handle the main page."""

from app.commands import AddPlayerCommand
from app.views import AddPlayerView

from .abc import Controller


class AddPlayerController(Controller):
    """Main page."""

    def __init__(self):
        """Init."""
        super().__init__()

        self.view = AddPlayerView(self.commands)
