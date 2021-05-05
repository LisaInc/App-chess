from .abc import View


class AddPlayerView(View):
    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Add a new player"

    def display_body(self):
        """Menu."""
        print("Menu")
