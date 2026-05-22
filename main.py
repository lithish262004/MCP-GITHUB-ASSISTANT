from fastapi import FastAPI
from app.embeddings import create_embedding
from app.chroma_store import (
    add_repository,
    search_repository
)

from app.github_tools import (
    search_repositories,
    get_repository,
    get_readme,
    get_issues,
    decode_readme_content
)

from app.summarizer import summarize_text

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "MCP GitHub Assistant Running"
    }


@app.get("/search")
def search(query: str):

    return search_repositories(query)


@app.get("/repo")
def repo(owner: str, repo: str):

    return get_repository(owner, repo)


@app.get("/readme")
def readme(owner: str, repo: str):

    return get_readme(owner, repo)


@app.get("/issues")
def issues(owner: str, repo: str):

    return get_issues(owner, repo)


@app.get("/summarize")
def summarize(owner: str, repo: str):

    readme_data = get_readme(owner, repo)

    decoded_text = decode_readme_content(readme_data)

    summary = summarize_text(decoded_text)

    return {
        "repository": repo,
        "summary": summary
    }

@app.get("/index")

def index_repo(owner: str, repo: str):

    # Fetch README from GitHub
    readme_data = get_readme(owner, repo)

    # Decode Base64 README content
    decoded_text = decode_readme_content(readme_data)

    # Create embedding vector
    embedding = create_embedding(decoded_text)

    # Store in ChromaDB
    add_repository(
        repo_name=repo,
        content=decoded_text,
        embedding=embedding
    )

    return {
        "message": f"{repo} indexed successfully"
    }

@app.get("/semantic-search")

def semantic_search(query: str):

    # Convert query into embedding
    query_embedding = create_embedding(query)

    # Search ChromaDB
    results = search_repository(query_embedding)

    return results
