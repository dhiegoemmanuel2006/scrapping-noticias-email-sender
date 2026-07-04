from bs4 import BeautifulSoup
import logging
from utils.http_utils import make_request
from utils.json_utils import append_in_json_file

# Configuração básica do logging para quando o script rodar diretamente
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Request para coleta do HTML
def make_request_g1(url):
    return make_request(url)

# Mineração dos dados de Noticias
def scrapping_news_g1(response):
    soup = BeautifulSoup(response, 'html.parser')
    posts = soup.select('.feed-post-link')
    
    news_list = []
    for post in posts:
        titulo = post.text.strip()
        link = post.get('href')
        
        if titulo and link:
            news_list.append({
                "fonte": "G1",
                "titulo": titulo,
                "link": link
            })
            
    if news_list:
        return news_list
    else:
        logging.warning("Nenhum post encontrado no G1")
        return None

# Inicialização
if __name__ == '__main__':
    url = "https://g1.globo.com/"
    response = make_request_g1(url)
    if not response:
        logging.error("Erro ao fazer requisição para o G1")
        import sys; sys.exit()

    news = scrapping_news_g1(response)
    if not news:
        logging.error("Erro ao fazer scrapping para o G1")
        import sys; sys.exit()

    append_in_json_file(news)