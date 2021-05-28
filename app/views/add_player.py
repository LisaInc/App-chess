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
        return AddPlayerCommand(**player_data)
