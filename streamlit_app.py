import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="GitHub MCP Assistant",
    layout="wide"
)

st.title("🚀 MCP GitHub Repository Assistant")

st.markdown(
    "AI-powered GitHub repository intelligence system"
)

# -----------------------------
# Repository Search
# -----------------------------

st.header("🔍 Search GitHub Repositories")

query = st.text_input(
    "Enter repository topic",
    placeholder="langchain"
)

if st.button("Search Repositories"):

    response = requests.get(
        f"{BACKEND_URL}/search",
        params={"query": query}
    )

    data = response.json()

    if "items" in data:

        for repo in data["items"][:10]:

            st.subheader(repo["full_name"])

            st.write(repo["description"])

            st.write(f"⭐ Stars: {repo['stargazers_count']}")

            st.write(repo["html_url"])

            st.divider()

# -----------------------------
# Repository Summarization
# -----------------------------

st.header("🧠 Repository Summarization")

owner = st.text_input(
    "Repository Owner",
    placeholder="langchain-ai"
)

repo = st.text_input(
    "Repository Name",
    placeholder="langchain"
)

if st.button("Generate Summary"):

    response = requests.get(
        f"{BACKEND_URL}/summarize",
        params={
            "owner": owner,
            "repo": repo
        }
    )

    data = response.json()

    st.subheader("AI Summary")

    st.write(data["summary"])

# -----------------------------
# Semantic Search
# -----------------------------

st.header("📚 Semantic Repository Search")

semantic_query = st.text_input(
    "Ask semantically",
    placeholder="framework for building LLM apps"
)

if st.button("Semantic Search"):

    response = requests.get(
        f"{BACKEND_URL}/semantic-search",
        params={"query": semantic_query}
    )

    results = response.json()

    st.write(results)