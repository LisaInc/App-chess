"""Module of a match."""

from tinydb import TinyDB
from player import Player


class Match:
    """Class of a match from a round."""

    db = TinyDB("db.json")
    match_table = db.table("match")

    def __init__(self, player1, player2, result={}):
        """All the attribute of a match."""
        self.player1 = player1
        self.player2 = player2
        self.result = result
        self.id = None

    def add_result(self, result_player1, result_player2):
        """Add the result."""
        self.result[self.player1] = result_player1
        self.result[self.player2] = result_player2
        self.player1.score += 1
        self.player2.score += 1

    def save(self):
        """Save to the db."""
        if self.id:
            self.update()
        else:
            self.id = self.match_table.insert(
                {
                    "player1": self.player1.id,
                    "player2": self.player2.id,
                    "result": (self.result[self.player1], self.result[self.player2]),
                }
            )

    def update(self):
        """Update the db."""
        self.match_table.remove(self.id)
        self.save()

    def __str__(self):
        """Return the attribute of the match when print is use."""
        if hasattr(self, "result"):
            return f"{self.player1} Result: {self.result[self.player1]}\n\
{self.player2} Result: {self.result[self.player2]}\n"
        else:
            return f"{self.player1}\n{self.player2}\n"

    @classmethod
    def get(cls, id: int):
        """Return the match from the id."""
        match_id = cls.match_table.get(doc_id=id)
        if match_id:
            match_id = cls.deserialized(match_id)

            match = Match(Player.get(match_id.player1), Player.get(match_id.player2))
            match.id = match_id.id

            match.add_result(match_id.result[0], match_id.result[1])
            return match
        else:
            return None

    @classmethod
    def deserialized(cls, match_info):
        """Get a dictionnary and return a match obj."""
        return Match(**match_info)


if __name__ == "__main__":
    player1 = Player.get(1)
    player2 = Player.get(2)
    match = Match(player1, player2)
    # print(match)
    match.add_result(0, 1)
    match2 = Match.get(match.id)
    match.save()
    print(match2)
