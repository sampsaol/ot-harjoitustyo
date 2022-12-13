from ui.ui import UserInterface
from command_io import ConsoleIO
from services.character_service import CharacterService


def main():
    """The function that defines the IO and the used service and starts running the program
    """
    console = ConsoleIO()
    service = CharacterService()
    start_generator = UserInterface(console, service)
    start_generator.start()


if __name__ == "__main__":
    main()
