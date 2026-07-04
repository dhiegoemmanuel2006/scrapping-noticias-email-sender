import os
import json

def clean_json_file():
    path = os.getcwd()
    arquivo = os.path.join(path, 'news', 'noticias.json')
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=4)

def ler_noticias_json():
    arquivo = os.path.join(os.getcwd(), 'news', 'noticias.json')
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

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

    if isinstance(post_list, list):
        dados_atuais.extend(post_list)
    else:
        dados_atuais.append(post_list)

    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados_atuais, f, ensure_ascii=False, indent=4)
