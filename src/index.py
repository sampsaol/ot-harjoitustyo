from ui import UserInterface
from command_io import ConsoleIO

def main():
    start_generator = UserInterface(ConsoleIO())
    start_generator.start()


if __name__ == "__main__":
    main()