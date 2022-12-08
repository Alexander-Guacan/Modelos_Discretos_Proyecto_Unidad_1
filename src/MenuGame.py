"""
Archivo: MenuGame.py

Autor: Alexander Guacan

Version: 1.0

"""

# Importamos la clase Game
from Game import Game
# Importando modulo os con el nombre de console
import os as console

class MenuGame:
    """_summary_ Esta clase se encarga de gestionar cada opcion de la clase MenuGraphic y determina cual sera la opcion que permitira detener la ejecucion del juego
    """

    def __start_game(self) -> None:
        """_summary_ Inicia el juego de palabras encadenadas creando una instancia de la clase Game
        """
        
        # Creamos una instancia de la clase Game
        chained_words = Game()
        # Llamamos a la funcion start para iniciar el juego
        chained_words.start()

    def __print_instructions(self) -> None:
        """_summary_ Funcion encargada de imprimir las reglas del juego de palabras encadenadas
        """
        # Limpiamos la consola
        console.system("cls")

        # Imprimimos en pantalla todas las reglas e instrucciones de como jugar al juego
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
        """_summary_ Encargada de gestionar y realizar la opcion correspondiente a la opcion que se haya mandado por parametro

        Args:
            option (int): _description_ Opcion del menu del juego

        Returns:
            bool: _description_ Retorna true si option es la misma que la opcion "Salir" en el menu
        """

        # Controlamos el caso de opcion mandada por parametro
        match option:
            # Caso donde option es 1
            case 1:
                # Iniciamos el juego palabras encadenadas
                self.__start_game()
                # Pausamos la ejecucion del programa pero sin mostrar un mensaje por defecto de la consola
                console.system("pause > nul")
            # Caso donde option es 2
            case 2:
                # Imprimimos las reglas e instrucciones del juego palabras encadenadas
                self.__print_instructions()
                # Pausamos la ejecucion del programa pero sin mostrar un mensaje por defecto de la consola
                console.system("pause > nul")
            # Caso donde option es 2
            case 3:
                # Retornamos true ya que esta opcion seria la de "Salir" en el menu
                return True
        # Retornamos False ya que no se ha seleccionado la opcion de "Salir" en el menu
        return False