"""Start a new tornament."""
from app.commands.new_tournament import NewTornamentCommand
from .abc import EventView
from datetime import date


class NewTornamentCommand(EventView):
    """Start a new tornament."""

    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Start a new tornament"

    def ask_for_command(self):
        """Ask the user about the info."""
        self.player_data = {
            "name": input("Title of the tornament:"),
            "location": input("Location:"),
            "date_start": input("Start date (yyyy/mm/dd):"),
            "date_end": input("Start date (yyyy/mm/dd):"),
            "time_control": input("Time control:"),
            "description": input("Description:"),
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
                    self.ask_again("date of birth (yyyy/mm/dd)")
                    correct_info = False
            else:
                self.ask_again("date of birth (yyyy/mm/dd)")
                correct_info = False
            if self.player_data["sex"] not in ("f", "m", "o"):
                self.ask_again("sex (m,f,o)")
                correct_info = False
            if not self.player_data["rank"].isdigit():
                self.ask_again("rank")
                correct_info = False

    @classmethod
    def ask_again(self, wrong_info):
        """Ask the user to write again one player's information."""
        return input(f"Wrong {wrong_info}, please try again: ")
