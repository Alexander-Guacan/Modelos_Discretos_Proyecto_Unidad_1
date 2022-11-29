"""
Archivo: Game.py

Autor: Alexander David Guacan Rivera

Version: 1.2

"""

from random import randint # Importamos la libreria random, especificamente su funcion randint

class Game:
    """_summary_ Clase Game encargada de gestionar el funcionamiento del juego "Palabras encadenadas"
    """

    def __init__(self, lives = 3, points_to_win = 5) -> None:
        """_summary_

        Args:
            lives (int, optional): _description_ Numero de fallos posibles. Defaults to 5.
            points_to_win (int, optional): _description_ Cantidad de palabras que ingresara correctamente para ganar. Defaults to 10.
        """
        self.__lives = lives # Asignamos el valor de la variable lives a la variable miembro __lives
        self.__words_entered = list() # Asignamos una lista vacia a la variable miembro __words_entered
        # Asignamos un arreglo con palabras definidas a la variable miembro __initial_words
        self.__initial_words = ["mango", "carro", "cubo", "papel", "jarra", "manguera", "pez", "mounstruo", "mani", "ajolote"]
        self.__points_to_win = points_to_win # Asignamos el valor de points_to_win a la variable miembro __points_to_win

    def __select_random_initial_word(self) -> str:
        """_summary_ Funcion encargada de tomar una palabra al azar del listado de palabras de la variable miembro __initial_words

        Returns:
            str: _description_ Palabra escogida al azar
        """
        return self.__initial_words[randint(0, len(self.__initial_words) - 1)] # Selecciona una palabra en una posicion randomica dentro del arreglo

    def start(self) -> None:
        """_summary_ Inicia el juego

        Returns:
            None
        """

        # Agregamos al listado de __words_entered, la palabra seleccionada al azar de __initial_words
        self.__words_entered.append(self.__select_random_initial_word())
        current_points = 0 # Inicializamos a 0 la variable current_points

        # El juego se ejecutara mientras aun le queden vidas al jugador y no haya completado el puntaje estipulado
        while self.__lives > 0 and current_points < self.__points_to_win:
            # Imprimimos la ultima palabra ingresada o seleccionada
            print(f"Palabra actual = {self.__words_entered[-1]}")
            # Ingreso por teclado de una nueva palabra
            word_input = input("Ingrese una palabra: ")

            # Verificamos que la palabra no se haya escrito previamente y que comienze por la letra final de la ultima palabra ingresada
            if word_input not in self.__words_entered and word_input.startswith(self.__words_entered[-1][-1]):
                # Agregamos al listado de palabras ya ingresadas
                self.__words_entered.append(word_input)
                current_points += 1 # Incrementamos en uno el puntaje
                # Informamos al jugador que su palabra es correcto y que puntaje lleva actualmente
                print(f"\nCorrecto, [PUNTAJE ACTUAL = {current_points} de {self.__points_to_win}]\n")

            else: # La palabra no cumplio con alguna regla
                # Imprimimos el posible error que tiene la palabra ingresada
                print(f"\nERROR [La palabra ya ha sido ingresada previamente o su primera letra no comienza por {self.__words_entered[-1][-1]}, intenta nuevamente]")
                self.__lives -= 1 # Decrementamos en uno el total de vidas del jugador
                # Imprimimos el numero de vidas que le quedan al jugador
                print(f"Vidas restantes: {self.__lives}\n")

        # Imprimimos en pantalla si el jugador gano o perdio de acuerdo al puntaje obtenido al final del juego
        print("\n" + "Ganaste!!!" if current_points == self.__points_to_win else "Perdiste :c")