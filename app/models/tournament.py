"""Module of a tournament."""


from tinydb import TinyDB
from player import Player
from round import Round
from match import Match


class Tournament:
    """Class of a tournament."""

    db = TinyDB("db.json")
    players_table = db.table("tournament")

    def __init__(
        self,
        name,
        location,
        date_start,
        date_end,
        nb_rounds,
        rounds,
        players,
        time_control,
        description,
    ):
        """All the attributes of a tournament."""
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.nb_rounds = nb_rounds
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description

    def save(self):
        """Save to the db"""
        self.id = self.db.insert(
            {
                "name": self.name,
                "location": self.location,
                "date_start": self.date_start,
                "date_end": self.date_end,
                "rounds": self.rounds,
                "players": self.players,
                "time_control": self.time_control,
                "description": self.description,
            }
        )

    def __str__(self):
        """Return the attribute of the tournament when print is use."""
        string = f"{self.name}, in {self.location} from the {self.date_start} to the {self.date_end}, \n"
        for i, round in enumerate(self.rounds):
            string += f"Round {i+1}: \n {round.__str__()}"
        return string


if __name__ == "__main__":
    player1 = Player.get(1)
    player2 = Player.get(8)
    match = Match(player1, player2, "0-1")
    match2 = Match(player1, player2, "1-0")
    round = Round([match, match2])
    round2 = Round([match2, match])
    match.add_result("0-1")
    # match.save()
    tournament = Tournament(
        "t1",
        "ville",
        "01/01/2021",
        "01/01/2021",
        2,
        [round, round2],
        [player1, player2],
        "blitz",
        "waw description",
    )
    print(tournament)
    # match.add_result("0-1")
    # print(match)
    # # match.save()