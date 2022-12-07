"""
Tema: Palabras encadenadas

Descripcion:
El juego de las palabras encadenadas, es un juego clasico, el cual desafia la rapidez y memoria del jugador.
Consiste en que cada jugador dira una palabra de cualquier ambito y el siguiente jugador debera decir una nueva palabra
que comienze por la letra de la letra final de la ultima palabra mencionada y que ademas no se haya mencionada previamente.
Cada jugador se eliminara si falla en alguna de las reglas mencionadas y ya no podra participar, el ganador sera aquel jugador
que quede al final del juego.

Autor: Alexander David Guacan Rivera

Version: 1.4
"""

# Importamos la clase Game
from Game import *

# Definimos la funcion principal desde donde empezara el programa
def main() -> None:
    """_summary_ La funcion sirve como punto inicial del programa

        Returns:
        - None
    """

    # Limpiamos la terminal
    os.system("cls")

    # Imprimimos las reglas del juego
    print("""\t\t\tPALABRAS ENCADENADAS

COMO JUGAR: EL JUEGO INICIARA CON UNA PALABRA AL AZAR, SU OBJETIVO DEBERA SER INGRESAR PALABRAS
QUE EMPIEZEN POR LA ULTIMA LETRA DE LA PALABRA PRESENTADA
REGLAS:
- NO SE ACEPTAN PALABRAS QUE INICIEN POR VOCALES CON TILDE
- TIENE 3 VIDAS, CADA PALABRA MAL INGRESADA O REPETIDA LE RESTARA UNA VIDA
- DEBE INGRESAR HASTA 5 PALABRAS DE FORMA CORRECTA PARA GANAR
- INGRESE PALABRAS DE MAS DE 4 LETRAS
    
[PRESIONE CUALQUIER TECLA PARA COMENZAR EL JUEGO]""")

    os.system("pause > nul")


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