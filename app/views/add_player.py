from app.commands.add_player import AddPlayerCommand
from .abc import EventView


class AddPlayerView(EventView):
    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Add a new player"

    def ask_for_command(self):
        player_data = {
            "name": input("Please enter the full name:"),
            "birth": input("Date of birth (yyyy/mm/dd):"),
            "sex": input("Sex (f/m/o):"),
            "rank": input("Rank of this player:"),
        }
        return AddPlayerCommand(player_data)

    def check_data_player(self):
        """Check the input."""
        correct_info = False
        while not correct_info:
            correct_info = True
            elems = self["birth"].split("/")
            if len(elems) == 3 and all([elem.isdigit() for elem in elems]):
                self["birth"] = date(year, month, day)

            self["sex"]
            self["rank"]

    @classmethod
    def ask_again(self, wrong_info):
        """Ask the user to write again one olayer's information."""
        return input(f"Wrong {wrong_info}, please try again: ")
