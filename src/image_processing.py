import cv2
import numpy as np
import pyautogui
from colorama import Fore, Style

def load_template(template_path):
    """Charge l'image template et affiche une erreur si nécessaire."""
    template = cv2.imread(template_path)
    if template is None:
        print(f"{Fore.RED}Erreur: Impossible de charger l'image {template_path}{Style.RESET_ALL}")
    return template


def capture_screenshot(region=None):
    """Capture une zone de l'écran et la convertit au format BGR."""
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    return cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)


def find_template_multi_scale(template_path, confidence=0.7, region=None, min_scale=0.2, max_scale=1.0):
    """
    Trouve un modèle à différentes échelles dans une capture d'écran.
    Retourne la position et la taille si trouvé, None sinon.
    """
    template = load_template(template_path)
    if template is None:
        return None
    
    screenshot = capture_screenshot(region)
    
    # Obtenir les dimensions
    template_height, template_width = template.shape[:2]
    screenshot_height, screenshot_width = screenshot.shape[:2]
    
    # Convertir en niveaux de gris pour le template matching
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    # Définir la plage d'échelles à tester
    num_scales = int((max_scale - min_scale) / 0.1) + 1
    scales = np.linspace(min_scale, max_scale, num_scales)
    
    best_match = None
    best_val = -1
    
    # Pour chaque échelle, essayer de trouver le template
    for scale in scales:
        scale_width = int(template_width * scale)
        scale_height = int(template_height * scale)
        
        if scale_width > screenshot_width or scale_height > screenshot_height:
            continue
        
        resized_template = cv2.resize(gray_template, (scale_width, scale_height), interpolation=cv2.INTER_AREA)
        result = cv2.matchTemplate(gray_screenshot, resized_template, cv2.TM_CCOEFF_NORMED)
        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val >= confidence and max_val > best_val:
            best_val = max_val
            
            # Ajuster les coordonnées si une région est spécifiée
            x, y = max_loc
            if region:
                x += region[0]
                y += region[1]
            
            best_match = (x, y, scale_width, scale_height, max_val)
    
    return best_match


def check_pokemon_type(shiny_img, normal_img, game_region):
    """Vérifie si un Pokémon shiny ou normal est visible à l'écran."""
    try:
        print(f"{Fore.YELLOW}Recherche de shiny...{Style.RESET_ALL}")
        shiny_location = find_template_multi_scale(shiny_img, region=game_region)
        
        if shiny_location:
            return "shiny", shiny_location
        
        print(f"{Fore.YELLOW}Recherche de normal...{Style.RESET_ALL}")
        normal_location = find_template_multi_scale(normal_img, region=game_region)
        
        if normal_location:
            return "normal", normal_location
        
        return None, None
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de la détection d'image: {e}{Style.RESET_ALL}")
        return None, None
