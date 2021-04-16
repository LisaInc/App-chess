from .abc import View


class MainPageView(View):
    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Main Page"

    def display_body(self):
        """Display the books."""
        print("Menu")
