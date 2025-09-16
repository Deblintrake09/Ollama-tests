from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

doc_path = "./data/BOI.pdf"
model = "llama3.2"

#Load a local PDF file
if doc_path:
    loader = UnstructuredPDFLoader(file_path=doc_path)
    data = loader.load()
    print(f"Loaded {len(data)} pages from {doc_path}")
else:
    print("Upload a PDF file to process")

#Preview first page content
content = data[0].page_content
print(content[:100])  # Print the first 100 characters of the first page

#===== End of PDF Injection =====#

#==== Extract text from PDF and Split into chunks ====#
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma


# Split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
chunks = text_splitter.split_documents(data)
print(f"Done splitting... Split into {len(chunks)} chunks")

print("number of chunks:", len(chunks))
print("content of first chunk:", chunks[0])