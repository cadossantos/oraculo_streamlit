import streamlit as st
import tempfile
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate

from utils.configs import *
from utils.loaders import *


import tempfile
import streamlit as st

def carrega_arquivo(tipo_arquivo, arquivo):
    documento = None

    try:
        if tipo_arquivo in ['Site', 'YouTube']:
            if not arquivo or not arquivo.strip():
                st.warning('Por favor, insira uma URL válida.')
                return None

        elif tipo_arquivo in ['PDF', 'CSV', 'TXT']:
            if not arquivo:
                st.warning(f'Por favor, faça o upload do arquivo {tipo_arquivo}.')
                return None

        if tipo_arquivo == 'Site':
            documento = carrega_site(arquivo)

        elif tipo_arquivo == 'YouTube':
            documento = carrega_youtube(arquivo)

        elif tipo_arquivo in ['PDF', 'CSV', 'TXT']:
            suffix = f".{tipo_arquivo.lower()}"
            with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as temp_file:
                temp_file.write(arquivo.read())
                path_temp = temp_file.name
            if tipo_arquivo == 'PDF':
                documento = carrega_pdf(path_temp)
            elif tipo_arquivo == 'CSV':
                documento = carrega_csv(path_temp)
            elif tipo_arquivo == 'TXT':
                documento = open(path_temp, 'r').read()

        else:
            st.warning(f'Tipo de arquivo não suportado: {tipo_arquivo}')
            return None

        return documento

    except Exception as e:
        st.exception(e)
        return None


def carrega_modelo(provedor, modelo, tipo_arquivo, arquivo, api_key=None):

    documento = carrega_arquivo(tipo_arquivo, arquivo)
    system_prompt = f'''
        Você é um assistente amigável chamado Oráculo.
        Você possui acesso às seguintes informações vindas 
        de um documento {tipo_arquivo}: 

        ####
        {documento}
        ####

        Utilize as informações fornecidas para basear as suas respostas.

        Sempre que houver $ na sua saída, substita por S.

        Se a informação do documento for algo como "Just a moment...Enable JavaScript and cookies to continue" 
        sugira ao usuário carregar novamente o Oráculo!'''

    template = ChatPromptTemplate.from_messages([
        ('system', system_prompt),
        ('placeholder', '{chat_history}'),
        ('user', '{input}')
    ])

    chat_class = config_modelos[provedor]['chat']
    
    if provedor == 'Ollama':
        chat = chat_class(model=modelo)
    else:
        chat = chat_class(model=modelo, api_key=api_key)
    
    chain = template | chat

    st.session_state['chain'] = chain
    st.session_state['modelo_nome'] = f"{provedor} - {modelo}"

def chat_main():

    st.header('Oráculo', divider=True)
    chain = st.session_state.get('chain')
    if chain == None:
        st.warning('Inicialize o Oráculo para começar')
        st.stop()

    memoria = st.session_state.get('memoria', ConversationBufferMemory())
    input_usuario = st.chat_input('Fale com o Oráculo...')
    
    if chain:
        with st.sidebar:
            modelo_nome = st.session_state.get('modelo_nome', 'Desconhecido')
            st.caption(f"🔮 Modelo atual: `{modelo_nome}`")
    
    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    if input_usuario:

        chat = st.chat_message('human')
        chat.markdown(input_usuario)

        chat = st.chat_message('ai')
        resposta = chat.write_stream(chain.stream({
            'input': input_usuario,
            'chat_history': memoria.buffer_as_messages
            }))

        memoria.chat_memory.add_ai_message(resposta)
        st.session_state['memoria'] = memoria


def sidebar():
    tabs = st.tabs(['Upload de arquivos', 'Seleção de modelo'])
    with tabs[0]:
        tipo_arquivo = st.selectbox('Selecione o tipo de arquivo', arquivos_validos)
    
        if tipo_arquivo == 'Site':
            arquivo = st.text_input('Digite a url do site')
        elif tipo_arquivo == 'YouTube':
            arquivo = st.text_input('Digite a url do vídeo')
        elif tipo_arquivo == "PDF":
            arquivo = st.file_uploader('Faça o upload do arquivo', type=['.pdf'])
        elif tipo_arquivo == "CSV":
            arquivo = st.file_uploader('Faça o upload do arquivo', type=['.csv'])
        elif tipo_arquivo == "TXT":
            arquivo = st.file_uploader('Faça o upload do arquivo', type=['.txt'])

    with tabs[1]:
        provedor = st.selectbox('Selecione o provedor', config_modelos.keys())
        modelo = st.selectbox('Selecione o modelo', config_modelos[provedor]['modelos'])

        if provedor != 'Ollama':
            api_key = st.text_input(
                f'Insira sua chave de API da {provedor}',
                type='password',
                value=st.session_state.get(f'api_key_{provedor}')
            )
            st.session_state[f'api_key_{provedor}'] = api_key
        else:
            api_key = None  # Não necessário

    if st.button('Iniciar Oráculo', use_container_width=True):
        if provedor != 'Ollama' and not api_key:
            st.warning('É necessário inserir uma chave de API.')
            return
        carrega_modelo(provedor, modelo, tipo_arquivo, arquivo, api_key)
    if st.button('Apagar histórico', use_container_width=True):
        st.session_state['memoria'] = ConversationBufferMemory()


def main():
    with st.sidebar:
        sidebar()
    chat_main()


if __name__ == '__main__':
    main()