# Oráculo — Chat Interativo com Seus Dados

**Oráculo** é um WebApp interativo que permite conversar com seus próprios dados — incluindo vídeos do YouTube, arquivos CSV, PDFs e textos. Utilizando modelos de linguagem (LLMs) como OpenAI e Grok, o Oráculo transforma dados em respostas úteis e contextualizadas por meio de uma interface simples desenvolvida com Streamlit.

## Funcionalidades

- Interface web com Streamlit
- Suporte a múltiplos formatos: PDF, CSV, YouTube, TXT
- Escolha entre diferentes LLMs
- Conversational Retrieval Chain com LangChain
- Gerenciamento de contexto e memória da conversa
- Modularização e escalabilidade do código

## Primeiros Passos

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/oraculo.git
cd oraculo
```
2. Crie um ambiente virtual (ex: Conda)

```bash
conda create -n oraculo python=3.11
conda activate oraculo
```
3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Crie um arquivo .env com suas chaves de API
```bash
OPENAI_API_KEY=sk-xxxx
GROQ_API_KEY=xxxx
```
5. Execute o app
```bash
streamlit run app.py
```
## Como Usar
Use a barra lateral para escolher arquivos e modelos

O Oráculo irá processar os dados e responder às suas perguntas com base nas fontes carregadas

Suporta múltiplas interações com contexto salvo em tempo real

### Tecnologias Utilizadas
Python 3.11

Streamlit

LangChain

OpenAI

Grok

[PyPDF, YouTube Transcript API, mais detalhes em **requirements.txt**]

### Funcionalidades Futuras
Integração com banco de dados (PostgreSQL)

Autenticação e múltiplos usuários

Upload assíncrono e pré-processamento

Exportação das respostas

**Contribuindo**
Contribuições são bem-vindas. Crie uma issue ou abra um pull request com melhorias ou correções. Este projeto também é uma excelente oportunidade para praticar o uso de Git e branches.

**Licença**
Distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

**Créditos**
Projeto baseado na iniciativa educacional de Rodrigo da **Asimov Academy**, com desenvolvimento e extensões feitas para fins didáticos e práticos no uso de IA aplicada.