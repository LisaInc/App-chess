"""Add a player."""
from app.commands.add_player import AddPlayerCommand
from .abc import EventView
from datetime import date


class AddPlayerView(EventView):
    """Add a player, check the data, return the info to the add player command."""

    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Add a new player"

    def ask_for_command(self):
        """Ask the user about the info."""
        self.player_data = {"name": input("Please enter the full name:")}
        if self.player_data["name"] == "":
            return AddPlayerCommand(None)
        self.player_data = {
            "birth": input("Date of birth (yyyy/mm/dd):"),
            "sex": input("Sex (f/m/o):"),
            "rank": input("Rank of this player:"),
        }
        self.check_data_player()
        return AddPlayerCommand(self.player_data)

    def check_data_player(self):
        """Check the input."""
        correct_info = False
        while not correct_info:
            correct_info = True
            if "/" in self.player_data["birth"]:
                elems = self.player_data["birth"].split("/")
                if (
                    len(elems) == 3
                    and all(elem.isdigit() for elem in elems)
                    and int(elems[0]) > 1900
                    and int(elems[1]) <= 12
                    and int(elems[2]) <= 31
                ):
                    year = int(elems[0])
                    month = int(elems[1])
                    day = int(elems[2])
                    self.player_data["birth"] = date(year, month, day)
                else:
                    self.player_data["birth"] = self.ask_again(
                        "date of birth (yyyy/mm/dd)"
                    )
                    correct_info = False
            else:
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
