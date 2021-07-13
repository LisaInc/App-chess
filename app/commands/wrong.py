"""Wrong command."""


from .abc import Command


class WrongCommand(Command):
    """Wrong command."""

    def execute(self, context):
        """Create an error message."""
        from app.views import View

        context.view.messages.append(View.wrong_command)
