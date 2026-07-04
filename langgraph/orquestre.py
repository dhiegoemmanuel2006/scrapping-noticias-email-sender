from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from functools import partial

# Importando o Estado e os Agentes
from langgraph.state import Estado
from langgraph.classify_new_agent import classifier_agent
from langgraph.email_designer import designer_agent

import os
from dotenv import load_dotenv

# Carrega env vars
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

def agents_workflow():
    workflow = StateGraph(Estado)
    
    # Adicionando os nós (nodes) injetando o llm em cada agente
    workflow.add_node("classifier_node", partial(classifier_agent, llm))
    workflow.add_node("designer_node", partial(designer_agent, llm))
    
    # Definindo o fluxo (edges)
    workflow.add_edge(START, "classifier_node")
    workflow.add_edge("classifier_node", "designer_node")
    workflow.add_edge("designer_node", END)
    
    app = workflow.compile()
    return app
