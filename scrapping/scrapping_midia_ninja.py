from bs4 import BeautifulSoup
import logging
from utils.http_utils import make_request
from utils.json_utils import append_in_json_file

# Configuração básica do logging para quando o script rodar diretamente
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Coleta do HTML
def make_request_midia_ninja(url):
    return make_request(url)

# Mineração dos dados de Noticias
def scrapping_news_midia_ninja(response):
    soup = BeautifulSoup(response, 'html.parser')
    posts = soup.select('.post')
    
    news_list = []
    for post in posts:
        h2 = post.find('h2')
        a_tag = post.find_parent('a')
        
        if h2 and a_tag:
            titulo = h2.text.strip()
            link = a_tag.get('href')
            
            if titulo and link:
                news_list.append({
                    "fonte": "Midia Ninja",
                    "titulo": titulo,
                    "link": link
                })
                
    if news_list:
        return news_list
    else:
        logging.warning("Nenhum post encontrado na Mídia Ninja")
        return None

if __name__ == '__main__':
    url = "https://midianinja.org/"
    response = make_request_midia_ninja(url)
    if not response:
        logging.error("Erro ao fazer requisição para Midia Ninja")
        import sys; sys.exit()

    news = scrapping_news_midia_ninja(response)
    if not news:
        logging.error("Erro ao fazer scrapping para Midia Ninja")
        import sys; sys.exit()

    append_in_json_file(news)