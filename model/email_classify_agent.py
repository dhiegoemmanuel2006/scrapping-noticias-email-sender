import json
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Configuração do LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)


# Leitura do prompt
def ler_prompt_md():
    """Lê o prompt do arquivo PROMPT.MD localizado na pasta model/."""
    prompt_path = os.path.join(os.path.dirname(__file__), 'PROMPT.MD')
    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()

# Leitura do JSON de notícias
def ler_noticias_json():
    arquivo = os.path.join(os.getcwd(), 'news', 'noticias.json')
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Geração do HTML
def gerar_html_noticias(noticias):
    """Gera o template HTML de notícias usando o prompt do PROMPT.MD e o modelo de IA."""
    prompt_text = ler_prompt_md()
    # Adiciona a variável {noticias} ao template lido do arquivo
    template = prompt_text + "\n\nNotícias em JSON:\n{noticias}"

    prompt = PromptTemplate.from_template(template)
    agente_curador = prompt | llm | StrOutputParser()

    html_gerado = agente_curador.invoke({
        "noticias": json.dumps(noticias, ensure_ascii=False)
    })

    # Limpeza de formatação markdown residual
    html_gerado = html_gerado.replace("```html", "").replace("```", "").strip()
    return html_gerado

if __name__ == '__main__':
    noticias = ler_noticias_json()
    
    if not noticias:
        print("Nenhuma notícia encontrada.")
        import sys; sys.exit()

    html_gerado = gerar_html_noticias(noticias)

    # Salva o HTML para ser usado pelo seu outro serviço
    caminho_html = os.path.join(os.getcwd(), 'news', 'template_email.html')
    with open(caminho_html, 'w', encoding='utf-8') as f:
        f.write(html_gerado)
        
    print(f"HTML gerado com sucesso em: {caminho_html}")