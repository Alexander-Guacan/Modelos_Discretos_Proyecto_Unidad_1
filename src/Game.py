from random import randint

class Game:

    def __init__(self, lives = 5, points_to_win = 10) -> None:
        self.__lives = lives
        self.__words_entered = list()
        self.__initial_words = ["mango", "carro", "cubo", "papel", "jarra", "manguera", "pez", "mounstruo", "mani", "ajolote"]
        self.__points_to_win = points_to_win

    def __select_random_initial_word(self) -> str:
        return self.__initial_words[randint(0, len(self.__initial_words) - 1)]

    def start(self) -> None:
        self.__words_entered.append(self.__select_random_initial_word())
        current_points = 0

        while self.__lives > 0 and current_points < self.__points_to_win:
            print(f"Palabra actual = {self.__words_entered[-1]}")
            word_input = input("Ingrese una palabra: ")

            if word_input not in self.__words_entered and word_input.startswith(self.__words_entered[-1][-1]):
                self.__words_entered.append(word_input)
                current_points += 1
                print(f"\nCorrecto, [PUNTAJE ACTUAL = {current_points} de {self.__points_to_win}]\n")

            else:
                print(f"\nERROR [La palabra ya ha sido ingresada previamente o su primera letra no comienza por {self.__words_entered[-1][-1]}, intenta nuevamente]")
                self.__lives -= 1
                print(f"Vidas restantes: {self.__lives}\n")

        print("\n" + "¡¡¡Ganaste!!!" if current_points == self.__points_to_win else "Perdiste :c")