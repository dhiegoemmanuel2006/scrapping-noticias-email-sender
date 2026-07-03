import os
import json
import requests

def make_request(url):
    try:
        request = requests.get(url)
        if request.status_code == 200:
            return request.text
    except Exception as e:
        print(f"Erro na requisição para {url}: {e}")
    return None

def append_in_json_file(post_list):
    path = os.getcwd()
    arquivo = os.path.join(path, 'news', 'noticias.json')

    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            try:
                dados_atuais = json.load(f)
            except json.JSONDecodeError:
                dados_atuais = []
    else:
        os.makedirs(os.path.dirname(arquivo), exist_ok=True)
        dados_atuais = []

    dados_atuais.append(post_list)

    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados_atuais, f, ensure_ascii=False, indent=4)
