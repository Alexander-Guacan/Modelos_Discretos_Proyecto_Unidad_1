"""
Archivo: Game.py

Autor: Alexander David Guacan Rivera

Version: 1.4

"""

# Importacion de libreria random y libreria os propias del estandar de Python
import random, os

class Game:
    """_summary_ Clase encargada del gestionamiento del juego Palabras encadanadas
    """

    def __init__(self) -> None:
        """_summary_ Constructor de la clase Game, inicializa las variables miembro
        """

        # Inicializando variable miembro random_words la cual tendra una lista de 3 palabras, de las cuales se elegira una de ellas al azar para iniciar el juego
        self.random_words = ["pera", "palo", "cobre"]
        # Inicializando variable miembro words_entered con un objeto vacio de la clase list que almacena objetos de la clase str. Esta variable se encarga de almacenar todas las palabras validas ingresadas por el usuario asi como la palabra elegida al azar de random_wods
        self.words_entered = list()
        # Inicializando variable miembro lives con el valor de 3. Indica el numero de palabras erroneas maximas que el usuario puede ingresar en el juego
        self.lives = 3
        # Inicializando variable miembro score_to_win con el valor de 5. Indica 
        self.score_to_win = 5

    def __select_random_word(self) -> str:
        """_summary_ Elige una palabra al azar del listado de palabras de la variable miembro random_words

        Returns:
            str: _description_ Palabra al azar de random_words
        """

        # Seleccionando una palabra al azar a traves de la generacion de un numero randomico con ayuda de la funcion randInt, perteneciente a la libreria random, que servira como indice dentro de la lista random_words
        return self.random_words[random.randint(0, len(self.random_words) - 1)]

    def start(self) -> bool:
        """_summary_ Da inicio al juego de palabras encadenadas

        Returns:
            bool: _description_ Retorna true si el jugador gano el juego que se traduce que completo el puntaje necesario para ganar, caso contrario retorna false
        """

        # Inicializamos variable current_score a 0. Cuenta el numero de palabras validas que el usuario ha ido ingresado a lo largo del juego
        current_score = 0
        # Seleccionamos una palabra al azar de la variable miembro random_words y la agregamos la final de la lista de la variable miembro words_entered
        self.words_entered.append(self.__select_random_word())

        # El juego se mantiene en ejecucion mientras el jugador aun tenga vidas disponibles o aun no haya completado el puntaje para ganar
        while self.lives > 0 and current_score < self.score_to_win:

            # Inicializamos la variable current_word con un string vacio. Almacena lo que ingresa el jugador por teclado y que a su vez nos permitira disernir si dicha palabra es valida o no segun las reglas del juego
            current_word = ""

            # Bucle que valida un primer ingreso por consola, donde el mismo no debe ser una cadena vacia ni contener algun caracter que no se alfabetico. Las palabras con tilde no se admiten.
            while len(current_word) <= 4 or not current_word.isalpha():
                # Uso de la funcion system de la libreria os. Limpia la consola.
                os.system("cls")
                # Se muestra por consola la ultima palabra ingresada en el listado de la variable miembro words_entered
                print(f"Palabra: {self.words_entered[-1]}\n")
                # Se pide al usuario que ingrese una palabra por consola y se utiliza la funcion replace para borrar todos los espacios en blanco. Posteriormente se almacena dicho ingreso en la variable current_word
                current_word = input("Ingrese una nueva palabra: ")

                # Si la palabra contiene menos de 4 letras
                if len(current_word) <= 4:
                    # Impresion en pantalla el error generado
                    print("\n[ERROR: INGRESE UNA PALABRA DE MAS DE 4 LETRAS]")
                    # Hacmos una pausa a la ejecucion del programa
                    os.system("pause > nul")

                # Si la palabra contiene algun caracter no alfabetico
                elif not current_word.isalpha():
                    # Impresion en pantalla el error generado
                    print("\n[ERROR: SU PALABRA CONTIENE CARACTERES NO ALFABETICOS]")
                    # Hacmos una pausa a la ejecucion del programa
                    os.system("pause > nul")

            # Se verifica si la palabra es valida si la letra con la comienza la palabra ingresada por el usuario es igual a la letra final de la ultima palabra en el listado de words_entered y dicha palabra ingresada por el usuario no ha sido previamente ingresada en words_entered
            if current_word[0] == self.words_entered[-1][-1] and current_word not in self.words_entered:
                # Incrementamos en uno el puntaje del jugador
                current_score += 1
                # Agregamos la palabra ingresada por el usuario al listado de la variable miembro words_entered
                self.words_entered.append(current_word)
                # Mostramos por consola informacion acerca del puntaje
                print(f"\n[CORRECTO]-> Puntaje: {current_score} de {self.score_to_win}\n")
            # En caso de que la palabra no cumpla las condiciones del juego
            else:
                # Decrementamos en uno las vidas del jugador
                self.lives -= 1
                # Mostramos en consola informacion del numero de vidas que le quedan al jugador
                print(f"\n[INCORRECTO: Palabra no comienza por la ultima letra de la palabra presentada o es repetida]-> Vidas restantes: {self.lives}\n")

            # Ejecutamos una instruccion del terminal que pausara el juego hasta que el usuario presiona una tecla cualquiera
            os.system("pause > nul")

        # Limpiamos la consola
        os.system("cls")

        # Determinamos si el jugador gano o no si ha llegado al puntaje establecido para ganar, si no lo cumple es que el jugador ha perdido
        return current_score == self.score_to_win