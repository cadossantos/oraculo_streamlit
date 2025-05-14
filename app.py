import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils.configs import *


def carrega_modelo (provedor, modelo, api_key):
    chat = config_modelos[provedor]['chat'](model=modelo, api_key=api_key)
    st.session_state['chat'] = chat


def chat_main():
    st.header('Oráculo', divider=True)
    chat_model = st.session_state.get('chat')
    memoria = st.session_state.get('memoria', ConversationBufferMemory())
    input_usuario = st.chat_input('Fale com o Oráculo...')
    
    if chat_model:
        with st.sidebar:
            st.caption(f"🔮 Modelo atual: `{chat_model.model_name}`")
    
    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    if input_usuario:
        if not chat_model:
            st.error("Você precisa iniciar o Oráculo primeiro na barra lateral.")
            return
        
        chat = st.chat_message('human')
        chat.markdown(input_usuario)

        chat = st.chat_message('ai')
        resposta = chat.write_stream(chat_model.stream(input_usuario))

        memoria.chat_memory.add_ai_message(resposta)
        st.session_state['memoria'] = memoria


def sidebar():
    tabs = st.tabs(['Upload de arquivos', 'Seleção de modelo'])
    with tabs[0]:
        tipo_arquivo = st.selectbox('Selecione o tipo de arquivo', arquivos_validos)
    
        if tipo_arquivo == 'Site':
            arquivo = st.text_input('Digite a url do site')
        if tipo_arquivo == 'YouTube':
            arquivo = st.text_input('Digite a url do vídeo')
        if tipo_arquivo == "PDF":
            arquivo = st.file_uploader('Faça o upload do arquivo', type=['.pdf'])
        if tipo_arquivo == "CSV":
            arquivo = st.file_uploader('Faça o upload do arquivo', type=['.csv'])
        if tipo_arquivo == "TXT":
            arquivo = st.file_uploader('Faça o upload do arquivo', type=['.txt'])

    with tabs[1]:
        provedor = st.selectbox('Selecione o provedor', config_modelos.keys())
        modelo = st.selectbox('Selecione o modelo', config_modelos[provedor]['modelos'])
        api_key = st.text_input(
            f'Insira sua chave de API da {provedor}',
            type='password',
            value=st.session_state.get(f'api_key_{provedor}')
        )
        st.session_state[f'api_key_{provedor}'] = api_key
        

        if st.button('Iniciar Oráculo', use_container_width=True):
            if not api_key:
                st.error('É necessário inserir uma chave de API.')
                return
            carrega_modelo(provedor, modelo, api_key)


def main():
    chat_main()
    with st.sidebar:
        sidebar()

if __name__ == '__main__':
    main()