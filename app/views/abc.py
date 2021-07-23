"""Views class: page view and event view."""

import re
from rich.table import Table
from rich.console import Console

from app.commands import BlankCommand, QuitCommand, WrongCommand


class View:
    """View class."""

    console = Console()
    SEPARATOR = "-"
    CENTER_LENGTH = 198
    LINE = SEPARATOR * CENTER_LENGTH

    messages = []
    wrong_command = "Wrong command. Please, retry."
    enter_choice = "Enter a choice: "

    def __init__(self, *arg):
        """Init."""
        self.commands = [QuitCommand, BlankCommand]
        self.title = ""

    def print_part(self, part: str):
        """Print a part."""
        self.console.print(f" {part} ", style="yellow bold", justify="Right")

    def display(self):
        """Display the page."""
        self.console.clear()
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
        print()
        self.messages = []

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

    def print_table(self, colomns, rows, title=None):
        """
        Print a table with:
        * columns names in a list
        * list of row (tuple)
        * title (str) optionnal
        """
        table = Table(title=title) if title else Table()
        for column in colomns:
            table.add_column(column, style="bold")
        for row in rows:
            table.add_row(*row)
        self.console.print(table)

    def check_date(self, date):
        """Check if the str is a date."""
        return bool(
            re.search("^[0-9]{4}/(0?[1-9]|1[012])/(0?[1-9]|[12][0-9]|3[01])$", date)
        )

    def print_rounds(self, tournament):
        columns = ["Round", "State"]
        rows = []
        for i, round in enumerate(tournament.rounds):
            state = "Finish" if round.is_ended() else "Ongoing"
            rows.append((f"Round {i}", state))
        self.print_table(columns, rows)
