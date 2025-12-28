import streamlit as st
from typing import List
import tempfile
import os


def init_session_state():
    """Initialize Streamlit session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "vector_store_initialized" not in st.session_state:
        st.session_state.vector_store_initialized = False

    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = []


def display_chat_history():
    """Display all chat messages."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message.get("sources"):
                with st.expander("📚 Sources"):
                    for source in message["sources"]:
                        st.write(f"- {source}")


def add_message(role: str, content: str, sources: List[str] = None):
    """
    Add a message to chat history.

    Args:
        role: 'user' or 'assistant'
        content: Message content
        sources: Optional list of source filenames
    """
    message = {"role": role, "content": content}
    if sources:
        message["sources"] = sources

    st.session_state.messages.append(message)


def clear_chat_history():
    """Clear all chat messages."""

    st.session_state.messages = []


def save_uploaded_file(uploaded_file) -> str:
    """
    Save uploaded file temporarily and return its path.
    """
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


def display_sidebar_info():
    """Sidebar layout and information."""
    with st.sidebar:
        st.header("📖 About")

        st.markdown("""
        This is an **AI Document RAG Chatbot** that can:

        - 📄 Answer questions from your uploaded documents  
        - 💬 Provide contextual and accurate responses  

        **How to use:**
        1. Upload PDF or TXT files  
        2. Wait for processing  
        3. Ask questions  
        """)

        st.divider()

        st.header("📁 Uploaded Files")
        if st.session_state.uploaded_files:
            for file in st.session_state.uploaded_files:
                st.write(f"✅ {file}")
        else:
            st.write("No files uploaded yet")

        st.divider()
        # Clear chat button
        st.markdown("""
        <style>
        button:hover span {
            color: red !important;
        }
        </style>
        """, unsafe_allow_html=True)
        if st.button("🗑️ Clear Chat History"):
            clear_chat_history()
            st.rerun()


def display_file_uploader():
    """Render file uploader."""
    return st.file_uploader(
        "Upload your documents (PDF or TXT)",
        type=["pdf", "txt"],
        accept_multiple_files=True,
        help="Upload documents to chat with"
    )


def display_processing_status(message: str, status: str = "info"):
    """Show processing feedback."""
    if status == "success":
        st.success(message)
    elif status == "warning":
        st.warning(message)
    elif status == "error":
        st.error(message)
    else:
        st.info(message)
