from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('8_Documents_loader_langchain/Programming PyTorch for Deep Learning (2020).pdf')

book = loader.load()

print(book[100].page_content)
print(book[100].metadata)
print(len(book))

