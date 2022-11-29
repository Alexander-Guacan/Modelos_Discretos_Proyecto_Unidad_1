"""
Tema: Palabras encadenadas

Descripcion:
El juego de las palabras encadenadas, es un juego clasico, el cual desafia la rapidez y memoria del jugador.
Consiste en que cada jugador dira una palabra de cualquier ambito y el siguiente jugador debera decir una nueva palabra
que comienze por la letra de la letra final de la ultima palabra mencionada y que ademas no se haya mencionada previamente.
Cada jugador se eliminara si falla en alguna de las reglas mencionadas y ya no podra participar, el ganador sera aquel jugador
que quede al final del juego.

Autor: Alexander David Guacan Rivera

Version: 1.2
"""

from Game import * # Importamos la clase Game

# Definimos la funcion principal desde donde empezara el programa
def main() -> int:
    """_summary_ La funcion sirve como punto inicial del programa

    Returns:
        int: _description_ Retorna el estado en que termino el programa (0 = correcto, 1 = incorrecto o con error)
    """
    game = Game() # Creamos una instancia de la clase Game
    game.start() # Iniciamos el juego
    
    return 0

main() # Llamamos a la funcion main para comenzar el programa