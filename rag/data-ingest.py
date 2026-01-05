import os
import glob
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter



MODEL = "gpt-4.1-nano"
db_name = "vector_db"
PATH = "knowledge-base/*"
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")



def read_documents(path):
    # Load in everything in the knowledgebase using LangChain's loaders
    folders = glob.glob(path)

    documents = []
    for folder in folders:
        doc_type = os.path.basename(folder)
        loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
        folder_docs = loader.load()
        for doc in folder_docs:
            doc.metadata["doc_type"] = doc_type
            documents.append(doc)

    print(f"Loaded {len(documents)} documents")
    return documents

def split_documents(documents):
    # Divide documentsinto chunks using the LangChain's RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

    print(f"Divided into {len(chunks)} chunks")
    return chunks

def create_embeddings(chunks):
    # create embeddings and persist the vector store
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    #embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    if os.path.exists(db_name):
        Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()

    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=db_name)
    print(f"Vectorstore created with {vectorstore._collection.count()} documents")



if __name__ == "__main__":
    print("Ingestion started")
    documents = read_documents(PATH)
    chunks = split_documents(documents)
    create_embeddings(chunks)
    print("Ingestion complete")