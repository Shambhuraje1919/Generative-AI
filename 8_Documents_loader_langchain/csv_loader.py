
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('8_Documents_loader_langchain\Social_Network_Ads.csv')

csv_file = loader.load()
print('len rows of csv file /n',len(csv_file))
print("type of this file /n " , type(csv_file))
print(csv_file[0].metadata)
print(csv_file[0].page_content)