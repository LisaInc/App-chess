from pprint import pprint


def get_round(base_players, blacklist):
    players_to_match = base_players.copy()
    round = []
    while players_to_match:
        p1 = players_to_match.pop(0)
        for p2 in players_to_match:
            match = (p1, p2)
            if match not in blacklist:
                round.append(match)
                blacklist.append(match)
                players_to_match.pop(players_to_match.index(p2))
                break
    return round


def get_rounds(base_players):
    blacklist = []
    return [get_round(base_players, blacklist) for _ in range(7)]


def set_rounds(players):
    rounds = get_rounds(players)
    best_difference = 99999
    best_round = []
    for round in rounds:
        difference = sum(abs(p1[1] - p2[1]) for p1, p2 in round)
        if difference < best_difference:
            best_difference = difference
            if round not in rounds_blacklist:
                best_round = round
    rounds_blacklist.append(best_round)
    return best_round


players = [(index, 0) for index in list(range(8))]
rounds_blacklist = []
rounds = set_rounds(players)
pprint(rounds)


def pairing_for_a_round_score(self):
    """Create the next round."""
    matchs = []
    players_results_sorted = self.get_players_results(self.players)
    players_whitelist = self.get_whitelist_player()
    while players_results_sorted:
        player_whitelist_sorted = self.get_players_results(
            players_whitelist[players_results_sorted[0]]
        )
        for i in range(8):
            if player_whitelist_sorted[i] in players_results_sorted:
                print(i)
                match = Match(
                    Player.get(players_results_sorted[0]),
                    Player.get(player_whitelist_sorted[0]),
                )
                ### Creation de tous les rounds possibles
                ### Calcul de la différences de score entre les joueur total
                #### Si ce round est meilleur on le garde
                #### Sinon on créé un autre round
                matchs.append(match)
                players_results_sorted.pop(
                    players_results_sorted.index(player_whitelist_sorted[0])
                )
                players_results_sorted.pop(0)
                break
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
        player.id: [player2.id for player2 in self.players] for player in self.players
    }
    for round in self.rounds:
        for match in round.matchs:
            player_whitelist[match.player1.id].remove(match.player2.id)
            player_whitelist[match.player1.id].remove(match.player1.id)
            player_whitelist[match.player2.id].remove(match.player1.id)
            player_whitelist[match.player2.id].remove(match.player2.id)
    return player_whitelist
