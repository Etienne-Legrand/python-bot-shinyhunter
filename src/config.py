import time
import pyautogui
import keyboard
from colorama import Fore, Style

def get_key_input(prompt):
    """Fonction pour obtenir une entrée de touche de l'utilisateur valide."""
    while True:
        print(prompt, end="")
        key = input().strip().lower()
        
        # Tester si la touche est valide sans l'appuyer réellement
        try:
            keyboard.key_to_scan_codes(key)
            return key
        except ValueError:
            print(f"{Fore.RED}Erreur: '{key}' n'est pas une touche valide. Veuillez réessayer.{Style.RESET_ALL}")

def define_search_region():
    """Permet à l'utilisateur de définir une région de l'écran à surveiller."""
    print(f"{Fore.CYAN}Pour définir une région, placez votre souris au coin supérieur gauche et pressez Entrée,{Style.RESET_ALL}")
    print(f"{Fore.CYAN}puis placez-la au coin inférieur droit et pressez Entrée à nouveau.{Style.RESET_ALL}")
    
    input()
    pos1 = pyautogui.position()
    print(f"Position 1: {pos1}")
    input()
    pos2 = pyautogui.position()
    print(f"Position 2: {pos2}")
    
    x = min(pos1.x, pos2.x)
    y = min(pos1.y, pos2.y)
    width = abs(pos2.x - pos1.x)
    height = abs(pos2.y - pos1.y)
    
    return (x, y, width, height)


def setup_configuration():
    """Configure les paramètres du bot."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Configuration des touches pour le bot{Style.RESET_ALL}")
    advance_key = get_key_input("Entrez la touche pour avancer dans les cinématiques (par exemple: a, z, e, space): ")
    reset_key = get_key_input("Entrez la touche pour réinitialiser la partie si le Pokémon n'est pas shiny: ")
    
    game_region = None
    if get_key_input(f"\n{Fore.CYAN}{Style.BRIGHT}Voulez-vous configurer une région spécifique pour la recherche? (o/n){Style.RESET_ALL} ") == 'o':
        print(f"{Fore.YELLOW}Configurez la région pour le jeu Pokémon (pressez Entrée pour commencer):{Style.RESET_ALL}")
        game_region = define_search_region()
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Préparation pour la capture d'écran{Style.RESET_ALL}")
    print("Cliquez sur l'émulateur du jeu pour commencer (vous avez 5 secondes pour cliquer)...")
    time.sleep(5)
    
    return advance_key, reset_key, game_region
