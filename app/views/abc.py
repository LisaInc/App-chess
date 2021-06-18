"""Views class: page view and event view."""

import os

from app.commands import BlankCommand, QuitCommand, WrongCommand, NavigationCommand


class View:
    """View class."""

    SEPARATOR = "-"
    CENTER_LENGTH = 30
    LINE = SEPARATOR * CENTER_LENGTH

    messages = []
    wrong_command = "Wrong command. Please, retry."
    enter_choice = "Enter a choice: "

    def __init__(self):
        """Init."""
        self.commands = [QuitCommand, BlankCommand, NavigationCommand]
        self.title = ""

    def print_part(self, part: str):
        """Print a part."""
        print(f" {part} ".center(self.CENTER_LENGTH, self.SEPARATOR))

    def clear(self):
        """Clear the console."""
        os.system("cls" if os.name == "nt" else "clear")

    def display(self):
        """Display the page."""
        self.clear()
        self.display_header()
        self.display_messages()
        self.display_body()
        self.display_footer()
        print()
        print(self.enter_choice, end="")

    def display_header(self):
        """Display the Header."""
        print(self.LINE)
        self.print_part(self.title)

    def display_messages(self):
        """Display the messages."""
        if self.messages:
            for message in self.messages:
                print("\n*", message)
        self.messages = []
        print()

    def display_body(self):
        """Display the body."""
        pass

    def display_footer(self):
        """Display the footer."""
        print()
        self.print_part("Commands")
        for command in self.commands:
            if command.key:
                print(command.readable_key, ":", command.description)

    def get_command(self):
        """Get the command."""
        choice = input()

        for Command in self.commands:
            if choice in Command.get_choices():
                return Command(choice)

        return WrongCommand(choice)
