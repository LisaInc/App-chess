from .abc import View

from app.commands import NavigationCommand
from app.models import Tournament


class HistoryView(View):
    def __init__(self):
        """Init."""
        super().__init__()
        self.commands.append(NavigationCommand)
        self.all_tournaments = Tournament.all()

    def display_body(self):
        self.print_tournaments(self.all_tournaments)
        id = input("Choose a tournament: ")
        while not id.isdigit():
            id = input("Choose a tournament (id): ")
        while not Tournament.get(int(id)):
            id = input("Choose a tournament from the list: ")
        self.tournament = Tournament.get(int(id))
        self.print_rounds(self.tournament)
        print("1 - See details of the rounds \n2 - Go to main page: ")
        choice = input("")
        while choice not in ["1", "2"]:
            choice = input("Choose 1 or 2: ")
        if choice == "2":
            return NavigationCommand("main page")
        for i, round in enumerate(self.tournament.rounds):
            print("\nRound ", i)
            self.print_round(round)
            if (i + 2) <= len(self.tournament.rounds):
                input("Press any key to see next round")
            else:
                print("Press any key to go to the main page")
                return NavigationCommand("main page")
