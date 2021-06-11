"""App module."""

from app.controllers import Controller, MainPageController, AddPlayerController


class Application:
    """Application context.

    Use the strategy pattern.
    Attrs:
    - controller (Controller): the "strategy". Handle a page in the application.
    - running (bool): True if the application is running else False.
    """

    def __init__(self):
        """Initialize the main page."""
        self.controller: Controller = MainPageController()
        self.running = True

    def run(self):
        """Run the application."""
        while self.running:
            self.controller.view.display()
            command = self.controller.get_command()
            command.execute(context=self)

    def change_page(self, choice):
        possible_path = {
            "mainpage": MainPageController,
            "addplayer": AddPlayerController,
        }
        self.controller = possible_path[choice]()
