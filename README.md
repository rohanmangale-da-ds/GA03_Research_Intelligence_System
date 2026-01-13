
📩 Gmail - rohanmangale4001@gmail.com

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🤖 Research Intelligence RAG Chatbot

An AI-powered Research Intelligence System that allows users to upload documents and interact with them using Retrieval-Augmented Generation (RAG) — enhanced with optional real-time web search via Tavily.

The system intelligently combines local document knowledge with fresh web information to deliver accurate, contextual, and well-reasoned answers through a clean Streamlit chat interface.

## 📸 Screenshots
1. User Interface (UI)
<img width="1897" height="914" alt="image" src="https://github.com/user-attachments/assets/cf234560-5c57-4ec7-ade2-7f0fec098c44" />

2. Extracting Information from Documents
<img width="1898" height="927" alt="image" src="https://github.com/user-attachments/assets/53b57b20-efbd-42cb-b435-9153b7505498" />

3. Hybrid RAG: Documents + Web Search (Wikipedia & Web Sources)
<img width="1897" height="919" alt="image" src="https://github.com/user-attachments/assets/4e2bd933-9a3c-4512-b369-b7866e5349c8" />



### ✨ Key Features

✔ Upload and analyze multiple documents (PDF / TXT)
✔ Ask natural-language questions over uploaded documents
✔ Hybrid RAG: Document search + optional Tavily web search
✔ Fast semantic retrieval using FAISS
✔ Real-time web augmentation (Wikipedia & trusted sources)
✔ Streaming, ChatGPT-like responses
✔ Clean, modern Streamlit UI
✔ Modular, scalable, production-style architecture
✔ Suitable for research, legal, academic, and enterprise use cases


### 💡 Tech Stack

1. UI	-> Streamlit
2. LLM	-> Groq (LLaMA 3.x series)
3. Embeddings -> 	HuggingFace (Sentence Transformers)
4. Vector Database ->	FAISS
5. Backend ->	Python
6. Configuration ->	.env, settings.py
7. Architecture ->	Modular & Scalable
8. Web Search -> Tavily API

### 📁 Project Structure

```
GA03_Research_Intelligence_System/
│
├── .streamlit/
│   └── config.toml              # UI theme configuration
│
├── config/
│   ├── __init__.py
│   └── settings.py              # Centralized configuration & secrets
│
├── core/
│   ├── chain.py                 # RAG pipeline logic
│   ├── document_processor.py    # PDF/TXT parsing & chunking
│   ├── embeddings.py            # Embedding generation
│   └── vector_store.py          # FAISS vector store manager
│
├── tools/
│   └── tavily_search.py         # Tavily web search integration
│
├── ui/
│   ├── chat_interface.py        # Chat orchestration logic
│   └── components.py            # Reusable Streamlit components
│
├── data/
│   └── input_data/              # Uploaded documents
│
├── app.py                       # Streamlit entry point
├── main.py                      # Optional CLI entry
├── requirements.txt
├── pyproject.toml
├── .env                         # Environment variables (ignored)
├── .gitignore
└── README.md

```

### ⚙️ How It Works (High-Level)
1️⃣ Document Upload

Users upload PDF or TXT documents through the Streamlit UI.

2️⃣ Chunking & Embedding

Uploaded documents are:

Split into semantically meaningful chunks

Converted into vector embeddings using Sentence Transformers

3️⃣ Vector Storage

All embeddings are stored in a FAISS vector database for fast similarity search.

4️⃣ Hybrid Query Processing

When a user asks a question:

Relevant document chunks are retrieved from FAISS

Optional web search (Tavily) fetches fresh external knowledge

Both contexts are merged intelligently

5️⃣ Response Generation

The LLM generates:

Accurate, grounded answers

Context-aware explanations

Source-backed responses (documents + web)

🚀 Ideal Use Cases

Academic research assistance

Legal & policy document analysis

Technical documentation Q&A

Knowledge base exploration

Enterprise research intelligence tools

### 🛠️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/rohanmangale-da-ds/GA03_Research_Intelligence_System.git
cd GA03_Research_Intelligence_System

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

5️⃣ Run the App
streamlit run app.py


### 🔒 Notes

.env is excluded from Git for security

API keys should never be committed

FAISS index is generated dynamically

The app works offline after document ingestion

Web search can be enabled or disabled per query

### 🌟 Project Highlights 

Demonstrates RAG + Hybrid Search

Clean separation of concerns

Real-world AI system design

Production-style configuration handling

ChatGPT-like UX with streaming responses
