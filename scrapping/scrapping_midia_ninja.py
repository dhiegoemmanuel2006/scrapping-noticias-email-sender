from bs4 import BeautifulSoup
from scrapping.utils import make_request, append_in_json_file

# Coleta do HTML
def make_request_midia_ninja(url):
    return make_request(url)

# Mineração dos dados de Noticias
def scrapping_news_midia_ninja(response):
    soup = BeautifulSoup(response, 'html.parser')
    posts = soup.select('main .post')
    if len(posts) > 0:
        posts = soup.select('.post')
        post_list = {
            "Midia" : {
                "name" : "Midia Ninja",
                "title" : [],
                "link" : []
            }
        }
        for post in posts:
            h2 = post.find('h2')
            a_tag = post.find_parent('a')
    
            if h2 and a_tag:
                titulo = h2.text.strip()
                link = a_tag.get('href')
        
                post_list["Midia"]["title"].append(titulo)
                post_list["Midia"]["link"].append(link)
        
        if len(post_list["Midia"]["title"]) > 0 and len(post_list["Midia"]["link"]) > 0:
            return post_list["Midia"]
    else:
        print("Nenhum post encontrado na Mídia Ninja")
        return None

if __name__ == '__main__':
    url = "https://midianinja.org/"
    response = make_request_midia_ninja(url)
    if not response:
        print("Erro ao fazer requisição para Midia Ninja")
        import sys; sys.exit()

    news = scrapping_news_midia_ninja(response)
    if not news:
        print("Erro ao fazer scrapping para Midia Ninja")
        import sys; sys.exit()

    append_in_json_file(news)