"""
Tema: Palabras encadenadas

Descripcion:
El juego de las palabras encadenadas, es un juego clasico, el cual desafia la rapidez y memoria del jugador.
Consiste en que cada jugador dira una palabra de cualquier ambito y el siguiente jugador debera decir una nueva palabra
que comienze por la letra de la letra final de la ultima palabra mencionada y que ademas no se haya mencionada previamente.
Cada jugador se eliminara si falla en alguna de las reglas mencionadas y ya no podra participar, el ganador sera aquel jugador
que quede al final del juego.

Autor: Alexander David Guacan Rivera

Version: 1.3
"""

# Importamos la clase Game
from Game import *

# Definimos la funcion principal desde donde empezara el programa
def main() -> None:
    """_summary_ La funcion sirve como punto inicial del programa
    """

    # Creamos una instancia de la clase Game
    game = Game()

    # Llamamos a la funcion miembro start de la clase Game. Guardamos en la variable is_winner el estado final del jugador si el mismo gano o no
    is_winner = game.start()
    
    # Si el jugador gano el juego
    if is_winner:
        print("\nGanaste")
    # Si el jugador no gano el juego
    else:
        print("\nPerdiste")

# Llamamos a la funcion main para comenzar el programa
main()