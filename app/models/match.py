"""Module of a match."""

from tinydb import TinyDB

from .player import Player
from .db import DB


class Match(DB):
    """Class of a match from a round."""

    db = TinyDB("db.json")
    table = db.table("match")

    def __init__(self, player1, player2, result={}, id=None):
        """All the attribute of a match."""
        self.player1 = player1
        self.player2 = player2
        self.result = result
        self.id = id

    def add_result(self, result_player1, result_player2):
        """Add the result."""
        self.result[str(self.player1.id)] = result_player1
        self.result[str(self.player2.id)] = result_player2
        self.player1.score += result_player1
        self.player2.score += result_player2

    def __str__(self):
        """Return the attribute of the match when print is use."""
        if self.result:
            return (
                f"{self.player1} Result: {self.result[str(self.player1.id)]}\n"
                f"{self.player2} Result: {self.result[str(self.player2.id)]}\n"
            )
        else:
            return f"{self.player1}\n{self.player2}\n"

    def serialized(self):
        """Return the match serialized."""
        if self.result:
            return {
                "player1": self.player1.id,
                "player2": self.player2.id,
                "result": (
                    self.result[str(self.player1.id)],
                    self.result[str(self.player2.id)],
                ),
            }
        return {
            "player1": self.player1.id,
            "player2": self.player2.id,
            "result": {},
        }

    @classmethod
    def deserialized(cls, info):
        """Get a dictionnary and return a match obj."""
        match = Match(
            Player.get(int(info["player1"])),
            Player.get(int(info["player2"])),
            {},
            info.doc_id,
        )
        if info["result"]:
            result_p1, result_p2 = info["result"]
            match.add_result(result_p1, result_p2)
        return match


if __name__ == "__main__":
    player1 = Player.auto_init()
    player2 = Player.auto_init()
    DB.save(player1)
    DB.save(player2)
    match = Match(player1, player2)
    print(match)
    match.add_result(0, 1)
    DB.save(match)
    match2 = Match.get(1)
    match.save()

    print(match2)
