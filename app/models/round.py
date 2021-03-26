"""Module of a round."""

from tinydb import TinyDB
from match import Match
from player import Player


class Round:
    """Class of a round from a tournament."""

    db = TinyDB("db.json")
    players_table = db.table("match")

    def __init__(self, matchs: list):
        """All the attributes of a round."""
        self.matchs = matchs

    def save(self):
        """Save to the db"""
        self.id = self.db.insert({"matchs": self.matchs})

    def __str__(self):
        """Return the attribute of the round when print is use."""
        string = ""
        for match in self.matchs:
            string += match.__str__()
        return string


if __name__ == "__main__":
    player1 = Player.get(1)
    player2 = Player.get(8)
    match = Match(player1, player2, "0-1")
    match2 = Match(player1, player2, "1-0")
    liste = [match, match2]
    round = Round(liste)
    match.add_result("0-1")
    print(round)
    # match.save()
