import requests
import logging

def make_request(url):
    try:
        request = requests.get(url)
        if request.status_code == 200:
            return request.text
    except Exception as e:
        logging.error(f"Erro na requisição para {url}: {e}")
    return None
