from langchain_community.document_loaders.base_o365 import CHUNK_SIZE
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("9_text_spliters/dl-curriculum.pdf")
pdf = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap =0,
    separator=''
)
pdf_spliter = splitter.split_documents(pdf)

print(pdf_spliter[0].page_content)

