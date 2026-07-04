from typing import TypedDict, Annotated
from pydantic import BaseModel, Field

class NoticiaClassificada(BaseModel):
    titulo: str = Field(description="O título exato da notícia")
    link: str = Field(description="O link/URL exato da notícia")
    fonte: str = Field(description="A fonte da notícia (G1 ou Midia Ninja)")
    categoria: str = Field(description="Categoria principal (ex: Tecnologia, Economia, Esportes)")
    prioridade: str = Field(description="Nível de relevância: Alta, Média ou Baixa")
    resumo_critico: str = Field(description="Um resumo de duas frases focando no impacto da notícia")
    
class Estado(TypedDict):
    noticias_curadas: str 
    noticias_classificadas: list[NoticiaClassificada]
    html_gerado: str