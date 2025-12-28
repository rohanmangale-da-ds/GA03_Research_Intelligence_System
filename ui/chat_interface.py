import streamlit as st
from typing import Generator, Optional

from core.document_processor import DocumentProcessor
from core.vector_store import VectorStoreManager
from core.chain import RAGChain
from ui.components import save_uploaded_file


class ChatInterface:
    """
    Main chat interface orchestrator.

    Handles:
    - Document ingestion
    - Vector search
    - RAG-based question answering
    """

    def __init__(self):
        self.doc_processor = DocumentProcessor()
        self.vector_store = VectorStoreManager()
        self.rag_chain: Optional[RAGChain] = None

    def process_uploaded_files(self, uploaded_files) -> int:
        """
        Process uploaded files and add them to the vector store.

        Args:
            uploaded_files: List of uploaded documents

        Returns:
            Number of processed chunks
        """
        all_chunks = []

        for uploaded_file in uploaded_files:
            file_path = save_uploaded_file(uploaded_file)

            chunks = self.doc_processor.process(file_path)

            # Add metadata
            for chunk in chunks:
                chunk.metadata["source"] = uploaded_file.name

            all_chunks.extend(chunks)

            if uploaded_file.name not in st.session_state.uploaded_files:
                st.session_state.uploaded_files.append(uploaded_file.name)

        if all_chunks:
            self.vector_store.add_documents(all_chunks)
            st.session_state.vector_store_initialized = True

        return len(all_chunks)

    def initialize_rag_chain(self):
        """Initialize RAG chain after documents are indexed."""
        if self.vector_store.is_initialized:
            self.rag_chain = RAGChain(self.vector_store)

    def get_response(self, query: str) -> Generator[str, None, None]:
        """
        Generate streaming response from document knowledge base.
        """
        if self.rag_chain is None and self.vector_store.is_initialized:
            self.initialize_rag_chain()

        if not self.rag_chain:
            yield "⚠️ Please upload documents first."
            return

        for chunk in self.rag_chain.query_stream(query):
            yield chunk

    def get_sources(self, query: str) -> list:
        """
        Retrieve source documents for the given query.
        """
        if not self.vector_store.is_initialized:
            return []

        docs = self.vector_store.search(query)
        return list(set(doc.metadata.get("source", "Unknown") for doc in docs))
