"""App module."""

from app.controllers import (
    Controller,
    MainPageController,
    AddPlayerController,
    NewTournamentController,
)


class Application:
    """Application context.

    Use the strategy pattern.
    Attrs:
    - controller (Controller): the "strategy". Handle a page in the application.
    - running (bool): True if the application is running else False.
    """

    possible_path = {
        "mainpage": MainPageController,
        "addplayer": AddPlayerController,
        "newtournament": NewTournamentController,
    }

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
        """Change the controller of the app."""
        self.controller = self.possible_path[choice]()
