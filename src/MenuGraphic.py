"""
File: MenuGraphic.py

Author: Alexander Guacan

Version: 1.1

GitHub: https://github.com/Alexander-Guacan/Modelos_Discretos_Proyecto_Unidad_1.git

"""

# Importing os module with the name console
import os as console

class MenuGraphic:
    """_summary_ This class is in charge of printing on the screen a menu with the different options passed by paramatero in the constructor and asking the user to enter the number of the option he/she wants to choose.

    Attributes:
    - __title: Menu title
    - __options: Menu options

    Methods:
    - __init__: Default constructor
    - print: Show menu on console with all options
    """

    def __init__(self, title : str, options : list[str]) -> None:
        """_summary_ Default constructor

        Args:
            title (str): _description_ Menu title
            options (list[str]): _description_ List of menu options that will be displayed sequentially on console
        """

        # Initializing the member variable __title with the title variable passed as a parameter
        self.__title = title
        # Initializing the member variable __options with the variable options passed as a parameter
        self.__options = options
        

    def print(self) -> int:
        """_summary_ Print the title and options list of the __title and __options member variables respectively. Each option is assigned a number sequentially from 1 to the number of options in the __options list.

        Returns:
            int: _description_ Option selected by the player
        """

        # This variable is in charge of storing the option selected by the player and verifies if it is within the existing options.
        option_selected = -1

        # The player will still be prompted to enter a menu option as long as it is outside the range of between 1 and the total number of options in the __options list.
        while option_selected < 1 or option_selected > len(self.__options):
            # Clean the console
            console.system("cls")
            # Print the menu title
            print(self.__title)
            # We print all the options of __options
            for i in range(len(self.__options)):
                # We add an identifier number to each menu option
                print(f"{i + 1}.- {self.__options[i]}")
            
            # We start an exception block
            try:
                # We ask the user to enter the menu option
                option_selected = int(input("Ingrese el numero de opcion y presione ENTER [ ]\b\b"))
            # Exception if the selected option is not of type int
            except ValueError:
                # Print a message telling the user what the error was
                print("\nERROR: [EL DATO INGRESADO DEBE SER UN NUMERO ENTERO, PRESIONE CUALQUIER TECLA PARA CONTINUAR]\n")
                # We pause the program execution but without displaying a default console message
                console.system("pause > nul")
        
        # We return the option selected by the player
        return option_selected
