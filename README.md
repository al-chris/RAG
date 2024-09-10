# README: Simple RAG (Retrieval-Augmented Generation) Project

## Overview

This project implements a basic Retrieval-Augmented Generation (RAG) pipeline. The system processes a PDF file, splits it into text chunks, stores these chunks in a vector store using FAISS, and provides a retriever for efficient information retrieval from the stored chunks. The retriever is then used to answer user queries by fetching relevant information from the PDF chunks.

## Features

- **PDF to Text Chunk Conversion:** Takes in a PDF and splits it into smaller text chunks for better information retrieval.
- **Vector Store Integration:** Stores the text chunks in a FAISS-based vector store for fast similarity searches.
- **Retriever Creation:** A retriever is set up to find the most relevant chunks of text from the stored data.
- **Integration with Language Models:** The retriever can be combined with models from LangChain or other model providers to generate more context-aware responses.

## Prerequisites

Ensure you have Python 3.7+ installed on your machine. The required libraries are listed in the `requirements.txt` file.

### Required Libraries

- `langchain`
- `langchain-community`
- `pypdf`
- `faiss-cpu` or `faiss-gpu` (depending on your hardware)
- `langchain-ollama`
- `langchain-google-genai`
- `python-dotenv`

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

### FAISS Installation

You can install either the CPU or GPU version of FAISS depending on your environment:

- **CPU Version:**
    ```bash
    pip install faiss-cpu
    ```

- **GPU Version (requires CUDA):**
    ```bash
    pip install faiss-gpu
    ```

## Project Structure

The main components of the project are structured as follows:

```
├── rag.ipynb                  # Main application file
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables (e.g., API keys)
├── sample.pdf                 # the pdf file
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies:**

    Ensure all required libraries are installed by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory to store API keys or other sensitive information, especially if you are using external APIs or models.

   Example `.env` file:

   ```bash
   GEMINI_API_KEY=your_google_genai_api_key
   ```

4. **Run the application:**

   You can run the application using jupyter nootbook

## How It Works

1. **PDF Processing:**
   The project uses `pypdf` to extract text from a provided PDF file.
   
2. **Text Splitting:**
   The text is split into smaller chunks to facilitate efficient retrieval. This is typically done using `langchain`'s text splitting utilities.

3. **Vector Store:**
   The text chunks are embedded into vector representations and stored in a FAISS-based vector store for fast retrieval.

4. **Retriever:**
   A retriever is created using the FAISS vector store. It allows the system to find and retrieve the most relevant text chunks based on similarity to a query.

5. **Query Handling:**
   The retriever is queried using user input, and the most relevant chunks are fetched. Optionally, these chunks can be further processed using external language models (e.g., using `langchain-ollama` or `langchain-google-genai`).

## Example Usage

1. **Load a PDF File:**

   The app will prompt you to load a PDF file. The text from the PDF will be automatically extracted and processed into smaller chunks.

2. **Store the Chunks:**

   The extracted text chunks are then embedded and stored in a FAISS vector store.

3. **Query the PDF:**

   You can input any query, and the retriever will find the most relevant text chunks from the stored data. If you have connected a language model, the system can also generate answers based on the retrieved chunks.

## Customization

You can modify the following to suit your specific needs:

- **Chunking Strategy:** Customize how the PDF text is split into chunks. LangChain provides several chunking strategies (e.g., by paragraph, sentence, or fixed length).
  
- **Language Models:** Modify the models used for RAG by changing the integrations for `langchain-ollama`, `langchain-google-genai`, or other providers.

## Troubleshooting

- **FAISS Setup Issues:**
   Ensure that you have installed the correct version of FAISS (CPU or GPU) based on your system's capabilities.

- **Missing Dependencies:**
   Double-check that all the necessary dependencies are installed via `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

---

Feel free to extend or modify this project to suit more complex requirements such as handling multiple documents, integrating with more advanced models, or enhancing the retrieval logic.

---

