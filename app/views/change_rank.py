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
        player_choosen = None
        while not player_choosen:
            self.print_table(
                ["id", "name", "rank"],
                [
                    (str(player.id), player.name, str(player.rank))
                    for player in self.all_players
                ],
                "List of all the player in the data base:",
            )
            id = input("player's id: ")
            if id.isdigit():
                player_choosen = Player.get(int(id))
                if player_choosen:
                    new_rank = input("New rank: ")
                    if new_rank.isdigit():
                        return ChangeRankCommand(player_choosen, new_rank)
            print("Enter the player's id")
