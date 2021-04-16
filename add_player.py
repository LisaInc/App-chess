from .abc import View


class Add_player(View):
    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Add player"

    def display_body(self):
        """Display the books."""
        print(
            "Menu:\
            1 - New tournament\
            2 - Add player\
            3 - View HistoryCommand"
        )