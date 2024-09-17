import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.agents import Tool, AgentExecutor, initialize_agent, AgentType
from dotenv import load_dotenv

load_dotenv()

# Set up environment variables
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Load and ingest data
loader = PyPDFDirectoryLoader('climate_docs')
documents = loader.load()

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# Create embeddings and build vector store
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=os.getenv("GEMINI_API_KEY"))
vectorstore = FAISS.from_documents(texts, embeddings)

# Set up the language model
llm = GoogleGenerativeAI(
    model='gemini-pro',  # Updated to use Gemini Pro
    temperature=0.7,
    max_output_tokens=512
)

# Create a RetrievalQA chain
qa_chain = RetrievalQA.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

# Define tools for the agent
tools = [
    Tool(
        name='Climate QA System',
        func=qa_chain.run,
        description='Answers questions about climate change using retrieved documents.'
    )
]

# Initialize the agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Test the application
def main():
    print("Welcome to the Climate Change Assistant! Ask any question or type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == 'exit':
            print("Goodbye!")
            break

        response = agent.run(query)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()