"""Module of a round."""

from tinydb import TinyDB
from datetime import date
from random import choice

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

    def is_ended(self):
        for match in self.matchs:
            if not match.result:
                return False
        return True

    def auto_play(self):
        choices = [(0, 1), (1, 0), (0.5, 0.5)]
        for match in self.matchs:
            match.add_result(*choice(choices))


if __name__ == "__main__":
    liste = []
    for _ in range(2):
        players = [Player.auto_init() for _ in range(2)]
        for player in players:
            player.save()
        liste.append(Match(players[0], players[1]))
    round = Round(liste)
    round.save()
    round = round.get(1)
    round.matchs[0].add_result(0, 1)
    round.add_endtime()
    for match in round.matchs:
        print(match.result)
