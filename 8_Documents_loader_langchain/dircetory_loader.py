from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(path= "8_Documents_loader_langchain/books",
                         glob='*.pdf',
                         loader_cls=PyPDFLoader)

all_books = loader.load()

print("length of the two books in total \n",len(all_books))
print("*" * 100)
print("Metadata on the page number 200  \n",all_books[200].metadata)
print("*" * 100)
print(  "Page content on page number 200 \n", all_books[200].page_content)
print("*" * 100)
print(type(all_books))
