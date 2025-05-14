import streamlit as st


mensagens_exemplo = [
    ('user', 'oi'),
    ('assistant', 'Opa, beleza?'),
    ('user', 'Tudo ótimo'),
]

def chat_main():
    st.header('Oráculo', divider=True)

    mensagens = st.session_state.get('mensagens', mensagens_exemplo)
    for mensagem in mensagens:
        chat = st.chat_message(mensagem[0])
        chat.markdown(mensagem[1])

    input_usuario = st.chat_input('Fale com o Oráculo...')
    if input_usuario:
        mensagens.append(('user', input_usuario))
        st.session_state['mensagens'] = mensagens
        st.rerun()

def main():
    chat_main()

if __name__ == '__main__':
    main()