# utils.configs.py

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

arquivos_validos = ['Site', 'YouTube', 'PDF', 'CSV', 'TXT']

config_modelos = {
    'Groq': {
        'modelos':['llama-3.3-70b-versatile', 'gemma2-9b-it', 'llama-3.1-8b-instant'],
        'chat': ChatGroq
    },
    'OpenAI': {
        'modelos': ['gpt-4o-mini', 'gpt-4o', 'o1-mini'],
        'chat': ChatOpenAI
    }
}
