from underthesea import text_normalize
from langchain_community.document_loaders import PyPDFLoader

def normalize(text):
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\t", " ")
    text = text_normalize(text)

    return text

def read_pdf(file_location):
     loader = PyPDFLoader(file_location)
     text = ''
     for doc in loader.lazy_load():
          text += normalize(doc.page_content)
     
     return text