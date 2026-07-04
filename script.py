"""
Initialize script for all scrapings and email sending.

Pass 1:
    Run scrapping to get all news.
    Save in a JSON file.
    

Pass 2:
    AI Model for verify if it's important to me, based in a prompt.

    AI Model create a html template for sending all news on email

Pass 3:
    Sending Email to me of all news important

Pass 4:
    Close email connection


"""
import os
import sys
import json
import logging
from dotenv import load_dotenv

from scrapping.scrapping_g1 import make_request_g1, scrapping_news_g1
from scrapping.scrapping_midia_ninja import make_request_midia_ninja, scrapping_news_midia_ninja
from langgraph.orquestre import agents_workflow
from email_sender.email import email_server, send_email_template

from utils.json_utils import clean_json_file, ler_noticias_json, append_in_json_file

# Configuração global de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Inicializa as variáveis de ambiente
load_dotenv()

# URLs para raspagem
URL_G1 = "https://g1.globo.com/"
URL_MIDIA_NINJA = "https://midianinja.org/"

def main():
    # Pass 1: Run scrapping para pegar todas noticias. Salvar em JSON
    logging.info("Passo 1: Iniciando a raspagem de notícias...")
    
    # Limpa o arquivo de notícias para evitar acúmulos redundantes de execuções anteriores
    clean_json_file()
    
    # Raspagem G1
    logging.info("Buscando notícias no G1...")
    g1_response = make_request_g1(URL_G1)
    if not g1_response:
        logging.error("Erro ao fazer requisição para o G1")
    else:
        g1_news = scrapping_news_g1(g1_response)
        if g1_news:
            append_in_json_file(g1_news)
            logging.info("Notícias do G1 salvas com sucesso.")
        else:
            logging.warning("Nenhuma notícia coletada do G1.")
            
    # Raspagem Mídia Ninja
    logging.info("Buscando notícias na Mídia Ninja...")
    mn_response = make_request_midia_ninja(URL_MIDIA_NINJA)
    if not mn_response:
        logging.error("Erro ao fazer requisição para Mídia Ninja")
    else:
        mn_news = scrapping_news_midia_ninja(mn_response)
        if mn_news:
            append_in_json_file(mn_news)
            logging.info("Notícias da Mídia Ninja salvas com sucesso.")
        else:
            logging.warning("Nenhuma notícia coletada da Mídia Ninja.")

    # Pass 2: Modelo de IA para processamento e classificação das noticias usando langgraph
    logging.info("Passo 2: Processando notícias com IA usando LangGraph...")
    noticias = ler_noticias_json()
    if not noticias:
        logging.error("Nenhuma notícia encontrada nos arquivos de raspagem. Pipeline encerrado.")
        sys.exit()

    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        logging.error("Erro: GOOGLE_API_KEY não configurada no arquivo .env.")
        sys.exit()

    # Executa o grafo compilado
    app = agents_workflow()
    
    initial_state = {
        "noticias_curadas": json.dumps(noticias, ensure_ascii=False),
        "noticias_classificadas": [],
        "html_gerado": ""
    }
    
    # Executa o workflow com o estado inicial
    logging.info("Executando workflow (isso pode levar alguns segundos)...")
    final_state = app.invoke(initial_state)
    html_gerado = final_state.get("html_gerado", "")

    if not html_gerado:
        logging.error("Erro: O HTML gerado pelo LangGraph está vazio.")
        sys.exit()

    caminho_html = os.path.join(os.getcwd(), 'news', 'template_email.html')
    with open(caminho_html, 'w', encoding='utf-8') as f:
        f.write(html_gerado)
        
    logging.info(f"HTML gerado com sucesso em: {caminho_html}")

    # Pass 3: Envio do e-mail com as notícias
    logging.info("Passo 3: Enviando e-mail de notícias...")
    email_usr = os.getenv("EMAIL")
    password_usr = os.getenv("PASSWORD_EMAIL")
    
    if not email_usr or not password_usr:
        logging.error("Erro: EMAIL ou PASSWORD_EMAIL não configurados no arquivo .env.")
        sys.exit()

    email_smtp = email_server(email_usr, password_usr)
    send_email_template(email_smtp, "Noticias do dia para você Dhiego", html_gerado, email_usr)

    # Pass 4: Fechando conexão do email
    logging.info("Passo 4: Fechando conexão com o servidor de e-mail...")
    email_smtp.close()
    logging.info("Pipeline de integração concluído com sucesso!")

if __name__ == "__main__":
    main()