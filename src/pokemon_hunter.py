import time
import threading
import pydirectinput
from colorama import Fore, Style
from src.ui import print_shiny_found
from src.image_processing import check_pokemon_type

# Constantes pour les chemins des images
NORMAL_POKEMON_IMG = "src/images/normal_pokemon.png"
SHINY_POKEMON_IMG = "src/images/shiny_pokemon.png"

def key_presser(key, stop_event, interval=1/3):
    """Fonction qui appuie sur une touche à intervalles réguliers tant que l'événement stop est désactivé."""
    while not stop_event.is_set():
        pydirectinput.press(key)
        time.sleep(interval)

def start_key_pressing_thread(key, interval=1/3):
    """Démarre un thread d'appui sur les touches et retourne le thread et l'événement d'arrêt."""
    stop_event = threading.Event()
    key_thread = threading.Thread(target=key_presser, args=(key, stop_event, interval))
    key_thread.daemon = True
    key_thread.start()
    return key_thread, stop_event

def stop_key_pressing_thread(key_thread, stop_event):
    """Arrête proprement un thread d'appui sur les touches."""
    stop_event.set()
    key_thread.join(timeout=1)

def search_pokemon(normal_img, shiny_img, game_region, advance_key):
    """Recherche un Pokémon à l'écran tout en appuyant sur la touche d'avancement."""
    # Démarrer le thread d'appui sur les touches
    key_thread, stop_event = start_key_pressing_thread(advance_key)
    
    try:
        # Rechercher le Pokémon pendant que le thread appuie sur les touches
        pokemon_type, location = check_pokemon_type(shiny_img, normal_img, game_region)
        return pokemon_type, location
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de la recherche: {e}{Style.RESET_ALL}")
        return None, None
    finally:
        # Toujours arrêter le thread, même en cas d'erreur
        stop_key_pressing_thread(key_thread, stop_event)

def hunt_shiny_pokemon(advance_key, reset_key, game_region):
    """Fonction principale pour la chasse aux Pokémon shiny."""
    print(f"{Fore.GREEN}{Style.BRIGHT}Le bot a commencé! Recherche de Pokémon shiny en cours...{Style.RESET_ALL}")

    attempts = 0
    while True:
        attempts += 1
        print(f"{Fore.BLUE}{Style.BRIGHT}Tentative #{Style.RESET_ALL} {Fore.BLUE}{Style.BRIGHT}{attempts}{Style.RESET_ALL}")

        # Continuer à chercher jusqu'à ce qu'un Pokémon soit trouvé
        pokemon_found = False
        while not pokemon_found:
            pokemon_type, _ = search_pokemon(NORMAL_POKEMON_IMG, SHINY_POKEMON_IMG, game_region, advance_key)
            if pokemon_type:
                pokemon_found = True
        
        # Traiter le résultat et vérifier s'il faut arrêter la boucle
        if pokemon_type == "shiny":
            print_shiny_found(attempts)
            break
        elif pokemon_type == "normal":
            print(f"{Fore.RED}Pokémon normal trouvé. Réinitialisation...{Style.RESET_ALL}")
            pydirectinput.press(reset_key)
            time.sleep(1)
