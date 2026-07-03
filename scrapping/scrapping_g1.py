from bs4 import BeautifulSoup
from scrapping.utils import make_request, append_in_json_file

# Request para coleta do HTML
def make_request_g1(url):
    return make_request(url)

# Mineração dos dados de Noticias
def scrapping_news_g1(response):
    soup = BeautifulSoup(response, 'html.parser')
    posts = soup.select('.feed-post-link')
    
    if len(posts) > 0:
        post_list = {
            "G1" : {
                "name" : "G1",
                "title" : [],
                "link" : []
            }
        }
        for post in posts:
            titulo = post.text.strip()
            link = post.get('href')
            
            if titulo and link:
                post_list["G1"]["title"].append(titulo)
                post_list["G1"]["link"].append(link)
        
        if len(post_list["G1"]["title"]) > 0 and len(post_list["G1"]["link"]) > 0:
            return post_list["G1"]
    else:
        print("Nenhum post encontrado no G1")
        return None

# Inicialização
if __name__ == '__main__':
    url = "https://g1.globo.com/"
    response = make_request_g1(url)
    if not response:
        print("Erro ao fazer requisição para o G1")
        import sys; sys.exit()

    news = scrapping_news_g1(response)
    if not news:
        print("Erro ao fazer scrapping para o G1")
        import sys; sys.exit()

    append_in_json_file(news)