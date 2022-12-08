"""
Title: Palabras encadenadas

Description:
The word chain game is a classic game, which challenges the player's memory and knowledge of words.
It consists in that each player will say a word from any field and the next player must say a new word that begins with the letter of the final letter of the last
that begins with the letter of the final letter of the last mentioned word and that has not been previously mentioned.
For this game only one player will have to enter the words, showing a random word at the beginning.

Author: Alexander David Guacan Rivera

GitHub: https://github.com/Alexander-Guacan/Modelos_Discretos_Proyecto_Unidad_1.git

Version: 1.5
"""

# We import the Game class
from MenuGraphic import MenuGraphic
# We import the MenuGame class
from MenuGame import MenuGame

# We define the main function where the program will start from
def main() -> None:
    """_summary_ This is the main function from where the game will start running. Making use of objects of the MenuGraphic and Menu Game classes. The user will be presented with the menu options and the game will only end when the player selects the "Exit" option.
    """

    # We create an instance of the MenuGraphic class. Initializing the constructor with the title and options of the main menu.
    menu_gui = MenuGraphic(
    "\t\tPALABRAS ENCADENADAS",
        [
            "JUGAR",
            "INSTRUCCIONES",
            "SALIR"
        ]
    )
    
    # We create a boolean variable that will determine when the execution of the game should be terminated.
    end_game = False
    # We create an instance of the MenuGame class that will be in charge of managing the options chosen by the player.
    menu_game = MenuGame()

    # The game will continue to run as long as the option selected by the player is not "Exit" in the menu.
    while not end_game:
        # We assign the result of the option chosen in the menu, if it was "Exit" it is true, otherwise any of the other options is false.
        end_game = menu_game.select_option(menu_gui.print())

# We verify that the program is being executed from this module.
if __name__ == "__main__":
    # We call the main function to start the program
    main()