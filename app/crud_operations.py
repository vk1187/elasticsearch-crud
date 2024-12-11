# from app.config import es
from elasticsearch import Elasticsearch

# Create Elasticsearch client
es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "my_index"

# Create Index
def create_index():
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME)
        return f"Index '{INDEX_NAME}' created successfully."
    return f"Index '{INDEX_NAME}' already exists."

# Create Document
def create_document(doc_id, document):
    es.index(index=INDEX_NAME, id=doc_id, document=document)
    return f"Document with ID {doc_id} created successfully."

# Read Document
def read_document(doc_id):
    if es.exists(index=INDEX_NAME, id=doc_id):
        return es.get(index=INDEX_NAME, id=doc_id)['_source']
    return f"Document with ID {doc_id} does not exist."

# Update Document
def update_document(doc_id, updated_fields):
    if es.exists(index=INDEX_NAME, id=doc_id):
        es.update(index=INDEX_NAME, id=doc_id, body={"doc": updated_fields})
        return f"Document with ID {doc_id} updated successfully."
    return f"Document with ID {doc_id} does not exist."

# Delete Document
def delete_document(doc_id):
    if es.exists(index=INDEX_NAME, id=doc_id):
        es.delete(index=INDEX_NAME, id=doc_id)
        return f"Document with ID {doc_id} deleted successfully."
    return f"Document with ID {doc_id} does not exist."
