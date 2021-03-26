"""Player module."""

from tinydb import TinyDB, Query, where


class Player:
    """
    Class of a player with his full name, birth's date, sex, rank and id that will be
    the primary key in the database.
    """

    db = TinyDB("db.json")
    players_table = db.table("players")

    def __init__(
        self, first_name: str, last_name: str, birth: str, sex: str, rank: int
    ):
        """All the attributes of a player."""
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.sex = sex
        self.rank = rank
        self.id = None

    def save(self):
        self.id = self.db.insert(
            {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "birth": self.birth,
                "sex": self.sex,
                "rank": self.rank,
            }
        )

    def __str__(self):
        """Return the attribute of the player when print is use."""
        return f"{self.first_name} {self.last_name} \
            Date de naissance: {self.birth} \
            Sexe: {self.sex} \
            Rang: {self.rank}"

    @classmethod
    def get(cls, id: int):
        """Return tha player from the id."""
        player = cls.db.get(doc_id=id)
        if player:
            player = cls.deserialized(player)
            player.id = id
            return player
        else:
            return None

    @classmethod
    def deserialized(cls, player_info):
        """Get a dictionnary and return a player obj"""
        return Player(**player_info)

    def print_rank(self):
        return f"{self.first_name} {self.last_name} \t {self.rank}"


if __name__ == "__main__":
    player = Player("cc", "jm", "21/02/2000", "f", 0)
    print(player)
    # player.save()
    id = player.id
    player1 = Player.get(id)
    print(player1)
