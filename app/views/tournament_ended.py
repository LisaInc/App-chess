from .abc import View
from app.commands.navigation import NavigationCommand


class TournamentEndedView(View):
    def __init__(self, tournament):
        """Init."""
        super().__init__()
        self.title = "Display a round"
        self.tournament = tournament
        self.commands.append(NavigationCommand)

    def display_body(self):
        self.console.print(self.tournament.name, " is now finish !")
        sorted_by_score = sorted(
            self.tournament.players, key=lambda player: player.score
        )
        self.print_table(
            ("Player", "Player's score"),
            [(player.name, str(player.score)) for player in sorted_by_score],
        )
