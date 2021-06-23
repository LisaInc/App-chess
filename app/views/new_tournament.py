"""Start a new tournament."""

from app.commands.navigation import NavigationCommand
import re
from rich.table import Table
from rich.console import Console

from app.commands.new_tournament import NewTournamentCommand
from app.models.player import Player

from .abc import View


class NewTournamentView(View):
    """Start a new tournament."""

    def __init__(self):
        """Init."""
        super().__init__()
        self.title = "Start a new tournament"

    def get_command(self):
        """Ask the user about the info."""
        while len(Player.table.all()) < 8:
            choice = input(
                "Not enough player in the database,\n\
                press 1 to generate a random tournament with random players\n\
                press 2 to go to the main page:"
            )
            if choice == "1":
                return NewTournamentCommand(None)
            elif choice == "2":
                return NavigationCommand("mainpage")
            else:
                print("Press 1 or 2")
        self.tournament_data = {
            "name": input(
                "Title of the tournament (leave empty to generate a random tornament):"
            )
        }
        if not self.tournament_data["name"]:
            return NewTournamentCommand(None)
        self.tournament_data["location"] = input("Location:")
        self.tournament_data["date_start"] = input("Start date (yyyy/mm/dd):")
        self.tournament_data["date_end"] = input("End date (yyyy/mm/dd):")
        self.tournament_data["time_control"] = input(
            "Time control (Bullet, Blitz, Speed chess):"
        )
        self.tournament_data["description"] = (input("Description (optional):"),)

        self.check_data_tournement()
        players = []
        while len(players) < 8:
            table = Table(title="Player regitered in the database")
            print("Choose a player from the list:")
            table.add_column("ID", style="blue")
            table.add_column("Informations", style="magenta")
            for player in Player.all():
                table.add_row(player.id, player.name)  ####TEST FINI ICI
            id = input("Player's id:")
            if id.isdigit():
                players.add[Player.get(id)]
        return NewTournamentCommand(self.tournament_data)

    def check_data_tournement(self):
        """Check the input."""
        correct_info = False
        while not correct_info:
            correct_info = True
            if not re.search("\d{4}/\d{2}/\d{2}", self.tournament_data["date_start"]):
                self.tournament_data["date_start"] = self.ask_again(
                    "start day (yyyy/mm/dd)"
                )
                correct_info = False
            if not re.search("\d{4}/\d{2}/\d{2}", self.tournament_data["date_end"]):
                self.tournament_data["date_end"] = self.ask_again(
                    "end day (yyyy/mm/dd)"
                )
                correct_info = False
            if self.tournament_data["time_control"].lower() not in [
                "bullet",
                "blitz",
                "speed chess",
            ]:
                self.tournament_data["time_control"] = self.ask_again(
                    "time control (Bullet, Blitz, Speed chess)"
                )
                correct_info = False

    @classmethod
    def ask_again(self, wrong_info):
        """Ask the user to write again one player's information."""
        return input(f"Wrong {wrong_info}, please try again: ")
