from .abc import View


class AddPlayerView(View):
    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Add a new player"

    def display_body(self):
        """Menu."""
        name = input("Please enter the full name:\tleave blanc for a random new player")
        birth = input("Date of birth (yyyy/mm/dd):")
