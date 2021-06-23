"""Module of a round."""

from tinydb import TinyDB
from datetime import date

from .match import Match
from .player import Player
from .db import DB


class Round(DB):
    """Class of a round from a tournament."""

    db = TinyDB("db.json")
    table = db.table("round")

    def __init__(
        self, matchs: list, start_time=str(date.today()), end_time=None, id=None
    ):
        """All the attributes of a round."""
        self.matchs = matchs
        self.start_time = start_time
        self.end_time = end_time
        self.id = id

    def __str__(self):
        """Return the attribute of the round when print is use."""
        string = "Match:\n".join(str(match) for match in self.matchs)
        return (
            "Match:\n"
            + string
            + "Début du round:"
            + self.start_time
            + "\nFin du round:"
            + self.end_time
            + "\n"
        )

    def add_endtime(self):
        """Set the end time."""
        self.end_time = str(date.today())

    def serialized(self):
        """Return the match serialized."""
        return {
            "matchs": [match.id for match in self.matchs],
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

    @classmethod
    def deserialized(cls, info):
        """Get a dictionnary and return a match obj."""
        return Round(
            [Match.get(match_id) for match_id in info["matchs"]],
            info["start_time"],
            info["end_time"],
            info.doc_id,
        )

    def save(self):
        """Save the round in he DB."""
        for match in self.matchs:
            match.save()
        super().save()


if __name__ == "__main__":
    player1 = Player.auto_init()
    player2 = Player.auto_init()
    match = Match(player1, player2)
    match2 = Match(player1, player2)
    match.add_result(1, 1)
    match2.add_result(1, 0)
    liste = [match, match2]
    round = Round(liste)
    round.add_endtime()

    round.save()
    print(round)
