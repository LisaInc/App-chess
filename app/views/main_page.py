from .abc import PageView


class MainPageView(PageView):
    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Main Page"

    def display_body(self):
        """Menu."""
        print("Menu")
