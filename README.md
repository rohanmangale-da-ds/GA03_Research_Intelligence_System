
📩 Gmail - rohanmangale4001@gmail.com

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🤖 Research Intelligence RAG Chatbot

An AI-powered Research Assistant that allows users to upload documents and interact with them using Retrieval-Augmented Generation (RAG).

This system enables intelligent document understanding by combining semantic search, vector embeddings, and LLM-based reasoning — all inside a clean and interactive Streamlit interface.

## 📸 Screenshots
1. User Interface (UI)
<img width="1910" height="962" alt="image" src="https://github.com/user-attachments/assets/5b20fba0-fd19-413b-bb68-a1d3529061ca" />

2. Extracting Information from Documents
<img width="1912" height="959" alt="image" src="https://github.com/user-attachments/assets/89003453-f533-4de2-ac1c-e50c201685d3" />

3. AI-Powered Question Answering from Documents
<img width="1914" height="959" alt="image" src="https://github.com/user-attachments/assets/b64a1cc9-450e-46b9-9c98-0cded798c852" />


### ✨ Key Features

✔ Upload and analyze multiple documents (PDF / TXT)
✔ Ask natural language questions about uploaded documents
✔ Uses Retrieval-Augmented Generation (RAG)
✔ Fast semantic search using FAISS
✔ Clean and modern Streamlit UI
✔ Modular, scalable, and production-ready architecture
✔ Designed for research, legal, academic, and enterprise use cases


### 💡 Tech Stack

1. UI	-> Streamlit
2. LLM	-> Groq (LLaMA 3.x series)
3. Embeddings -> 	HuggingFace (Sentence Transformers)
4. Vector Database ->	FAISS
5. Backend ->	Python
6. Configuration ->	.env, settings.py
7. Architecture ->	Modular & Scalable

### 📁 Project Structure

```
GA03_Research_Intelligence_System/
│
├── .streamlit/
│   └── config.toml              # UI theme configuration
│
├── config/
│   ├── __init__.py
│   └── settings.py              # Centralized configuration
│
├── core/
│   ├── chain.py                 # RAG pipeline logic
│   ├── document_processor.py    # Document parsing & chunking
│   ├── embeddings.py            # Embedding generation
│   └── vector_store.py          # FAISS vector store
│
├── ui/
│   ├── chat_interface.py        # Chat UI logic
│   └── components.py            # Reusable UI components
│
├── data/
│   └── input_data/              # Uploaded documents
│
├── app.py                       # Streamlit entry point
├── main.py                      # CLI entry (optional)
├── requirements.txt
├── pyproject.toml
├── .env                         # Environment variables (ignored)
├── .gitignore
└── README.md
```

### ⚙️ How It Works (High Level)
1️⃣ Document Upload

Users upload PDF or TXT documents through the Streamlit interface.

2️⃣ Chunking & Embedding

Uploaded documents are:

Split into meaningful chunks

Converted into vector embeddings using Sentence Transformers

3️⃣ Vector Storage

All embeddings are stored in a FAISS vector database for efficient similarity search.

4️⃣ Query Processing

When a user asks a question:

Relevant document chunks are retrieved

Context is injected into the LLM prompt

A grounded, document-based response is generated

5️⃣ Response Generation

The system produces:

Accurate answers

Context-aware explanations

Source-backed responses

### 🚀 Ideal Use Cases

Academic research assistance

Legal document analysis

Technical documentation Q&A

Knowledge base exploration

Enterprise document intelligence

### 🛠️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/rohanmangale-da-ds/GA03_Research_Intelligence_System.git
cd GA03_Research_Intelligence_System

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here

5️⃣ Run the App
streamlit run app.py

### 🔒 Notes

.env is excluded from Git for security

API keys should never be committed

The app works fully offline after document ingestion
