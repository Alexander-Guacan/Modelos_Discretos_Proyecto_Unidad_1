"""
File: MenuGame.py

Author: Alexander Guacan

Version: 1.1

GitHub: https://github.com/Alexander-Guacan/Modelos_Discretos_Proyecto_Unidad_1.git

"""

# Importamos la clase Game
from Game import Game
# Importando modulo os con el nombre de console
import os as console

class MenuGame:
    """_summary_ This class is in charge of managing each option of the MenuGraphic class and determines which option will stop the execution of the game.

    Attributes:
    
    Methods:
    - __start_game: Starts the chained word video game
    - __print_instructions: Function in charge of printing the rules of the chained word game
    """

    def __start_game(self) -> None:
        """_summary_ Starts the chained word game by creating an instance of the Game class
        """
        
        # Creamos una instancia de la clase Game
        chained_words = Game()
        # Llamamos a la funcion start para iniciar el juego
        chained_words.start()

    def __print_instructions(self) -> None:
        """_summary_ Function in charge of printing the rules of the chained word game
        """
        # Clean the console
        console.system("cls")

        # We print on screen all the rules and instructions on how to play the game.
        print("\t\t\t[INSTRUCCIONES]"
        "\nEste juego consiste en que se le mostrara una palabra en pantalla."
        "\nUsted debe ingresar una palabra que empieze con la ultima letra de dicha palabra actual presentada."
        "\n[La palabra no es valida si]"
        "\n- La palabra no comienza literalmente por la ultima letra de la palabra actual presentada"
        "\n- Es una palabra repetida"
        "\n- La palabra no existe en el diccionario o ha sido escrita con faltas de ortografia"
        "\nUsted debera ingresar 5 palabras validas para ganar el juego."
        "\nTiene 3 vidas, lo que quiere decir que solo podra ingresar 3 palabras incorrectas"
        "\n\t\t[PRESIONE CUALQUIER TECLA PARA CONTINUAR]"
        )


    def select_option(self, option : int) -> bool:
        """_summary_ Responsible for managing and performing the option corresponding to the option sent by parameter.

        Args:
            option (int): _description_ Game menu option

        Returns:
            bool: _description_ Returns true if option is the same as the "Exit" option in menu
        """

        # We control the case of option commanded by parameter
        match option:
            # Case where option is 1
            case 1:
                # We start the chained words game
                self.__start_game()
                # We pause the program execution but without displaying a default console message
                console.system("pause > nul")
            # Case where option is 2
            case 2:
                # We print out the rules and instructions of the chained words game.
                self.__print_instructions()
                # We pause the program execution but without displaying a default console message
                console.system("pause > nul")
            # Case where option is 3
            case 3:
                # We return true since this option would be the "Exit" option in the menu.
                return True
        # We return False because the "Exit" option has not been selected in the menu.
        return False