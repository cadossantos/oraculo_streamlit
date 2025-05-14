import streamlit as st


arquivos_validos = ['Site', 'YouTube', 'PDF', 'CSV', 'TXT']

config_modelos = {
    'Groq': {
        'modelos':['llama-3.1-70b-versatile', 'gemma2-9b-it', 'mixtral-8x7b-32768'],
        # 'api_key':''
    },
    'OpenAI': {
        'modelos': ['gpt-4o-mini', 'gpt-4o', 'o1-mini']
    }
}
mensagens_exemplo = [
    ('user', 'oi'),
    ('assistant', 'Opa, beleza?'),
    ('user', 'Tudo ótimo'),
]

def chat_main():
    st.header('Oráculo', divider=True)

    mensagens = st.session_state.get('mensagens', mensagens_exemplo)
    for role, mensagem in mensagens:
        with st.chat_message(role):
            st.markdown(mensagem)

    input_usuario = st.chat_input('Fale com o Oráculo...')
    if input_usuario:
        mensagens.append(('user', input_usuario))
        st.session_state['mensagens'] = mensagens
        st.rerun()

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


def main():
    chat_main()
    with st.sidebar:
        sidebar()

if __name__ == '__main__':
    main()