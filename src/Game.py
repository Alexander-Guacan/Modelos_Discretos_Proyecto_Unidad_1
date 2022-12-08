"""
File: Game.py

Author: Alexander David Guacan Rivera

Version: 1.5

GitHub: https://github.com/Alexander-Guacan/Modelos_Discretos_Proyecto_Unidad_1.git

"""

# Import of random library and os library from the Python standard. We also import the DictionaryOnline module to check if a word exists in the dictionary.
import random, DictionaryOnline, os as console

class Game:
    """_summary_ Class in charge of managing the Chained Words game

    Attributes:
    - __random_words: Random list of words, from which one of them will be chosen at random to start the game.
    - __words_entered: This variable is responsible for storing all valid words entered by the user as well as the randomly chosen word from random_words.
    - __score_to_wint: Indicates the number of valid words the player must enter to win the game.
    - __current_score: It indicates the number of valid words the player has entered.

    Methods:
    - __init__: Default constructor
    - __select_random_word: Picks a word at random from the list of words in the member variable __random_words
    - __is_a_chained_word: Checks if a word complies with the rules of the game
    - __update_score: Updates the player's score by increasing his current score by 1
    - __update_lives: We update the player's number of lives by decrementing by 1 the total number of lives remaining.
    - start: Starts the logic of the video game
    """

    def __init__(self) -> None:
        """_summary_ Default constructor
        """

        # Initializing member variable __random_words with a random list of words, from which one of them will be chosen at random to start the game.
        self.__random_words = ["pera", "palo", "cobre", "piramide", "computación", "piedra", "caer", "kiwi", "tribu", "sapo", "lémur"]
        # Initializing member variable __words_entered with an empty object of the list class that stores objects of class str. This variable is responsible for storing all valid words entered by the user as well as the randomly chosen word from random_words.
        self.__words_entered = list()
        # Initializing member variable __lives with a value of 3. Indicates the maximum number of wrong words the user can enter in the game.
        self.__lives = 3
        # Initializing member variable __score_to_win with a value of 5. Indicates the number of valid words the player must enter to win the game.
        self.__score_to_win = 5
        # We initialize member variable __current_score with a value of 0. It indicates the number of valid words the player has entered.
        self.__current_score = 0

    def __select_random_word(self) -> str:
        """_summary_ Picks a word at random from the list of words in the member variable __random_words

        Returns:
            str: _description_ Random word from __random_words
        """

        # Selecting a random word by generating a random number with the help of the randInt function, belonging to the random library, which will serve as an index into the __random_words list.
        return self.__random_words[random.randint(0, len(self.__random_words) - 1)]

    def __is_a_chained_word(self, word : str) -> bool:
        """_summary_ Checks if a word complies with the rules of the game

        Args:
            word (str): _description_ Word to verify that it complies with the rules of the game

        Returns:
            bool: _description_ Returns true if the word complies with all the rules of the game and false otherwise.
        """

        # We verify that the rules of the chained word set are met. We verify that the word begins with the last letter of the last word entered in __words_entered. Also that the word is not repeated and that the word exists in the dictionary.
        return len(word) > 0 and word[0] == self.__words_entered[-1][-1] and word not in self.__words_entered and DictionaryOnline.is_a_dictionary_word(word)

    def __update_score(self) -> None:
        """_summary_ Updates the player's score by increasing his current score by 1
        """

        # We increase the player's score by one.
        self.__current_score += 1
        # We show by console information about the score
        print(f"\n[CORRECTO]-> Puntaje: {self.__current_score} de {self.__score_to_win}\n")

    def __update_lives(self) -> None:
        """_summary_ We update the player's number of lives by decrementing by 1 the total number of lives remaining.
        """

        # Decrementamos en uno las vidas del jugador
        self.__lives -= 1
        # The console displays information on why the word entered is invalid as well as the number of lives the player has left.
        print(f"\nMOTIVOS POR EL CUAL TU PALABRA NO ES VALIDA:\n"
                "1.- La palabra no empieza literalmente por la ultima letra de la palabra presentada\n"
                "2.- La palabra ha sido ingresada previamente\n"
                "3.- La palabra no existe en el diccionario\n"
                f"Vidas restantes: {self.__lives}"
        )

    def start(self) -> None:
        """_summary_ Starts the logic of the video game
        """

        # We select a word at random from the member variable __random_words and add it to the end of the list of the member variable __words_entered
        self.__words_entered.append(self.__select_random_word())

        # The game runs as long as the player still has lives available or has not yet completed the winning score.
        while self.__lives > 0 and self.__current_score < self.__score_to_win:
            # Clean the console
            console.system("cls")
            
            # We print on the screen the last word selected, which is the last word entered in the __words_entered array.
            print(f"Palabra actual: {self.__words_entered[-1]}\n")

            # We ask the user to enter a word on the keyboard and then validate it.
            current_word = input("Ingrese una palabra encadenada: ")

            # The word is checked for validity if the letter at the beginning of the word entered by the user is the same as the last letter of the last word in the __words_entered list and the word entered by the user has not been previously entered in __words_entered.
            if self.__is_a_chained_word(current_word):
                # We update the player's score
                self.__update_score()
                # We add the word entered by the user to the list of the member variable __words_entered
                self.__words_entered.append(current_word)
            # In case the word does not comply with the game conditions
            else:
                # We update the number of lives of the player
                self.__update_lives()

            # Execute a terminal instruction that will pause the game until the user presses any key
            console.system("pause > nul")


        # Executes a terminal instruction that will pause the game until the user presses any key.
        print("[GANASTE]" if self.__current_score == self.__score_to_win else "[PERDISTE]")