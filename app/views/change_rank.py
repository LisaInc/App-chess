from .abc import View

from app.commands import ChangeRankCommand
from app.models import Player


class ChangeRankView(View):
    def __init__(self):
        """Init."""
        super().__init__()
        self.title = "Change the rank of a player"
        self.all_players = Player.all()

    def get_command(self):
        self.print_table(
            ["id", "name", "rank"],
            [
                (str(player.id), player.name, str(player.rank))
                for player in self.all_players
            ],
            "List of all the player in the data base:",
        )
        id = input("player's id: ")
        while not id.isdigit():
            id = input("player's id (must be a number): ")
        player_choosen = Player.get(int(id))
        while not player_choosen:
            id = input("player's id: ")
            player_choosen = Player.get(int(id))
        new_rank = input("New rank: ")
        while not new_rank.isdigit():
            new_rank = input("New rank (must be a number): ")
        return ChangeRankCommand(player_choosen, new_rank)
