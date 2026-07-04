from langchain_core.prompts import ChatPromptTemplate
from langgraph.state import Estado
import logging

PROMPT_DESIGNER = ChatPromptTemplate.from_messages([
    ("system", """Você é um designer de e-mail e desenvolvedor front-end especialista em newsletters de alto padrão.
Sua tarefa é gerar o código HTML completo, responsivo e inline-styled de uma newsletter contendo a lista de notícias fornecidas.

Diretrizes de Estilo e Design:
1. CORES E ESTÉTICA: Design limpo e moderno. Use fundo claro (#f4f6f8), com um container centralizado em fundo branco (#ffffff), borda sutil (#e1e4e6) e cantos arredondados (8px). Use tipografia profissional sans-serif (como 'Inter', Arial, sans-serif) com bom contraste.
2. CABEÇALHO: Inclua um cabeçalho elegante com o título principal "Curadoria Diária de Notícias" e um subtítulo agradável.
3. CARDS DE NOTÍCIA: Cada notícia classificada no JSON recebido deve ser exibida como um card individual com:
   - Uma tag/badge de Categoria destacada com uma cor de fundo suave correspondente à categoria (ex: azul claro para Política, verde claro para Copa do Mundo, etc.).
   - A fonte da notícia indicada (ex: "Fonte: G1").
   - O título real da notícia em destaque.
   - O resumo crítico em texto corrido e legível.
   - Um botão ou link estilizado de forma premium para "Acessar Matéria" com a exata label 'acesse', cujo atributo href DEVE ser o link real da notícia fornecido no JSON de entrada. Não invente links e não use "#" se o link estiver disponível.
4. RESPONSIVIDADE: O HTML deve ser bem estruturado (max-width: 600px, centralizado) para que renderize de forma perfeita no Gmail, Outlook e dispositivos móveis.
5. FORMATO DE SAÍDA: Retorne APENAS o código HTML puro, começando direto em <html> ou <div. Não envolva o código em tags de markdown (como ```html)."""),
    ("user", "Gere o HTML da newsletter contendo as seguintes notícias classificadas em JSON:\n{news_classificadas}")
])

import json

def designer_agent(llm, state: Estado):
    if not state.get('noticias_classificadas'):
        logging.error("Nenhuma notícia para ser exibida no email.")
        return state
        
    news_list_dict = [news.model_dump() for news in state["noticias_classificadas"]]
    news_json = json.dumps(news_list_dict, ensure_ascii=False, indent=2)
    
    prompt_designer = PROMPT_DESIGNER.invoke({
        "news_classificadas": news_json
    })
    
    result = llm.invoke(prompt_designer)
    if result:
        state['html_gerado'] = result.content
        logging.info("Html gerado com sucesso")
        return state
    
    logging.error("Falha ao gerar html")
    state['html_gerado'] = ""
    return state