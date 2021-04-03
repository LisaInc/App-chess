"""Wrong command."""

from app.views import View

from .abc import Command


class WrongCommand(Command):
    """Wrong command."""

    def execute(self, context):
        """Create an error message."""
        context.controller.view.messages.append(View.wrong_command)
