import requests
from bs4 import BeautifulSoup
import json

def google_search(search_term, api_key, cse_id, **kwargs):
    """
    Realiza uma pesquisa na API do Google Custom Search.

    Esta função envia uma requisição à API do Google Custom Search para buscar informações relacionadas ao termo de pesquisa fornecido.

    Args:
        search_term (str): O termo de pesquisa para ser consultado.
        api_key (str): A chave da API para autenticação.
        cse_id (str): O ID do mecanismo de pesquisa personalizado (Custom Search Engine ID).
        **kwargs: Parâmetros adicionais para a requisição da API (opcional).

    Returns:
        dict: O JSON de resposta da API, contendo os resultados da pesquisa.

    Raises:
        HTTPError: Se a requisição para a API falhar.
    """
    service_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id,
    }
    params.update(kwargs)

    response = requests.get(service_url, params=params)
    response.raise_for_status()

    return response.json()

def find_results(search_term, api_key, cse_id, **kwargs):
    """
    Busca e salva os links dos resultados da pesquisa em um arquivo.

    Esta função utiliza a função google_search para obter os resultados de pesquisa e grava os links dos resultados em um arquivo de texto.

    Args:
        search_term (str): O termo de pesquisa para ser consultado.
        api_key (str): A chave da API para autenticação.
        cse_id (str): O ID do mecanismo de pesquisa personalizado (Custom Search Engine ID).
        **kwargs: Parâmetros adicionais para a pesquisa (opcional).

    Returns:
        None
    """
    response = google_search(search_term, api_key, cse_id, **kwargs)
    results = response.get('items', [])

    with open("targets.txt", "a") as file:
        for result in results:
            link = result.get('link')
            if link:
                file.write(link + '\n')
                print(link)

if __name__ == '__main__':
    api_key = 'AIzaSyBvYRkuxbWRTU5A-s9RG-dJJF6XNkGX7FY'
    cse_id = 'e69c157c6ecb74fa2'
    
    search_term = 'intitle:index of /etc/ssh'
    find_results(search_term, api_key, cse_id)