"""Start a new tournament."""

import re  # attention ordre import

from app.commands.new_tournament import NewTournamentCommand
from app.models.player import Player

from .abc import EventView  # import relatif à la toute fin


class NewTournamentView(EventView):
    """Start a new tournament."""

    def __init__(self):
        """Init."""
        super().__init__()
        self.title = "Start a new tournament"

    def get_command(self):
        """Ask the user about the info."""
        if len(Player.table.all()) < 8:
            return NewTournamentCommand(None)
        self.tournament_data = {
            "name": input("Title of the tournament:"),
            "location": input("Location:"),
            "date_start": input("Start date (yyyy/mm/dd):"),
            "date_end": input("End date (yyyy/mm/dd):"),
            "time_control": input("Time control:"),
            "description": input("Description:"),
        }
        self.check_data_tournement()
        players = []
        while len(players) < 8:
            print("Choose a player from the list:")
            Player.print_all()
            id = input("Player's id:")
            if id.isdigit():
                players.add[Player.get(id)]
        return NewTournamentCommand(self.tournament_data)

    def check_data_tournement(self):
        """Check the input."""
        correct_info = False
        while not correct_info:
            correct_info = False
            while not correct_info:
                correct_info = True
                if not re.search("\d{4}/\d{2}/\d{2}", self.player_data["date_start"]):
                    self.player_data["date_start"] = self.ask_again(
                        "start day (yyyy/mm/dd)"
                    )
                    correct_info = False
                if not re.search("\d{4}/\d{2}/\d{2}", self.player_data["date_end"]):
                    self.player_data["date_end"] = self.ask_again(
                        "end day (yyyy/mm/dd)"
                    )
                    correct_info = False
                if self.player_data["sex"] not in ("f", "m", "o"):
                    self.player_data["sex"] = self.ask_again("sex (m,f,o)")
                    correct_info = False
                if not self.player_data["rank"].isdigit():
                    self.player_data["rank"] = self.ask_again("rank")
                    correct_info = False

    @classmethod
    def ask_again(self, wrong_info):
        """Ask the user to write again one player's information."""
        return input(f"Wrong {wrong_info}, please try again: ")
