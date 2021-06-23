"""Module of a tournament."""


import datetime
from faker import Faker
from random import choice
from tinydb import TinyDB
from datetime import date

from .match import Match
from .player import Player
from .round import Round
from .db import DB


class Tournament(DB):
    """Class of a tournament."""

    db = TinyDB("db.json")
    table = db.table("tournament")
    rounds_played_blacklist = []

    def __init__(
        self,
        name,
        location,
        date_start,
        date_end,
        players,
        time_control,
        nb_rounds=4,
        rounds=[],
        description=None,
        id=None,
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
        self.id = id

    def auto_init():
        """All the attributes of a player."""
        fake = Faker()
        city = fake.city()
        name = city + "tournament"
        time_control = choice(["Bullet", "Blitz", "Speed chess"])
        players = [Player.auto_init() for _ in range(8)]
        date = str(datetime.date.today())
        return Tournament(name, city, date, date, players, time_control)

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

    def serialized(self):
        """Return the match serialized."""
        return {
            "name": self.name,
            "location": self.location,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "nb_rounds": self.nb_rounds,
            "rounds": [round.id for round in self.rounds],
            "players": [player.id for player in self.players],
            "time_control": self.time_control,
            "description": self.description,
        }

    @classmethod
    def deserialized(cls, info):
        """Get a dictionnary and return a match obj."""
        return Tournament(
            info["name"],
            info["location"],
            info["date_start"],
            info["date_end"],
            [Player.get(player_id) for player_id in info["players"]],
            info["time_control"],
            info["nb_rounds"],
            [Round.get(round_id) for round_id in info["rounds"]],
            info["description"],
            info.doc_id,
        )

    def save(self):
        """Save a tournament."""
        for player in self.players:
            player.save()
        for round in self.rounds:
            round.save()
        super().save()

    def pairing_for_a_round(self):
        """Create a round."""
        is_first_round = not self.rounds
        matchs = self.set_first_round() if is_first_round else self.set_rounds()
        self.rounds.append(Round(matchs))
        for match in matchs:
            self.rounds_played_blacklist.append((match.player1, match.player2))

    def set_first_round(self):
        """Create the first round."""
        players = sorted(self.players, key=lambda player: player.rank)
        half = len(players) // 2
        first, last = players[:half], players[half:]
        matchs = []
        for player1, player2 in zip(first, last):
            match = Match(player1, player2)
            matchs.append(match)
        return matchs

    def get_rounds(self):
        """Create a round from the scorethat does not already exist."""
        blacklist = []
        rounds = []
        for _ in range(7):
            players_to_match = self.players.copy()
            round = []
            while players_to_match:
                p1 = players_to_match.pop(0)
                for p2 in players_to_match:
                    match = Match(p1, p2)
                    if (p1, p2) not in blacklist:
                        round.append(match)
                        blacklist.append((p1, p2))
                        players_to_match.pop(players_to_match.index(p2))
                        break
            rounds.append(round)
        return rounds

    def set_rounds(self):
        """Select the best round from all the rounds possible."""
        rounds = self.get_rounds()
        best_difference = 99999
        best_round = []
        for matchs in rounds:
            difference = sum(
                abs(match.player1.score - match.player2.score) for match in matchs
            )
            if difference < best_difference:
                for match in matchs:
                    pairing = (match.player1, match.player2)
                    if pairing not in self.rounds_played_blacklist:
                        best_round = matchs
                        best_difference = difference
        return best_round


if __name__ == "__main__":
    players = [Player.auto_init() for _ in range(8)]
    for player in players:
        player.save()
    date = "01/01/2021"
    tournament = Tournament("t1", "ville", date, date, players, "blitz")

    choices = [(0, 1), (1, 0), (0.5, 0.5)]
    for _ in range(tournament.nb_rounds):
        tournament.pairing_for_a_round()
        round = tournament.rounds[-1]
        for match in round.matchs:
            match.add_result(*choice(choices))
            tournament.rounds[0].add_endtime()
        round.add_endtime()
    tournament.save()
    tournament1 = Tournament.get(1)
    print(tournament1)

    Tournament1 = Tournament.auto_init()
    Tournament1.save()
