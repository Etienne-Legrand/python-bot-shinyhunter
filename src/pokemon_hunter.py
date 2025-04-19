import time
import keyboard
from colorama import Fore, Style
from src.ui import print_shiny_found
from src.image_processing import check_pokemon_type

def hunt_shiny_pokemon(advance_key, reset_key, game_region):
    """Fonction principale pour la chasse aux Pokémon shiny."""
    normal_pokemon_img = "src/images/normal_pokemon.png"
    shiny_pokemon_img = "src/images/shiny_pokemon.png"
    
    attempts = 0
    print(f"{Fore.GREEN}{Style.BRIGHT}Le bot a commencé! Recherche de Pokémon shiny en cours...{Style.RESET_ALL}")

    while True:
        attempts += 1
        print(f"{Fore.BLUE}{Style.BRIGHT}Tentative #{Style.RESET_ALL} {Fore.BLUE}{Style.BRIGHT}{attempts}{Style.RESET_ALL}")

        # Continuer à avancer jusqu'à ce qu'un Pokémon soit trouvé
        pokemon_found = False
        while not pokemon_found:
            time.sleep(0.5)
            keyboard.press_and_release(advance_key)

            pokemon_type, location = check_pokemon_type(shiny_pokemon_img, normal_pokemon_img, game_region)
            if pokemon_type:
                pokemon_found = True
        
        # Traiter le résultat
        if pokemon_type == "shiny":
            print_shiny_found(attempts)
            break
        elif pokemon_type == "normal":
            print(f"{Fore.RED}Pokémon normal trouvé. Réinitialisation...{Style.RESET_ALL}")
            keyboard.press_and_release(reset_key)
            time.sleep(3)  # Attendre que le jeu se réinitialise
