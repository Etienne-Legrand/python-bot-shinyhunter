import time
from colorama import init
from src.ui import print_title
from src.config import setup_configuration
from src.pokemon_hunter import hunt_shiny_pokemon

def main():
    init()  # Initialiser colorama
    print_title()
    
    advance_key, reset_key, game_region = setup_configuration()
    hunt_shiny_pokemon(advance_key, reset_key, game_region)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramme arrêté par l'utilisateur.")
