# Oráculo - Assistente de IA para Análise de Documentos

## Visão Geral

Oráculo é uma aplicação web interativa que permite processar e interagir com diversos formatos de dados através de modelos de linguagem avançados. A solução oferece uma interface intuitiva para extração e análise de informações a partir de múltiplas fontes.

## Principais Recursos

### Processamento de Documentos

- Suporte para múltiplos formatos:
  - Conteúdo web (via URL)
  - Vídeos do YouTube (transcrição automática)
  - Arquivos PDF (extração de texto)
  - Dados estruturados (CSV)
  - Texto puro (TXT)

### Integrações com Modelos de Linguagem

- Provedores suportados:
  - Ollama (execução local)
  - Groq (alta performance)
  - OpenAI (GPT family)

### Funcionalidades Avançadas

- Memória de conversação persistente
- Contextualização de respostas baseada nos documentos carregados
- Gerenciamento de estado da sessão
- Interface modular e extensível

## Requisitos do Sistema

- Python 3.11 ou superior
- Gerenciador de pacotes pip
- Contas ativas nos serviços de LLM (para provedores cloud)

## Configuração Inicial

### Instalação

1. Clonar o repositório:
   ```bash
   git clone https://github.com/seu-usuario/oraculo.git
   cd oraculo
   ```

2. Configurar ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Configuração de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Configuração opcional
USER_AGENT="Seu User Agent Personalizado"
```

## Utilização

Iniciar a aplicação:

```bash
streamlit run app.py
```

Na interface web:

- Selecione o tipo de conteúdo na aba "Upload de arquivos"
- Escolha o provedor e modelo na aba "Seleção de modelo"
- Para provedores cloud, **insira a chave de API** correspondente
   - Para OPENAI_API_KEY, acesse https://platform.openai.com/api-keys
   - Para GROQ_API_KEY, acesse https://console.groq.com/keys
- Clique em "Iniciar Oráculo" para carregar o sistema
- Interaja com o assistente através do campo de chat na página principal

## Arquitetura Técnica

### Componentes Principais

- `app.py`: Fluxo principal da aplicação Streamlit
- `utils/configs.py`: Configurações de modelos e provedores
- `utils/loaders.py`: Implementações de carregadores de documentos

### Dependências Principais

- Framework: Streamlit
- Processamento de LLMs: LangChain

#### Provedores

- Ollama: `langchain_community`
- Groq: `langchain_groq`
- OpenAI: `langchain_openai`

#### Manipulação de documentos

- PDF: `PyPDF2`
- CSV: `pandas`
- YouTube: `youtube-transcript-api`

## Roadmap

### Próximas Versões

- Integração com bancos de dados vetoriais
- Suporte a documentos Office (DOCX, XLSX)
- Sistema de autenticação de usuários
- Dashboard de métricas de uso

### Melhorias Planejadas

- Implementação de cache para documentos processados
- Pré-processamento assíncrono de arquivos grandes
- Exportação de conversas em múltiplos formatos

## Licença

Distribuído sob a licença MIT. Veja o arquivo LICENSE para mais informações.

## Contato

Para questões técnicas ou suporte, abra uma issue no repositório do projeto.