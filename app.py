import streamlit as st

# Import configuration and validate settings
from config.settings import settings

# Validate API keys before app starts
try:
    settings.validate()
except ValueError as e:
    st.error(f"⚠️ Configuration Error:\n\n{str(e)}")
    st.stop()

# Import UI components
from ui.components import (
    init_session_state,
    display_chat_history,
    add_message,
    display_sidebar_info,
    display_file_uploader,
    display_processing_status,
)
from ui.chat_interface import ChatInterface


# Page configuration
st.set_page_config(
    page_title="AI Advocate RAG Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Custom CSS for better appearance
st.markdown("""
<style>
/* Make the app use full width */
.main .block-container {
    max-width: 100%;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Optional: reduce top padding */
.css-18e3th9 {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)


def main():
    """Main application entry point."""

    # Initialize session state
    init_session_state()

    # Initialize chat interface
    if "chat_interface" not in st.session_state:
        st.session_state.chat_interface = ChatInterface()

    chat = st.session_state.chat_interface

    # Sidebar
    display_sidebar_info()

    # Title
    st.title("🤖 AI Advocate RAG Chatbot", text_alignment="center")
    st.markdown("Ask questions about your uploaded documents.")

    # File upload section
    with st.expander("📤 Upload Documents", expanded=not st.session_state.vector_store_initialized):
        uploaded_files = display_file_uploader()

        if uploaded_files:
            if st.button("🚀 Process Documents", type="secondary"):
                with st.spinner("Processing documents..."):
                    try:
                        num_chunks = chat.process_uploaded_files(uploaded_files)
                        display_processing_status(
                            f"✅ Processed {len(uploaded_files)} file(s) into {num_chunks} chunks!",
                            "success"
                        )
                    except Exception as e:
                        display_processing_status(f"❌ Error: {str(e)}", "error")

    st.divider()

    # Chat history
    display_chat_history()

    # Chat input
    st.markdown("""
    <style>
    div[data-testid="stChatInput"] {
        max-width: 800px;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)

    if prompt := st.chat_input("Ask a question about your documents..."):
        add_message("user", prompt)

        with st.chat_message("assistant"):
            try:
                response = st.write_stream(
                    chat.get_response(prompt)
                )

                sources = chat.get_sources(prompt)

                if sources:
                    with st.expander("📚 Sources"):
                        for source in sources:
                            st.write(f"- {source}")

                add_message("assistant", response, sources)

            except Exception as e:
                error_msg = f"❌ Error generating response: {str(e)}"
                st.error(error_msg)
                add_message("assistant", error_msg)


if __name__ == "__main__":
    main()
