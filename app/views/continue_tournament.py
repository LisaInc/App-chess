from .abc import View

from app.commands import ContinueCommand, NavigationCommand
from app.models import Tournament


class ContinueView(View):
    def __init__(self):
        """Init."""
        super().__init__()
        self.title = "Choose a tournament to continue"
        self.all_tournaments = Tournament.all()

    def get_command(self):
        tournament_choosen = None
        if not self.all_tournaments:
            return NavigationCommand("mainpage", 'There is no tournament in the database')
        while not tournament_choosen:
            self.print_table(
                ["id", "name"],
                [
                    (str(tournament.id), tournament.name)
                    for tournament in self.all_tournaments
                ],
                "List of all the tournament in the data base:",
            )
            id = input("Tournament's id: ")
            if id.isdigit():
                tournament_choosen = Tournament.get(int(id))
                if tournament_choosen:
                    return ContinueCommand(tournament_choosen)
            print("Enter the tournament's id")
