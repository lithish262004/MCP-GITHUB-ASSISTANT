import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="github_repos"
)

def add_repository(repo_name, content, embedding):

    collection.add(
        documents=[content],
        embeddings=[embedding],
        ids=[repo_name]
    )

def search_repository(query_embedding):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results