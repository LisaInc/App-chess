from models import Player


def print_match_players(match):
    """Print the two player of a match."""
    print(f"{match.player1}\n\nis playing against\n\n{match.player2}")


def print_players_rank(tournament):
    """Print the rank of all the players in the tornament."""
    for player_id in tournament.players_id:
        player = Player.get_player_from_id(player_id)
        print(Player.print_rank(player))
