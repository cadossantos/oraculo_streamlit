# CHANGELOG - Integração com Ollama (modelo local)

**Data**: 2025-05-15  
**Versão**: v0.2.0-beta

## Novidades

- Suporte a provedores locais com Ollama:
  - Adicionado Ollama como novo provedor de modelos no dicionário `config_modelos`
  - Implementado suporte ao modelo `llama3.1:8b` rodando localmente via `ChatOllama`

## Alterações Técnicas

### Novas Dependências
- Adicionado pacote `langchain_community`:
  ```bash
  pip install -U langchain_community
  ```

### Modificações no Código
* Arquivo utils/configs.py:

  * Importado ChatOllama de langchain_community

  * Adicionado dicionário de configuração do Ollama:

```python
'Ollama': {
  'modelos': ['llama3.1:8b'],
  'chat': ChatOllama
}
```
* Função carrega_modelo() (em app.py):

  * Implementado tratamento específico para Ollama (não exige API Key)

  * Adicionada persistência do nome do modelo em st.session_state['modelo_nome']

* Interface:

  * Quando o provedor é Ollama, o campo de chave de API é ocultado na sidebar

  * Corrigido acesso a model_name (não existente em ChatOllama)

  * Implementada exibição segura via st.session_state.get('modelo_nome')

### Implementações Futuras (Planejadas)
Carregadores de Documentos (utils/loaders.py)
Será adicionado suporte para carregamento de múltiplos formatos de documentos:

```python
from langchain_community.document_loaders import (
    WebBaseLoader,
    YoutubeLoader,
    CSVLoader,
    PyPDFLoader,
    TextLoader
)

def carrega_site(url):
    loader = WebBaseLoader(url)
    lista_documentos = loader.load()
    return '\n\n'.join([doc.page_content for doc in lista_documentos])

...
```
### Testes Realizados
* Ollama ativo com modelo llama3.1:8b carregado localmente

* Verificação de compatibilidade com outros provedores (Groq, OpenAI)

### Requisitos e Limitações
* Pré-requisitos para uso com Ollama:

  * Serviço Ollama deve estar em execução (ollama serve)

  * Modelo deve estar disponível localmente (ollama run llama3.1:8b)

### Limitações conhecidas:

* Falhas de conexão com localhost:11434 não estão tratadas

* Carregadores de documentos ainda não estão integrados ao fluxo principal (implementação planejada para v0.3.0)