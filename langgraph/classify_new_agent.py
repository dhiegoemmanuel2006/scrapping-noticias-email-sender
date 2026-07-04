from langchain_core.prompts import ChatPromptTemplate
from langgraph.state import Estado, NoticiaClassificada
import logging



CLASSIFICADOR_EMAILS_PROMPT = ChatPromptTemplate(
    [('system', '''Você é um curador e classificador de notícias. Receberá um JSON contendo uma lista de notícias, cada uma com fonte, título e link.

Regras de Classificação:
1. RELEVANTE: Apenas notícias sobre Política, Copa do Mundo ou Cultura, E que sejam estritamente originárias das fontes "Midia Ninja" ou "G1".
2. NÃO RELEVANTE: Notícias sobre outros temas ou de fontes diferentes. (Estas devem ser ignoradas e removidas do resultado final).

Para cada notícia classificada como RELEVANTE, você deve preencher os campos `titulo`, `link` e `fonte` exatamente como constam no JSON de entrada. Não altere os links ou os títulos.
'''),
    ('user', 'Noticias em JSON: {news}')]
)


from pydantic import BaseModel

class ListaNoticias(BaseModel):
    noticias: list[NoticiaClassificada]

def classifier_agent(llm, state: Estado):
    prompt_classifier = CLASSIFICADOR_EMAILS_PROMPT.format_messages(
        news=state["noticias_curadas"]
    )

    llm_classifier = llm.with_structured_output(ListaNoticias)
    result = llm_classifier.invoke(prompt_classifier)
    
    if result and hasattr(result, 'noticias'):
        state["noticias_classificadas"] = result.noticias
        logging.info("Notícias classificadas com sucesso")
        return state
    else:
        logging.error("Falha ao classificar notícias")
        state["noticias_classificadas"] = []
        return state
