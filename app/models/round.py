"""Module of a round."""

from tinydb import TinyDB
from match import Match
from player import Player
from datetime import date


class Round:
    """Class of a round from a tournament."""

    db = TinyDB("db.json")
    round_table = db.table("round")

    def __init__(self, matchs: list, start_time=None, end_time=None):
        """All the attributes of a round."""
        self.matchs = matchs
        self.start_time = str(date.today())
        self.end_time = end_time

    def save(self):
        """Save to the db."""
        for match in self.matchs:
            match.save()
        self.id = self.round_table.insert(
            {
                "matchs": ",".join(str(match.id) for match in self.matchs),
                "start_time": self.start_time,
                "end_time": self.end_time,
            }
        )

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

    @classmethod
    def get(cls, id: int):
        """Return the tournament from the id."""
        round_id = cls.round_table.get(doc_id=id)
        if round_id:
            round_id = cls.deserialized(round_id)
            matchs_id = round_id.matchs.split(",")
            matchs = [Match.get(int(match)) for match in matchs_id]
            round = Round(
                matchs,
                round_id.start_time,
                round_id.end_time,
            )
            round.id = id
            return round
        else:
            return None

    @classmethod
    def deserialized(cls, round_info):
        """Get a dictionnary and return a round obj."""
        return Round(**round_info)


if __name__ == "__main__":
    player1 = Player.get(1)
    player2 = Player.get(2)
    match = Match(player1, player2)
    match2 = Match(player1, player2)
    match.add_result(1, 1)
    match2.add_result(1, 0)
    liste = [match, match2]
    round = Round(liste)
    round.add_endtime()

    round.save()
    round1 = Round.get(1)
    print(round1)
