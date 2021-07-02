from .abc import View


class PlayARoundView(View):
    def init(self, tournament):
        """Init."""
        super().init()
        self.title = "Play a round"

    def get_command(self):
        matchs_not_done = True

        while matchs_not_done:
            self.print_round(self.tournament)

    def print_round(self, round):
        for i, match in enumerate(round.matchs):
            print(f"Match {i}")
            self.print_table()