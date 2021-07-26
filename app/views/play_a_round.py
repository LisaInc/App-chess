from app.commands import ContinueCommand
from app.models import Tournament

from .abc import View


class PlayARoundView(View):
    def __init__(self, tournament_id):
        """Init."""
        super().__init__()
        self.title = "Play a round"
        self.tournament = Tournament.get(tournament_id)

    def get_command(self):
        current_round = self.tournament.rounds[-1]
        currrent_nb_round = len(self.tournament.rounds)

        while not current_round.is_ended():
            print(f"Round {currrent_nb_round}")
            self.print_round(current_round)
            id = input("select a match (id only or nothing to auto play): ")
            if not id:
                current_round.auto_play()
            if id.isdigit() and int(id) < 4:
                match_choosen = current_round.matchs[int(id)]
                print(
                    "Who win the game: "
                    f"\n 1 - {match_choosen.player1.name},"
                    f"\n 2 - {match_choosen.player2.name},"
                    f"\n 3 - Draw"
                )
                winner = input("")

                while not match_choosen.result:
                    if winner == "1":
                        self.tournament.rounds[-1].matchs[int(id)].add_result(1, 0)
                    elif winner == "2":
                        self.tournament.rounds[-1].matchs[int(id)].add_result(0, 1)
                    elif winner == "3":
                        self.tournament.rounds[-1].matchs[int(id)].add_result(0.5, 0.5)
                    else:
                        winner = input("Select 1, 2 or 3: ")
            self.console.clear()
        current_round.save()
        return ContinueCommand(self.tournament.id)
