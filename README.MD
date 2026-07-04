# 📰 News Scraping & Email Sender

> **[Leia em Português](#-português)**

---

## 🇬🇧 English

An automated pipeline that scrapes news from Brazilian portals, filters them with AI, and delivers a curated HTML newsletter straight to your inbox.

### ✨ Features

| Step | Description |
|------|-------------|
| **1. Web Scraping** | Collects headlines and links from **G1** and **Mídia Ninja** |
| **2. AI Orchestration** | **LangGraph** orchestrates two Gemini 2.5 Flash agents: a **Classifier** (filters by relevance) and a **Designer** (generates high-quality HTML) |
| **3. Email Delivery** | Sends the curated newsletter via Gmail using `yagmail` |

### 📁 Project Structure

```
script-noticias-scrapping/
├── script.py                          # Main orchestrator – runs the full pipeline
├── scrapping/
│   ├── scrapping_g1.py                # G1 portal scraper
│   └── scrapping_midia_ninja.py       # Mídia Ninja portal scraper
├── langgraph/                         # LangGraph multi-agent orchestration
│   ├── orquestre.py                   # LangGraph workflow setup
│   ├── classify_new_agent.py          # Agent: Classifies relevant news
│   ├── email_designer.py              # Agent: Generates email HTML
│   └── state.py                       # Shared state schema
├── utils/
│   ├── http_utils.py                  # HTTP requests handler
│   └── json_utils.py                  # JSON manipulation handler
├── email_sender/
│   └── email.py                       # Email server setup and dispatch
├── news/
│   ├── noticias.json                  # Scraped news (auto-generated)
│   └── template_email.html            # Generated HTML template (auto-generated)
├── .env                               # Environment variables (secrets)
├── .gitignore
├── pyproject.toml                     # Project metadata & dependencies
└── uv.lock                           # Dependency lockfile
```

### ⚙️ Prerequisites

- **Python** ≥ 3.13
- **[uv](https://docs.astral.sh/uv/)** — Fast Python package manager
- **Google API Key** — For the Gemini 2.5 Flash model
- **Gmail App Password** — For sending emails via `yagmail`

### 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dhiegoemmanuel2006/scrapping-noticias-email-sender.git
   cd scrapping-noticias-email-sender
   ```

2. **Install dependencies with uv**
   ```bash
   uv sync
   ```

3. **Configure environment variables**

   Create a `.env` file at the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   EMAIL=your_email@gmail.com
   PASSWORD_EMAIL=your_gmail_app_password
   ```

   > **Note:** Use a [Gmail App Password](https://support.google.com/accounts/answer/185833), not your regular password.

### ▶️ Usage

```bash
uv run script.py
```

**Pipeline output:**
```
2026-07-04 19:21:15,573 - INFO - Passo 1: Iniciando a raspagem de notícias...
2026-07-04 19:21:15,574 - INFO - Buscando notícias no G1...
2026-07-04 19:21:15,995 - INFO - Notícias do G1 salvas com sucesso.
2026-07-04 19:21:15,995 - INFO - Buscando notícias na Mídia Ninja...
2026-07-04 19:21:17,694 - INFO - Notícias da Mídia Ninja salvas com sucesso.
2026-07-04 19:21:17,695 - INFO - Passo 2: Processando notícias com IA usando LangGraph...
2026-07-04 19:21:17,696 - INFO - Executando workflow (isso pode levar alguns segundos)...
2026-07-04 19:21:59,424 - INFO - Notícias classificadas com sucesso
2026-07-04 19:22:04,759 - INFO - Html gerado com sucesso
2026-07-04 19:22:04,761 - INFO - HTML gerado com sucesso em: ...\news\template_email.html
2026-07-04 19:22:04,761 - INFO - Passo 3: Enviando e-mail de notícias...
2026-07-04 19:22:07,427 - INFO - Email enviado com sucesso
2026-07-04 19:22:07,428 - INFO - Passo 4: Fechando conexão com o servidor de e-mail...
2026-07-04 19:22:07,609 - INFO - Pipeline de integração concluído com sucesso!
```

### 🤖 Customizing the AI Prompts

The AI behavior is orchestrated via LangGraph and controlled by two main agents:

- **[`langgraph/classify_new_agent.py`](langgraph/classify_new_agent.py)**: Edit the prompt here to change which **topics** are considered relevant and how they are structured.
- **[`langgraph/email_designer.py`](langgraph/email_designer.py)**: Edit the prompt here to modify the **HTML structure**, layout rules, and visual style of the generated email.

No main code changes needed — just edit the prompts in these agents and re-run the script.

### 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `beautifulsoup4` | HTML parsing for web scraping |
| `requests` | HTTP requests to news portals |
| `langgraph` | Multi-agent orchestration framework |
| `langchain-google-genai` | Google Gemini integration |
| `python-dotenv` | Environment variable loading |
| `yagmail` | Gmail email sending |

### 🛠️ Tech Stack

- **Language:** Python 3.13+
- **AI Model:** Google Gemini 2.5 Flash (via LangChain)
- **Scraping:** BeautifulSoup4 + Requests
- **Email:** yagmail (Gmail SMTP)
- **Package Manager:** uv

---

## 🇧🇷 Português

Um pipeline automatizado que faz raspagem de notícias de portais brasileiros, filtra com IA e entrega uma newsletter HTML curada direto na sua caixa de entrada.

### ✨ Funcionalidades

| Etapa | Descrição |
|-------|-----------|
| **1. Web Scraping** | Coleta manchetes e links do **G1** e **Mídia Ninja** |
| **2. Orquestração com IA** | **LangGraph** orquestra dois agentes (Gemini 2.5 Flash): um **Classificador** (filtra por relevância) e um **Designer** (gera HTML de alta qualidade) |
| **3. Envio de E-mail** | Envia a newsletter curada via Gmail usando `yagmail` |

### 📁 Estrutura do Projeto

```
script-noticias-scrapping/
├── script.py                          # Orquestrador principal – executa todo o pipeline
├── scrapping/
│   ├── scrapping_g1.py                # Raspador do portal G1
│   └── scrapping_midia_ninja.py       # Raspador do portal Mídia Ninja
├── langgraph/                         # Orquestração multi-agente LangGraph
│   ├── orquestre.py                   # Setup do workflow do LangGraph
│   ├── classify_new_agent.py          # Agente: Classifica as notícias relevantes
│   ├── email_designer.py              # Agente: Gera o HTML do e-mail
│   └── state.py                       # Esquema de estado (State schema)
├── utils/
│   ├── http_utils.py                  # Utilitário para requisições HTTP
│   └── json_utils.py                  # Utilitário para manipulação de JSON
├── email_sender/
│   └── email.py                       # Configuração e envio de e-mail
├── news/
│   ├── noticias.json                  # Notícias raspadas (gerado automaticamente)
│   └── template_email.html            # Template HTML gerado (gerado automaticamente)
├── .env                               # Variáveis de ambiente (segredos)
├── .gitignore
├── pyproject.toml                     # Metadados e dependências do projeto
└── uv.lock                           # Lockfile de dependências
```

### ⚙️ Pré-requisitos

- **Python** ≥ 3.13
- **[uv](https://docs.astral.sh/uv/)** — Gerenciador de pacotes Python rápido
- **Google API Key** — Para o modelo Gemini 2.5 Flash
- **Senha de App do Gmail** — Para envio de e-mails via `yagmail`

### 🚀 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/dhiegoemmanuel2006/scrapping-noticias-email-sender.git
   cd scrapping-noticias-email-sender
   ```

2. **Instale as dependências com uv**
   ```bash
   uv sync
   ```

3. **Configure as variáveis de ambiente**

   Crie um arquivo `.env` na raiz do projeto:
   ```env
   GOOGLE_API_KEY=sua_google_api_key_aqui
   EMAIL=seu_email@gmail.com
   PASSWORD_EMAIL=sua_senha_de_app_gmail
   ```

   > **Nota:** Use uma [Senha de App do Gmail](https://support.google.com/accounts/answer/185833), não sua senha normal.

### ▶️ Como Usar

```bash
uv run script.py
```

**Saída do pipeline:**
```
2026-07-04 19:21:15,573 - INFO - Passo 1: Iniciando a raspagem de notícias...
2026-07-04 19:21:15,574 - INFO - Buscando notícias no G1...
2026-07-04 19:21:15,995 - INFO - Notícias do G1 salvas com sucesso.
2026-07-04 19:21:15,995 - INFO - Buscando notícias na Mídia Ninja...
2026-07-04 19:21:17,694 - INFO - Notícias da Mídia Ninja salvas com sucesso.
2026-07-04 19:21:17,695 - INFO - Passo 2: Processando notícias com IA usando LangGraph...
2026-07-04 19:21:17,696 - INFO - Executando workflow (isso pode levar alguns segundos)...
2026-07-04 19:21:59,424 - INFO - Notícias classificadas com sucesso
2026-07-04 19:22:04,759 - INFO - Html gerado com sucesso
2026-07-04 19:22:04,761 - INFO - HTML gerado com sucesso em: ...\news\template_email.html
2026-07-04 19:22:04,761 - INFO - Passo 3: Enviando e-mail de notícias...
2026-07-04 19:22:07,427 - INFO - Email enviado com sucesso
2026-07-04 19:22:07,428 - INFO - Passo 4: Fechando conexão com o servidor de e-mail...
2026-07-04 19:22:07,609 - INFO - Pipeline de integração concluído com sucesso!
```

### 🤖 Personalizando os Prompts da IA

O comportamento da IA é orquestrado via LangGraph e controlado por dois agentes principais:

- **[`langgraph/classify_new_agent.py`](langgraph/classify_new_agent.py)**: Edite o prompt aqui para mudar quais **temas** são considerados relevantes.
- **[`langgraph/email_designer.py`](langgraph/email_designer.py)**: Edite o prompt aqui para modificar a **estrutura HTML**, regras de layout e estilo visual do e-mail gerado.

Nenhuma alteração na lógica principal é necessária — basta editar os prompts desses agentes e re-executar o script.

### 📦 Dependências

| Pacote | Finalidade |
|--------|------------|
| `beautifulsoup4` | Parsing de HTML para web scraping |
| `requests` | Requisições HTTP para portais de notícias |
| `langgraph` | Framework de orquestração multi-agente |
| `langchain-google-genai` | Integração com Google Gemini |
| `python-dotenv` | Carregamento de variáveis de ambiente |
| `yagmail` | Envio de e-mails via Gmail |

### 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.13+
- **Modelo de IA:** Google Gemini 2.5 Flash (via LangChain)
- **Scraping:** BeautifulSoup4 + Requests
- **E-mail:** yagmail (Gmail SMTP)
- **Gerenciador de Pacotes:** uv
