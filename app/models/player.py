"""Player module."""

from tinydb import TinyDB


class Player:
    """Class of a player with his full name, birth's date, sex, rank and id."""

    db = TinyDB("db.json")
    players_table = db.table("players")

    def __init__(
        self,
        first_name: str,
        last_name: str,
        birth: str,
        sex: str,
        rank: int,
        score=0,
    ):
        """All the attributes of a player."""
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.sex = sex
        self.rank = rank
        self.id = None
        self.score = score
        self.save()

    def save(self):
        """Save to the db."""
        self.id = self.players_table.insert(
            {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "birth": self.birth,
                "sex": self.sex,
                "rank": self.rank,
            }
        )

    def print_details(self):
        """Return the attribute of the player when print is use."""
        return f"{self.first_name} \t{self.last_name} \tDate de naissance: \
            {self.birth} \tSexe: {self.sex} \tRang: {self.rank}"

    def __repr__(self):
        """Repr."""
        return str(self)

    @classmethod
    def get(cls, id: int):
        """Return tha player from the id."""
        player = cls.players_table.get(doc_id=id)
        if player:
            player = cls.deserialized(player)
            player.id = id
            return player
        else:
            return None

    @classmethod
    def deserialized(cls, player_info):
        """Get a dictionnary and return a player obj."""
        return Player(**player_info)

    def __str__(self):
        """Get the rank of the player."""
        return f"{self.id} {self.first_name} {self.last_name} \t {self.rank}"


if __name__ == "__main__":
    player = Player("cc", "jm", "21/02/2000", "f", 0)
    print(player)

    id = player.id
    player1 = Player.get(1)
    print(player1)
