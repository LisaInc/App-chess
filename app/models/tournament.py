"""Module of a tournament."""


from tinydb import TinyDB
from player import Player
from round import Round
from match import Match


class Tournament:
    """Class of a tournament."""

    db = TinyDB("db.json")
    tournament_table = db.table("tournament")

    def __init__(
        self,
        name,
        location,
        date_start,
        date_end,
        players,
        time_control,
        nb_rounds=4,
        rounds=None,
        description=None,
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
        """Save to the db."""
        self.id = self.tournament_table.insert(
            {
                "name": self.name,
                "location": self.location,
                "date_start": self.date_start,
                "date_end": self.date_end,
                "rounds": ",".join(str(round.id) for round in self.rounds),
                "players": ",".join(str(player.id) for player in self.players),
                "time_control": self.time_control,
                "description": self.description,
            }
        )
        for player in self.players:
            player.save()
        for round in self.rounds:
            round.save()

    def __str__(self):
        """Return the attribute of the tournament when print is use."""
        details = (
            f"{self.name}, à {self.location} "
            f"du {self.date_start} au {self.date_end}, \n"
            f"Contrôle du temps: {self.time_control}\n"
        )
        for i, round in enumerate(self.rounds, start=1):
            details += f"Round {i}: \n {round}"
        return details

    @classmethod
    def get(cls, id: int):
        """Return the tournament from the id."""
        tournament_id = cls.tournament_table.get(doc_id=id)
        if tournament_id:
            tournament_id = cls.deserialized(tournament_id)
            players_id = tournament_id.players.split(",")
            players = [Player.get(int(player)) for player in players_id]
            rounds_id = tournament_id.rounds.split(",")
            rounds = [Round.get(int(round)) for round in rounds_id]
            tournament = Tournament(
                tournament_id.name,
                tournament_id.location,
                tournament_id.date_start,
                tournament_id.date_end,
                players,
                tournament_id.time_control,
                tournament_id.nb_rounds,
                rounds,
                tournament_id.description,
            )
            tournament.id = id
            return tournament
        else:
            return None

    @classmethod
    def deserialized(cls, tournament_info):
        """Get a dictionnary and return a player obj."""
        return Tournament(**tournament_info)

    def pairing_for_a_round(self):
        if len(self.rounds) == 1:
            sorted_players = self.players.sort(key=lambda player: player.rank)
            players = sorted(self.players, key=lambda player: player.rank)
            print(players)


if __name__ == "__main__":
    player1 = Player("cc", "jm", "21/02/2000", "f", 1)
    # player1.save()
    player2 = Player("cc", "cc", "21/02/2000", "f", 0)
    # player2.save()
    match = Match(player1, player2)
    match2 = Match(player1, player2)
    match.add_result(0, 1)
    match2.add_result(1, 0)
    # match.save()
    # match2.save()
    round = Round([match, match2])
    round2 = Round([match2, match])
    round.add_endtime()
    round2.add_endtime()
    # round.save()
    # round2.save()
    tournament = Tournament(
        "t1",
        "ville",
        "01/01/2021",
        "01/01/2021",
        [player1, player2],
        "blitz",
        2,
        [round],
        "waw description",
    )

    # tournament.save()
    tournament1 = Tournament.get(1)
    print(tournament)
    tournament.pairing_for_a_round()
