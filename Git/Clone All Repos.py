import requests
import os
from git import Repo

def download_all_repos(github_username, token=None):
    """Downloads all public repositories of a GitHub user.

    Args:
        github_username (str): The username of the GitHub user.
        token (str, optional): A GitHub personal access token for private repos. Defaults to None.
    """

    base_url = f"https://api.github.com/users/{github_username}/repos"
    headers = {"Authorization": f"token {token}" if token else None}

    while True:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        repos = response.json()
        for repo in repos:
            repo_name = repo["name"]
            clone_url = repo["clone_url"]

            try:
                Repo.clone_from(clone_url, repo_name)
                print(f"Downloaded {repo_name} successfully.")
            except Exception as e:
                print(f"Error downloading {repo_name}: {e}")

        # Check for pagination
        next_page_url = response.links.get("next", {}).get("url")
        if not next_page_url:
            break
        base_url = next_page_url

if __name__ == "__main__":
    github_username = input("Enter the GitHub username: ")
    access_token = input("Enter your personal access token (for private repos): ")
    download_all_repos(github_username, token=access_token)