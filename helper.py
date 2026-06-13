from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_core.documents import Document
import re
def load_pdf_files(Data):
    loader = DirectoryLoader(
        Data,
        glob="*.pdf",
        loader_cls=PyMuPDFLoader 
    )
    return loader.load()



def clean_text(text):
    text = re.sub(r"GALE ENCYCLOPEDIA.*", "", text)
    text = re.sub(r"GEM - \d+.*", "", text)
    text = re.sub(r"Page \d+", "", text)
    text = re.sub(r"\n+", " ", text)
    return text.strip()


def is_good_page(text):
    bad_keywords = [
        "copyright",
        "contents",
        "advisory board",
        "introduction",
        "contributors"
    ]

    text_lower = text.lower()

    if len(text) < 200:
        return False

    if any(word in text_lower for word in bad_keywords):
        return False

    return True


def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs = []

    for doc in docs:
        cleaned = clean_text(doc.page_content)

        if not is_good_page(cleaned):
            continue

        minimal_docs.append(
            Document(
                page_content=cleaned,
                metadata=doc.metadata
            )
        )

    return minimal_docs

def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap= 20,

    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk






from langchain_community.embeddings import HuggingFaceEmbeddings
def download_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings