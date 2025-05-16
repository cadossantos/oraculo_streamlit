# CHANGELOG

Todos as mudanças notáveis neste projeto serão documentadas neste arquivo.  

## [1.0.0] - 15-05-2025
### Added
- **Funcionalidade Principal**: Assistente de IA "Oráculo" com memória de conversação
- **Provedores de Modelos**:
  - Suporte a Ollama (local) com 4 modelos (Llama3, Mistral, CodeLlama, DeepSeek)
  - Integração com Groq (3 modelos)
  - Integração com OpenAI (3 modelos)
- **Carregamento de Documentos**:
  - Sites web via URL com User-Agent configurável
  - Transcrição de vídeos do YouTube
  - Processamento de arquivos (PDF, CSV, TXT) via upload
- **Gerenciamento de Estado**:
  - Persistência do modelo selecionado em `st.session_state`
  - Histórico de conversa com `ConversationBufferMemory`

### Changed
- **Refatoração**:
  - Sistema de prompts dinâmico baseado no tipo de documento
  - Função `carrega_arquivo()` unificada para todos os formatos
- **Interface**:
  - Abas organizadas para upload e seleção de modelo
  - Ocultação automática do campo API Key para Ollama

### Fixed
- Tratamento de erros em carregamento de URLs
- Correção na exibição do nome do modelo para ChatOllama
- Validação de inputs vazios

## [0.2.0-beta] - 14-05-2025
### Added
- Implementação inicial da integração com Ollama
- Adição de `langchain_community` como dependência
- Mecanismo básico de carregamento de documentos

### Changed
- Atualização do dicionário `config_modelos` para suportar Ollama
- Adaptação da UI para provedores locais

## [0.1.0-alpha] - 13-05-2025
### Added
- Estrutura inicial do projeto
- Configurações básicas para Groq e OpenAI
- Esboço das funções de carregamento