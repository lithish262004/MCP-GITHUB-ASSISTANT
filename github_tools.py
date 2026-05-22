import requests
import os
from dotenv import load_dotenv
import base64
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def search_repositories(query):

    url = f"https://api.github.com/search/repositories?q={query}"

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()


def get_repository(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()


def get_readme(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()


def get_issues(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/issues"

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()

def decode_readme_content(readme_data):

    if "content" not in readme_data:
        return "README not found"

    encoded_content = readme_data["content"]

    decoded_bytes = base64.b64decode(encoded_content)

    decoded_text = decoded_bytes.decode("utf-8")

    return decoded_text