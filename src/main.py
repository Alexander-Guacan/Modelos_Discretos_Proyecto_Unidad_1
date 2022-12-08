"""
Tema: Palabras encadenadas

Descripcion:
El juego de las palabras encadenadas, es un juego clasico, el cual desafia la memoria del jugador y su conocimiento de las palabras.
Consiste en que cada jugador dira una palabra de cualquier ambito y el siguiente jugador debera decir una nueva palabra
que comienze por la letra de la letra final de la ultima palabra mencionada y que ademas no se haya mencionada previamente.
Para este juego unicamente sera solo un jugador el que debera ingresar las palabras, mostrando en un inicio una palabra al azar.

Autor: Alexander David Guacan Rivera

Version: 1.4
"""

# Importamos la clase Game
from MenuGraphic import MenuGraphic
# Importamos la clase MenuGame
from MenuGame import MenuGame

# Definimos la funcion principal desde donde empezara el programa
def main() -> None:
    """_summary_ Esta es la funcion principal desde donde empezara a ejecutarse el juego. Haciendo uso de objetos de las clases MenuGraphic y Menu Game. Se presentara al usuario las opciones del menu y solo terminara el juego cuando el jugador seleccione la opcion de "Salir"
    """

    # Creamos una instancia de la clase MenuGraphic. Inicializando el constructor con el titulo y opciones del menu principal
    menu_gui = MenuGraphic(
    "\t\tPALABRAS ENCADENADAS",
        [
            "JUGAR",
            "INSTRUCCIONES",
            "SALIR"
        ]
    )
    
    # Creamos variable booleana que nos determinara cuando se debera terminar la ejecucion del juego
    end_game = False
    # Creamos una instancia de la clase MenuGame que se encargara de gestionar las opciones elegidas por el jugador
    menu_game = MenuGame()

    # El juego se seguira ejecutando mientras la opcion seleccionada por el jugador no sea la de "Salir" en el menu
    while not end_game:
        # Asignamos el resultado de la opcion elegida en el menu, si fue la de "Salir" es verdadero, caso contrario cualquiera de las otras opciones es falsa
        end_game = menu_game.select_option(menu_gui.print())

# Verificamos que el programa esta siendo ejecutado desde el presente modulo
if __name__ == "__main__":
    # Llamamos a la funcion main para comenzar el programa
    main()