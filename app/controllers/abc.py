"""Controller interface."""

from abc import ABC

from app.commands import BlankCommand, QuitCommand, WrongCommand
from app.views import View


class Controller(ABC):
    """Base controller."""

    def __init__(self, *args, **kwargs):
        """Init."""
        self.commands = [QuitCommand, BlankCommand]
        self.view: View = View(self.commands)

    def get_command(self):
        """Get the command."""
        choice = input()

        for Command in self.commands:
            if choice in Command.get_choices():
                return Command(choice)

        return WrongCommand(choice)
