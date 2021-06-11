"""Add a player."""
from app.commands.add_player import AddPlayerCommand
from .abc import EventView
import re


class AddPlayerView(EventView):
    """Add a player, check the data, return the info to the add player command."""

    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Add a new player"

    def ask_for_command(self):
        """Ask the user about the info."""
        self.player_data = {
            "name": input(
                "Please enter the full name (leave empty to generate a random player):"
            )
        }
        if not self.player_data["name"]:
            return AddPlayerCommand(None)
        self.player_data["birth"] = input("Date of birth (yyyy/mm/dd):")
        self.player_data["sex"] = input("Sex (f/m/o):")
        self.player_data["rank"] = input("Rank of this player:")
        self.check_data_player()
        print(self.player_data)
        return AddPlayerCommand(self.player_data)

    def check_data_player(self):
        """Check the input."""
        correct_info = False
        while not correct_info:
            correct_info = True
            if not re.search("\d{4}/\d{2}/\d{2}", self.player_data["birth"]):
                self.player_data["birth"] = self.ask_again("date of birth (yyyy/mm/dd)")
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
