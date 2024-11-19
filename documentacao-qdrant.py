import os
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

from dotenv import load_dotenv
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = QdrantClient(url=QDRANT_URL)

client.create_collection(
    collection_name="collection-name",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
)

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
embeddings = OpenAIEmbeddings()

vectorstore = Qdrant(
    client=client,
    collection_name="collection-name",
    embeddings=embeddings
)

def get_chunks(text):
    text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
    )
    chunks = text_splitter.split(text)
    return chunks
#substituir pelo texto do arquivo
with open("./base_dados.txt") as f:
    raw_text = f.read()

texts = get_chunks(raw_text)
  
vectorstore.add_texts(texts)

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

query = "Sua pergunta aqui"
response = qa.run(query)

print(response)

