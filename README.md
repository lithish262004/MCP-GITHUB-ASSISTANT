# MCP GitHub Repository Assistant

An AI-powered GitHub repository intelligence system built using **FastAPI, Streamlit, ChromaDB, and Sentence Transformers**.
The application enables intelligent GitHub repository analysis through repository search, AI-generated summaries, semantic search, and vector-based retrieval workflows.

---

# Features

## GitHub Repository Search

Search repositories dynamically using the GitHub API.

Displays:

* Repository Name
* Description
* Stars
* Repository URL

---

## AI Repository Summarization

Generate intelligent summaries from repository README files.

Features:

* README extraction
* Base64 decoding
* AI-based summarization
* Context-aware repository understanding

---

## Semantic Repository Search

Perform semantic search using embeddings and ChromaDB.

Unlike traditional keyword matching, the system understands:

* meaning
* context
* semantic similarity

Example:

```text
framework for building AI agents
```

returns repositories like:

```text
LangChain
```

even without exact keyword matches.

---

# System Architecture

```text
                    ┌────────────────────┐
                    │    Streamlit UI    │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   FastAPI Backend  │
                    └─────────┬──────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
 ┌──────────────┐    ┌────────────────┐    ┌──────────────┐
 │ GitHub API   │    │ Embedding Model│    │ ChromaDB     │
 └──────────────┘    └────────────────┘    └──────────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Semantic Retrieval │
                    └────────────────────┘
```

---

#  Tech Stack

## Backend

* FastAPI
* Python

## Frontend

* Streamlit

## AI & NLP

* Sentence Transformers
* Embedding Models

## Vector Database

* ChromaDB

## APIs

* GitHub REST API

---

#  Project Structure

```text
github-assistant/
│
├── app/
│   ├── main.py
│   ├── github_tools.py
│   ├── embeddings.py
│   ├── chroma_store.py
│   ├── summarizer.py
│   └── mcp_server.py
│
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

## 1️ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/github-assistant.git

cd github-assistant
```

---

# 2️ Create Virtual Environment

## Windows

```bash
python -m venv venv

venv\Scripts\activate
```

## Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Environment Variables

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token
```

Generate token from:

```text
https://github.com/settings/tokens
```

Required permissions:

* repo
* read:user

---

# Running the Application

# Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

# Start Streamlit Frontend

Open another terminal:

```bash
streamlit run streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

#  Application Workflow

# 1️ Search Repository

Enter:

```text
langchain
```

The app retrieves repositories from GitHub.

---

# 2️ Generate Repository Summary

Example:

Owner:

```text
langchain-ai
```

Repository:

```text
langchain
```

The system:

* fetches README
* decodes content
* generates summary
* creates embeddings
* stores vectors in ChromaDB

---

# 3️ Perform Semantic Search

Example query:

```text
framework for AI agents
```

The system:

* converts query into embeddings
* searches ChromaDB
* retrieves semantically related repositories

---

#  Why Semantic Search?

Traditional search:

```text
keyword matching
```

Semantic search:

```text
understanding meaning and intent
```

This enables:

* intelligent retrieval
* contextual understanding
* AI-powered search workflows

---

#  Example Use Cases

* AI repository analysis
* Developer productivity tools
* Semantic codebase search
* Intelligent GitHub exploration
* AI engineering assistants

---

#  Key Highlights

✅ GitHub API integration
✅ AI summarization
✅ Semantic vector search
✅ ChromaDB integration
✅ Streamlit frontend
✅ FastAPI backend
✅ Embedding-based retrieval

---
