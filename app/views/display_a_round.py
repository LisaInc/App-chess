from app.commands import ContinueCommand
from app.models import Tournament
from .abc import View


class DisplayARoundView(View):
    def __init__(self, tournament):
        """Init."""
        super().__init__()
        self.title = "Display a round"
        self.tournament = tournament

    def get_command(self):
        round_choosen = False
        while not round_choosen:
            self.print_rounds(self.tournament)
            id = input("Round's id: ")
            if id.isdigit():
                tournament_choosen = Tournament.get(int(id))
                if tournament_choosen:
                    return ContinueCommand(tournament_choosen)
            print("Enter the tournament's id")

    def print_rounds(self, tournament):
        columns = ["Round", "State"]
        rows = []
        for i, round in enumerate(tournament.rounds):
            state = "Finish" if round.is_ended() else "Ongoing"
            rows.append((f"Round {i}", state))
        self.print_table(columns, rows)
