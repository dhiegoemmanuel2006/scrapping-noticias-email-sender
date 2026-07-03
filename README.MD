# 📰 News Scraping & Email Sender

> **[Leia em Português](#-português)**

---

## 🇬🇧 English

An automated pipeline that scrapes news from Brazilian portals, filters them with AI, and delivers a curated HTML newsletter straight to your inbox.

### ✨ Features

| Step | Description |
|------|-------------|
| **1. Web Scraping** | Collects headlines and links from **G1** and **Mídia Ninja** |
| **2. AI Curation** | Gemini 2.5 Flash classifies and filters news by relevance (Politics, World Cup, Culture) |
| **3. HTML Generation** | Generates a clean, responsive email template with inline CSS |
| **4. Email Delivery** | Sends the newsletter via Gmail using `yagmail` |

### 📁 Project Structure

```
script-noticias-scrapping/
├── script.py                          # Main orchestrator – runs the full pipeline
├── scrapping/
│   ├── scrapping_g1.py                # G1 portal scraper
│   └── scrapping_midia_ninja.py       # Mídia Ninja portal scraper
├── model/
│   ├── email_classify_agent.py        # LangChain agent (Gemini 2.5 Flash)
│   └── PROMPT.MD                      # AI prompt template (editable)
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
Passo 1: Iniciando a raspagem de notícias...
Buscando notícias no G1...
Notícias do G1 salvas com sucesso.
Buscando notícias na Mídia Ninja...
Notícias da Mídia Ninja salvas com sucesso.

Passo 2: Processando notícias com IA (prompt lido de PROMPT.MD)...
HTML gerado com sucesso em: .../news/template_email.html

Passo 3: Enviando e-mail de notícias...
Email enviado com sucesso

Passo 4: Fechando conexão com o servidor de e-mail...
Pipeline de integração concluído com sucesso!
```

### 🤖 Customizing the AI Prompt

The AI behavior is fully controlled by the file [`model/PROMPT.MD`](model/PROMPT.MD). You can edit it to:

- Change which **topics** are considered relevant
- Modify the **HTML structure** of the generated email
- Adjust the **email title** or layout rules

No code changes needed — just edit the markdown file and re-run the script.

### 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `beautifulsoup4` | HTML parsing for web scraping |
| `requests` | HTTP requests to news portals |
| `langchain` | LLM orchestration framework |
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
| **2. Curadoria com IA** | Gemini 2.5 Flash classifica e filtra notícias por relevância (Política, Copa do Mundo, Cultura) |
| **3. Geração de HTML** | Gera um template de e-mail limpo e responsivo com CSS inline |
| **4. Envio de E-mail** | Envia a newsletter via Gmail usando `yagmail` |

### 📁 Estrutura do Projeto

```
script-noticias-scrapping/
├── script.py                          # Orquestrador principal – executa todo o pipeline
├── scrapping/
│   ├── scrapping_g1.py                # Raspador do portal G1
│   └── scrapping_midia_ninja.py       # Raspador do portal Mídia Ninja
├── model/
│   ├── email_classify_agent.py        # Agente LangChain (Gemini 2.5 Flash)
│   └── PROMPT.MD                      # Template de prompt da IA (editável)
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
Passo 1: Iniciando a raspagem de notícias...
Buscando notícias no G1...
Notícias do G1 salvas com sucesso.
Buscando notícias na Mídia Ninja...
Notícias da Mídia Ninja salvas com sucesso.

Passo 2: Processando notícias com IA (prompt lido de PROMPT.MD)...
HTML gerado com sucesso em: .../news/template_email.html

Passo 3: Enviando e-mail de notícias...
Email enviado com sucesso

Passo 4: Fechando conexão com o servidor de e-mail...
Pipeline de integração concluído com sucesso!
```

### 🤖 Personalizando o Prompt da IA

O comportamento da IA é totalmente controlado pelo arquivo [`model/PROMPT.MD`](model/PROMPT.MD). Você pode editá-lo para:

- Mudar quais **temas** são considerados relevantes
- Modificar a **estrutura HTML** do e-mail gerado
- Ajustar o **título do e-mail** ou regras de layout

Nenhuma alteração no código é necessária — basta editar o arquivo markdown e re-executar o script.

### 📦 Dependências

| Pacote | Finalidade |
|--------|------------|
| `beautifulsoup4` | Parsing de HTML para web scraping |
| `requests` | Requisições HTTP para portais de notícias |
| `langchain` | Framework de orquestração de LLMs |
| `langchain-google-genai` | Integração com Google Gemini |
| `python-dotenv` | Carregamento de variáveis de ambiente |
| `yagmail` | Envio de e-mails via Gmail |

### 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.13+
- **Modelo de IA:** Google Gemini 2.5 Flash (via LangChain)
- **Scraping:** BeautifulSoup4 + Requests
- **E-mail:** yagmail (Gmail SMTP)
- **Gerenciador de Pacotes:** uv
