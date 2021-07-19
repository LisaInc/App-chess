from app.commands.continue_tournament import ContinueCommand
from .abc import View


class PlayARoundView(View):
    def __init__(self, tournament):
        """Init."""
        super().__init__()
        self.title = "Play a round"
        self.tournament = tournament

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
                current_round.save()
            self.console.clear()
        return ContinueCommand(self.tournament)

    def print_round(self, round):
        columns = ["Match (id)", "Player 1", "Player 2", "Score (P1 - P2)"]
        rows = []
        for i, match in enumerate(round.matchs):
            score = (
                f"{match.result[str(match.player1.id)]} - {match.result[str(match.player2.id)]}"
                if match.result
                else "Ongoing"
            )
            rows.append((f"Match {i}", match.player1.name, match.player2.name, score))
        self.print_table(columns, rows)
