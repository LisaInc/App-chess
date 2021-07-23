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
        while not tournament_choosen:
            tournament_to_continue = [
                tournament
                for tournament in self.all_tournaments
                if len(tournament.rounds) < tournament.nb_rounds
            ]
            if tournament_to_continue:
                self.print_table(
                    ["id", "name"],
                    [
                        (str(tournament.id), tournament.name)
                        for tournament in tournament_to_continue
                    ],
                    "List of all the tournament in the data base:",
                )
                id = input("Tournament's id: ")
                if id.isdigit():
                    tournament_choosen = Tournament.get(int(id))
                    if tournament_choosen:
                        return ContinueCommand(tournament_choosen)
                print("Enter the tournament's id")
            else:
                return NavigationCommand(
                    "main page", "There is no tournament in the database"
                )
