
from core.embeddings import EmbeddingManager
from core.vector_store import VectorStoreManager
from core.document_processor import DocumentProcessor

file_path = r"input_data\CLARiTy A Vision Transformer for Multi-Label Classification.pdf"

# step 1. loading documents and creating chunks using DocumentProcessor
processor = DocumentProcessor()
chunks = processor.process(file_path)
print("--------- Document Processor Test ---------\n")
print(f"Loaded and processed {len(chunks)} document chunks.\n")
print(f"First chunk content:\n{chunks[0].page_content}\n\n"
      f"Metadata: {chunks[0].metadata}")

# step 2. create embeddings using EmbeddingManager
embedder = EmbeddingManager()
print("Embedding model loaded")
print(f"Model: {embedder.model_name}")
print(f"Dimension: {embedder.get_embedding_dimension()}")

# step 3. retrieve similar documents using VectorStoreManager
vector_store = VectorStoreManager(embedder)
vector_store.create_from_documents(chunks)
print(f"Vector store created with {len(chunks)} documents")
query = "What is clarity?"
retrieved_docs = vector_store.search(query, k=2)
print("--------- Vector Store Manager Test ---------\n")
print(f"Query: {query}\n")
for i, doc in enumerate(retrieved_docs, 1):
    print(f"Result {i}:\nContent: {doc.page_content[:100]}\nMetadata: {doc.metadata}\n")

# Step 4: Save vector store
print("\nStep 4: Saving vector store...")
vector_store.save()
print(f"Vector store saved to {vector_store.index_path}/")

# Step 5: Load and verify
print("\nStep 5: Loading saved vector store...")
vs_loader = VectorStoreManager(embedder)
vs_loader.load()
print("Vector store loaded successfully\n")
    
# Verify it works
test_result = vs_loader.search("what is clarity", k=1)
print("Query:", "what is clarity\n")
print(f"Verification search returned: \nPage content:{test_result[0].page_content[:100]}... \nMetadata:{test_result[0].metadata}")


# testing RAG chain
from core.chain import RAGChain
rag_chain = RAGChain(vector_store)
response = rag_chain.query("Explain the CLARiTy model in brief.", k=2)
print("\n--------- RAG Chain Test ---------\n")
print(f"Query: Explain the CLARiTy model in brief.\n")
print(f"Response Answer:\n{response["answer"]}\n\nSources:\n{response["sources"]}\n\nContext:\n{response["context"]}\n\n Documents:\n{response["documents"]}")
