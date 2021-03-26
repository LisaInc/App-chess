"""Module of a match."""

from tinydb import TinyDB
from player import Player


class Match:
    """Class of a match from a round."""

    db = TinyDB("db.json")
    players_table = db.table("match")

    def __init__(self, player1, player2, *result):
        """All the attribute of a match"""
        self.player1 = player1  # tuple ?
        self.player2 = player2
        for r in result:
            self.result = r

    def add_result(self, result):
        """Add the result"""
        self.result = result

    def save(self):
        """Save to the db"""
        self.id = self.db.insert(
            {
                "player1": self.player1.id,
                "player2": self.player2.id,
                "result": self.result,
            }
        )

    def __str__(self):
        """Return the attribute of the match when print is use."""
        if hasattr(self, "result"):
            return f"{self.player1.__str__()}\n{self.player2.__str__()} \n\
                        Result: {self.result}\n"
        else:
            return f"{self.player1.__str__()}\n{self.player2.__str__()} \n"

    @classmethod
    def get(cls, id: int):
        """Return tha player from the id."""
        match = cls.db.get(doc_id=id)
        if match:
            match = cls.deserialized(match)
            match.id = id
            return match
        else:
            return None

    @classmethod
    def deserialized(cls, match_info):
        """Get a dictionnary and return a player obj"""
        return Match(**match_info)


if __name__ == "__main__":
    player1 = Player.get(1)
    player2 = Player.get(8)
    match = Match(player1, player2, "0-1")
    # print(match)
    # match.add_result("0-1")
    match2 = Match.get(9)
    print(match2)
    # match.save()
