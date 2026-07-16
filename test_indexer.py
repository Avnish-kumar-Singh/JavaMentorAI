from app.rag.indexer import DocumentIndexer

indexer = DocumentIndexer()

indexer.index_documents("data/uploads")

print()
print("All documents indexed successfully.")