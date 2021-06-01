import os


class View:

    SEPARATOR = "-"
    CENTER_LENGTH = 30
    LINE = SEPARATOR * CENTER_LENGTH

    messages = []
    wrong_command = "Wrong command. Please, retry."
    enter_choice = "Enter a choice: "

    def __init__(self, commands):
        """Init."""
        self.commands = commands
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


class PageView(View):
    type = "page"


class EventView(View):
    type = "event"

    def display(self):
        """Display the page."""
        self.clear()
        self.display_header()
        self.display_messages()
        self.ask_for_command()
        self.display_footer()
        print()

    def ask_for_command(self):
        """récupère des événements utilisateur et retourne une commande."""
        pass