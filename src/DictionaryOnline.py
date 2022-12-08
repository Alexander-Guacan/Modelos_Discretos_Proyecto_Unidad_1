"""
Archivo:

Autor: Alexander Guacan

Version: 1.0

"""

# Importando modulos request y bs4 encargadas de manejar web scrapping
import requests
from bs4 import BeautifulSoup

def is_a_dictionary_word(word : str) -> bool:
    """_summary_ Esta funcion se encarga de verificar si una palabra existe a traves de la tecnica llamada webscrapping. La palabra existira si al ingresar a la url de la pagina, existe una definicion de la misma y si es q la palabra esta escrita exactamente como en el diccionario. Esto quiere decir que las faltas ortograficas se toman en cuenta

    Args:
        word (str): _description_ Palabra a verificar si existe en el diccionario

    Returns:
        bool: _description_ Retorna true si la palabra esta bien escrita y se pudo encontrar en la pagina
    """

    # URL de la pagina donde se buscara la definicion de la palabra
    url = f'https://www.wordreference.com/definicion/{word}'
    # Obtenemos el codigo html de la pagina web
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    # Buscamos todas las secciones que comienzen por <p> en el codigo html
    search_result = soup.find_all('p')
    # Buscamos todas las secciones que comienzen por <h3> en el codigo html
    textual_word = soup.find_all('h3')

    # Verificamos si la palabra existe si en la primera seccion <p> encontrada no se encuentra la palabra "No" ya que esta aparece cuando la palabra no tiene una definicion y tambien si la palabra esta siendo escrita correctamente como se muestra en el diccionario en la seccion <h3> de la pagina en su codigo html
    return not search_result[0].get_text().startswith("No") and word in textual_word[1].get_text()