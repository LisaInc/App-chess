"""Module of a tournament."""


import pprint

from tinydb import TinyDB

from match import Match
from player import Player
from round import Round


class Tournament:
    """Class of a tournament."""

    db = TinyDB("db.json")
    tournament_table = db.table("tournament")
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

    def __str__(self):
        """Return the attribute of the tournament when print is use."""
        details = (
            f"{self.name}, à {self.location} "
            f"du {self.date_start} au {self.date_end}, \n"
            f"Contrôle du temps: {self.time_control}\n"
        )
        for i, round in enumerate(self.rounds, start=1):
            print(round, str(i))
            details += f"Round {i}: \n {round}"
        return details

    def save(self):
        """Save to the db."""
        for round in self.rounds:
            round.save()
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

    ########################################################## Create rounds
    def pairing_for_a_round(self):
        """Create a round."""
        is_first_round = not self.rounds
        matchs = self.set_first_round() if is_first_round else self.set_rounds()
        self.rounds.append(Round(matchs))
        for match in matchs:
            self.rounds_played_blacklist.append((match.player1, match.player2))
        print(len(self.rounds_played_blacklist))

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

    def get_round(self, blacklist):
        """Create a round from the scorethat does not already exist."""
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
        return round

    def get_rounds(self):
        """Create all rounds possible."""
        blacklist = []
        return [self.get_round(blacklist) for _ in range(7)]

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
    player1 = Player("1", "cc", "21/02/2000", "f", 100)
    player2 = Player("2", "cc", "21/02/2000", "f", 80)
    player3 = Player("3", "cc", "21/02/2000", "f", 70)
    player4 = Player("4", "cc", "21/02/2000", "f", 60)
    player5 = Player("5", "cc", "21/02/2000", "f", 50)
    player6 = Player("6", "cc", "21/02/2000", "f", 40)
    player7 = Player("7", "cc", "21/02/2000", "f", 30)
    player8 = Player("8", "cc", "21/02/2000", "f", 20)

    tournament = Tournament(
        "t1",
        "ville",
        "01/01/2021",
        "01/01/2021",
        [player1, player2, player3, player4, player5, player6, player7, player8],
        "blitz",
        2,
    )

    tournament.pairing_for_a_round()
    tournament.rounds[0].matchs[0].add_result(1, 0)
    tournament.rounds[0].matchs[1].add_result(1, 0)
    tournament.rounds[0].matchs[2].add_result(1, 0)
    tournament.rounds[0].matchs[3].add_result(1, 0)
    tournament.rounds[0].add_endtime()
    tournament.pairing_for_a_round()
    tournament.rounds[1].matchs[0].add_result(1, 0)
    tournament.rounds[1].matchs[1].add_result(1, 0)
    tournament.rounds[1].matchs[2].add_result(1, 0)
    tournament.rounds[1].matchs[3].add_result(1, 0)
    tournament.rounds[1].add_endtime()
    tournament.pairing_for_a_round()
    tournament.rounds[2].matchs[0].add_result(1, 0)
    tournament.rounds[2].matchs[1].add_result(1, 0)
    tournament.rounds[2].matchs[2].add_result(1, 0)
    tournament.rounds[2].matchs[3].add_result(1, 0)
    tournament.rounds[2].add_endtime()
    tournament.pairing_for_a_round()
    tournament.rounds[3].matchs[0].add_result(1, 0)
    tournament.rounds[3].matchs[1].add_result(1, 0)
    tournament.rounds[3].matchs[2].add_result(1, 0)
    tournament.rounds[3].matchs[3].add_result(1, 0)
    tournament.rounds[3].add_endtime()
    tournament.save()
    print(tournament)
