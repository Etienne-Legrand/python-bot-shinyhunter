# Python - SHINY HUNTER BOT

```
   ███████╗██╗  ██╗██╗███╗   ██╗██╗   ██╗    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗
   ██╔════╝██║  ██║██║████╗  ██║╚██╗ ██╔╝    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
   ███████╗███████║██║██╔██╗ ██║ ╚████╔╝     ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
   ╚════██║██╔══██║██║██║╚██╗██║  ╚██╔╝      ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
   ███████║██║  ██║██║██║ ╚████║   ██║       ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
```

Bot automatisé développé en Python qui permet de détecter des Pokémon shiny dans vos jeux Pokémon en émulation sur PC.

https://github.com/user-attachments/assets/ed2e7048-7908-46aa-a374-33fb57c48729

## Fonctionnalités

- Détecter la présence d'un Pokémon à l'écran.
- Distinguer un Pokémon normal d'un Pokémon shiny.
- Automatiser les séquences d'appui sur les touches pour continuer et reset la sauvegarde.

## Prérequis

1. Python 3+

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Déplacez-vous dans le répertoire du projet
3. Créez et activez un environnement virtuel (recommandé) :

   **Sous Windows :**

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   **Sous macOS/Linux :**

   ```
   python -m venv venv
   source venv/bin/activate
   ```

4. Installez les dépendances nécessaires :

   ```
   pip install -r requirements.txt
   ```

5. Placez vos images de référence dans le dossier `src/images/` :
   - `pokemon-normal.png` - Image du Pokémon normal
   - `pokemon-shiny.png` - Image du Pokémon shiny

## Utilisation

1. Lancez votre émulateur et positionnez-vous avant la rencontre du Pokémon
2. Démarrez le bot avec la commande `python main.py`
3. Configurez les touches:
   - Touche pour avancer dans les cinématiques
   - Touche pour réinitialiser la partie si pas de shiny
4. Cliquez sur l'émulateur pour donner le focus
5. Le bot commencera automatiquement à chercher votre Pokémon shiny
6. Lorsqu'un shiny est trouvé, le bot s'arrêtera et affichera un message de félicitations
7. Fermer venv avec la commande `deactivate`

---

![shiny-pokemon](src/images/shiny_pokemon.png)

_"Attrapez-les tous !"_

