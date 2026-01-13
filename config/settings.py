from dataclasses import dataclass
import os
from dotenv import load_dotenv
from typing import Optional


# Load environment variables from .env file (for local development)
load_dotenv()


@dataclass
class Settings:
    """
    Centralized configuration settings for the RAG application.
    
    All API keys and configuration values are loaded from environment variables
    for security. Never hardcode API keys in your code!
    
    Supports multiple deployment scenarios:
    - Local: .env file or .streamlit/secrets.toml
    - Streamlit Cloud: Dashboard secrets
    - Docker/Other: Environment variables
    """
    GROQ_API_KEY:str = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY:str = os.getenv("TAVILY_API_KEY")
    LLM_MODEL:str = os.getenv("LLM_MODEL")
    LLM_TEMPERATURE:float =  float(os.getenv("LLM_TEMPERATURE", 0))
    EMBEDDING_MODEL:str = os.getenv("EMBEDDING_MODEL")
    CHUNK_SIZE:int = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP:int = int(os.getenv("CHUNK_OVERLAP", 200))
    FAISS_INDEX_PATH:str = os.getenv("FAISS_INDEX_PATH")
    TOP_K_RESULTS:int = int(os.getenv("TOP_K_RESULTS", 3))


    def validate(self) -> bool:
        if not self.GROQ_API_KEY:
            raise ValueError("❌ GROQ_API_KEY not set")

        if not self.TAVILY_API_KEY:
            raise ValueError("❌ TAVILY_API_KEY not set")

        return True



# Singleton instance for easy import
settings = Settings()
