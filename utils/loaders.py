# utils/loaders.py

import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities.requests import RequestsWrapper
from langchain_community.document_loaders import (
    WebBaseLoader,
    YoutubeLoader,
    CSVLoader,
    PyPDFLoader,
    TextLoader
)


def carrega_site(url):
    user_agent = os.getenv("USER_AGENT", "Mozilla/5.0")  # fallback
    wrapper = RequestsWrapper(headers={"User-Agent": user_agent})
    loader = WebBaseLoader(url)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento


def carrega_youtube(url):
    user_agent = os.getenv("USER_AGENT", "Mozilla/5.0")  # fallback
    wrapper = RequestsWrapper(headers={"User-Agent": user_agent})
    loader = YoutubeLoader.from_youtube_url(
        url,
        add_video_info=False,
        language=['pt']
        )
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento


def carrega_pdf(caminho_pdf):
    loader = PyPDFLoader(caminho_pdf)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento


def carrega_csv(caminho_csv):
    loader = CSVLoader(caminho_csv)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento


def carrega_txt(caminho_txt):
    loader = TextLoader(caminho_txt)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento
