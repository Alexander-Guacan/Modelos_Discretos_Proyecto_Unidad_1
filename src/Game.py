"""
Archivo: Game.py

Autor: Alexander David Guacan Rivera

Version: 1.4

"""

# Importacion de libreria random y libreria os propias del estandar de Python. tambien imporamos el modulo DictionaryOnline encargada de verificar si una palabra existe en el diccionario
import random, DictionaryOnline, os as console

class Game:
    """_summary_ Clase encargada del gestionamiento del juego Palabras encadanadas
    """

    def __init__(self) -> None:
        """_summary_ Constructor de la clase Game, inicializa las variables miembro
        """

        # Inicializando variable miembro __random_words la cual tendra una lista de 3 palabras, de las cuales se elegira una de ellas al azar para iniciar el juego
        self.__random_words = ["pera", "palo", "cobre"]
        # Inicializando variable miembro __words_entered con un objeto vacio de la clase list que almacena objetos de la clase str. Esta variable se encarga de almacenar todas las palabras validas ingresadas por el usuario asi como la palabra elegida al azar de random_wods
        self.__words_entered = list()
        # Inicializando variable miembro __lives con el valor de 3. Indica el numero de palabras erroneas maximas que el usuario puede ingresar en el juego
        self.__lives = 3
        # Inicializando variable miembro __score_to_win con el valor de 5. Indica el numero de palabras validas que el jugador debera ingresar para ganar el juego
        self.__score_to_win = 5
        # Inicializamos variable miembro __current_score con el valor de 0. Indica el numero de palabras validas que lleva ingresando el jugador
        self.__current_score = 0

    def __select_random_word(self) -> str:
        """_summary_ Elige una palabra al azar del listado de palabras de la variable miembro __random_words

        Returns:
            str: _description_ Palabra al azar de __random_words
        """

        # Seleccionando una palabra al azar a traves de la generacion de un numero randomico con ayuda de la funcion randInt, perteneciente a la libreria random, que servira como indice dentro de la lista __random_words
        return self.__random_words[random.randint(0, len(self.__random_words) - 1)]

    def __is_a_chained_word(self, word : str) -> bool:
        """_summary_ Verifica si una palabra cumple con las reglas del juego

        Args:
            word (str): _description_ Palabra a verificar que cumpla con las reglas del juego

        Returns:
            bool: _description_ Retorna true si la palabra cumple con todas las reglas del juego y false en case contrario
        """

        # Verificamos que se cumplan las reglas del juego de palabras encadenadas. Verificamos que la palabra empieze por la ultima letra de la ultima palabra ingresada en __words_entered. Tambien que dicha palabra no sea repetida y que la palabra exista en el diccionario
        return word[0] == self.__words_entered[-1][-1] and word not in self.__words_entered and DictionaryOnline.is_a_dictionary_word(word)

    def __update_score(self) -> None:
        """_summary_ Actualiza el puntaje del jugador incrementando en 1 el puntaje que lleva actualmente
        """

        # Incrementamos en uno el puntaje del jugador
        self.__current_score += 1
        # Mostramos por consola informacion acerca del puntaje
        print(f"\n[CORRECTO]-> Puntaje: {self.__current_score} de {self.__score_to_win}\n")

    def __update_lives(self) -> None:
        """_summary_ Actualizamos el numero de vidas del jugador decremetando en 1 el total de vidas que le quedan
        """

        # Decrementamos en uno las vidas del jugador
        self.__lives -= 1
        # Mostramos en consola informacion del porque la palabra ingresada no es valida asi como del numero de vidas que le quedan al jugador
        print(f"\nMOTIVOS POR EL CUAL TU PALABRA NO ES VALIDA:\n"
                "1.- La palabra no empieza literalmente por la ultima letra de la palabra presentada\n"
                "2.- La palabra ha sido ingresada previamente\n"
                "3.- La palabra no existe en el diccionario\n"
                f"Vidas restantes: {self.__lives}"
        )

    def start(self) -> None:
        """_summary_ 
            Variables:
            - current_word : Variable de tipo string encargada de guardar lo que ingresa por teclado el jugador para su posterior verificacion
        """

        # Seleccionamos una palabra al azar de la variable miembro __random_words y la agregamos la final de la lista de la variable miembro __words_entered
        self.__words_entered.append(self.__select_random_word())

        # El juego se mantiene en ejecucion mientras el jugador aun tenga vidas disponibles o aun no haya completado el puntaje para ganar
        while self.__lives > 0 and self.__current_score < self.__score_to_win:
            # Limpiamos la consola
            console.system("cls")
            
            # Imprimimos por pantalla la ultima palabra seleccionada, que es la ultima palabra ingresada en el arreglo __words_entered
            print(f"Palabra actual: {self.__words_entered[-1]}\n")

            # Pedimos al usuario que ingrese por teclado una palabra para posteriormente validarla
            current_word = input("Ingrese una palabra encadenada: ")

            # Se verifica si la palabra es valida si la letra con la comienza la palabra ingresada por el usuario es igual a la letra final de la ultima palabra en el listado de __words_entered y dicha palabra ingresada por el usuario no ha sido previamente ingresada en __words_entered
            if self.__is_a_chained_word(current_word):
                # Actualizamos el puntaje del jugador
                self.__update_score()
                # Agregamos la palabra ingresada por el usuario al listado de la variable miembro __words_entered
                self.__words_entered.append(current_word)
            # En caso de que la palabra no cumpla las condiciones del juego
            else:
                # Actualizamos el numero de vidas que lleva el jugador
                self.__update_lives()

            # Ejecutamos una instruccion del terminal que pausara el juego hasta que el usuario presiona una tecla cualquiera
            console.system("pause > nul")


        # Determinamos si el jugador gano o no si ha llegado al puntaje establecido para ganar, si no lo cumple es que el jugador ha perdido
        print("[GANASTE]" if self.__current_score == self.__score_to_win else "[PERDISTE]")