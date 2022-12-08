"""
Archivo: MenuGraphic.py

Autor: Alexander Guacan

Version: 1.0

"""

# Importando modulo os con el nombre de console
import os as console

class MenuGraphic:
    """_summary_ Esta clase es encargada de imprimir en pantalla un menu con las distinas opciones pasadas por paramatero en el constructor y pidiendole al usuario que ingrese el numero de la opcion que desea elegir
    """

    def __init__(self, title : str, options : list[str]) -> None:
        """_summary_ Constructor por default de la clase MenuGraphic

        Args:
            title (str): _description_ Titulo del menu
            options (list[str]): _description_ Listado de opciones del mneu que se desplegara secuencialmente en consola
        """

        # Inicializando la variable miembro __title con la variable title pasado por parametro
        self.__title = title
        # Inicializando la variable miembro __options con la variable options pasado por parametro
        self.__options = options
        

    def print(self) -> int:
        """_summary_ Imprime por pantalla el titulo y listado de opciones de las variables miembro __title y __options respectivamente. A cada opcion se le asigna un numero de forma secuencial desde 1 hasta el numero de opciones existentes en el listado de __options.

        Returns:
            int: _description_ Opcion seleccionada por el jugador
        """

        # Esta variable se encarga de almacenar la opcion seleccionada por el jugador y verifica si esta dentro de las opciones existentes
        option_selected = -1

        # Se le seguira pidiendo al jugador que ingrese una opcion del menu siempre y cuando este fuera del rando de entre 1 y el total de opciones en el listado de __options
        while option_selected < 1 or option_selected > len(self.__options):
            # Limpiamos la consola
            console.system("cls")
            # Imprimimos el titulo del menu
            print(self.__title)
            # Imprimimos todas las opciones de __options
            for i in range(len(self.__options)):
                # Agregamos un numero identificador a cada opcion del menu
                print(f"{i + 1}.- {self.__options[i]}")
            
            # Iniciamos un bloque de excepciones
            try:
                # Pedimos al usuario que ingrese la opcion del menu
                option_selected = int(input("Ingrese el numero de opcion y presione ENTER [ ]\b\b"))
            # Excepcion si la opcion seleccionada no es de tipo int
            except ValueError:
                # Imprimimos un mensaje que le indique al usuario cual ha sido el error
                print("\nERROR: [EL DATO INGRESADO DEBE SER UN NUMERO ENTERO, PRESIONE CUALQUIER TECLA PARA CONTINUAR]\n")
                # Pausamos la ejecucion del programa pero sin mostrar un mensaje por defecto de la consola
                console.system("pause > nul")
        
        # Retornamos la opcion que selecciono el jugador
        return option_selected
