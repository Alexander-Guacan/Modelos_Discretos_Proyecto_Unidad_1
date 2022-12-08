"""
File: DictionaryOnline.py

Author: Alexander Guacan

Version: 1.1

GitHub: https://github.com/Alexander-Guacan/Modelos_Discretos_Proyecto_Unidad_1.git

"""

# Importing request and bs4 modules in charge of web scrapping handling
import requests
from bs4 import BeautifulSoup

def is_a_dictionary_word(word : str) -> bool:
    """_summary_ This function is in charge of verifying if a word exists through the technique called webscrapping. The word will exist if when entering the url of the page, there is a definition of it and if the word is written exactly as in the dictionary. This means that spelling mistakes are taken into account.

    Args:
        word (str): _description_ Word to check if it exists in the dictionary

    Returns:
        bool: _description_ Returns true if the word is spelled correctly and could be found on the page.
    """

    # URL of the page where you will look for the definition of the word
    url = f'https://www.wordreference.com/definicion/{word}'
    # We get the html code of the web page
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    # We look for all sections beginning with <p> in the html code.
    search_result = soup.find_all('p')
    # Buscamos todas las secciones que comienzen por <h3> en el codigo html
    textual_word = soup.find_all('h3')

    # We check if the word exists if in the first section <p> found there is no word "No" as this appears when the word does not have a definition and also if the word is being spelled correctly as shown in the dictionary in the <h3> section of the page in its html code.
    return not search_result[0].get_text().startswith("No") and word in textual_word[1].get_text()