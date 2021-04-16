"""Module of a tournament."""


from tinydb import TinyDB

from match import Match
from player import Player
from round import Round


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

    def save(self):
        """Save to the db."""
        for player in self.players:
            player.save()
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
        """Create a round."""
        is_first_round = not self.rounds
        if is_first_round:
            matchs = self.pairing_for_the_first_round()
        else:
            matchs = (
                self.pairing_for_a_round_score()
            )  ### FAIRE EN SORTE QUE LES ID SOIT DE PLAYERS ALLER NTM
        self.rounds.append(Round(matchs))

    def pairing_for_the_first_round(self):
        """Create the first round."""
        players = sorted(self.players, key=lambda player: player.rank)
        half = len(players) // 2
        first, last = players[:half], players[half:]
        matchs = []
        for player1, player2 in zip(first, last):
            match = Match(player1, player2)
            matchs.append(match)
        return matchs

    def pairing_for_a_round_score(self):
        """Create the next round."""
        matchs = []
        players_results_sorted = self.get_players_results(self.players)
        players_whitelist = self.get_whitelist_player()
        while players_results_sorted:
            player_whitelist_sorted = self.get_players_results(
                players_whitelist[players_results_sorted[0]]
            )
            match = Match(players_results_sorted[0], player_whitelist_sorted[0])
            matchs.append(match)
            players_results_sorted.pop(0)
        print(matchs)
        return matchs

    def get_players_results(self, players):
        """
        Return a dict with key=player, value=result of all match for the list of
        players given, sorted from the smallest to the biggest score.
        """
        if type(players[0]) == int:
            players_results = {player_id: 0 for player_id in players}
        elif type(players[0]) == Player:
            players_results = {player.id: 0 for player in players}
        for round in self.rounds:
            for match in round.matchs:
                if match.player1.id in players_results:
                    players_results[match.player1.id] += match.result[match.player1]
                if match.player2.id in players_results:
                    players_results[match.player2.id] += match.result[match.player2]
        return sorted(players_results, key=lambda player: players_results[player])

    def get_whitelist_player(self):
        """Return a dict with key=player, value=list of all the opponents."""
        player_whitelist = {
            player.id: [player2.id for player2 in self.players]
            for player in self.players
        }
        for round in self.rounds:
            for match in round.matchs:
                player_whitelist[match.player1.id].remove(match.player2.id)
                player_whitelist[match.player1.id].remove(match.player1.id)
                player_whitelist[match.player2.id].remove(match.player1.id)
                player_whitelist[match.player2.id].remove(match.player2.id)
        return player_whitelist


if __name__ == "__main__":
    player1 = Player("1", "cc", "21/02/2000", "f", 100)
    player2 = Player("2", "cc", "21/02/2000", "f", 80)
    player3 = Player("3", "cc", "21/02/2000", "f", 70)
    player4 = Player("4", "cc", "21/02/2000", "f", 60)
    player5 = Player("5", "cc", "21/02/2000", "f", 50)
    player6 = Player("6", "cc", "21/02/2000", "f", 40)
    player7 = Player("7", "cc", "21/02/2000", "f", 30)
    player8 = Player("8", "cc", "21/02/2000", "f", 20)
    """match = Match(player1, player2)
    match2 = Match(player1, player2)
    match.add_result(0, 1)
    match2.add_result(1, 0)
    # match.save()
    # match2.save()
    round = Round([match])
    round2 = Round([match2])
    round.add_endtime()
    round2.add_endtime()
    # round.save()
    # round2.save()"""
    tournament = Tournament(
        "t1",
        "ville",
        "01/01/2021",
        "01/01/2021",
        [player1, player2, player3, player4, player5, player6, player7, player8],
        "blitz",
        2,
    )

    tournament.save()
    # tournament1 = Tournament.get(1)

    tournament.pairing_for_a_round()
    tournament.rounds[0].matchs[0].add_result(1, 0)
    tournament.rounds[0].matchs[1].add_result(1, 0)
    tournament.rounds[0].matchs[2].add_result(1, 0)
    tournament.rounds[0].matchs[3].add_result(1, 0)
    tournament.pairing_for_a_round()
    tournament.rounds[1].matchs[0].add_result(1, 0)
    tournament.rounds[1].matchs[1].add_result(1, 0)
    tournament.rounds[1].matchs[2].add_result(1, 0)
    tournament.rounds[1].matchs[3].add_result(1, 0)
    tournament.save()
    print(tournament)
