from mcp.server.fastmcp import FastMCP

from app.github_tools import (
    search_repositories,
    get_repository,
    get_issues
)

mcp = FastMCP(
    "GitHub Repository Assistant"
)

@mcp.tool()
def search_repo(query: str):

    return search_repositories(query)

@mcp.tool()
def get_repo(owner: str, repo: str):

    return get_repository(owner, repo)

@mcp.tool()
def get_repo_issues(owner: str, repo: str):

    return get_issues(owner, repo)

if __name__ == "__main__":
    mcp.run()