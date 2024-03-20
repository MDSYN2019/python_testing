import requests

def get_failed_pull_requests(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }import requests

def get_failed_pull_requests(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pulls = response.json()
        failed_pulls = []

        for pull in pulls:
            statuses_url = pull['statuses_url']
            status_response = requests.get(statuses_url, headers=headers)

            if status_response.status_code == 200:
                statuses = status_response.json()

                # Check if the latest status is 'failure'
                if statuses and statuses[0]['state'] == 'failure':
                    failed_pulls.append(pull)

        return failed_pulls
    else:
        print(f"Failed to fetch pull requests. Status code: {response.status_code}")
        return []

def close_pull_request(owner, repo, pull_number, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/merge"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "merge_method": "close"
    }
    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Pull request #{pull_number} closed successfully.")
    else:
        print(f"Failed to close pull request #{pull_number}. Status code: {response.status_code}")

        
# Provide your GitHub credentials
owner = "your_username_or_organization"
repo = "your_repository"
token = "your_personal_access_token"

failed_pulls = get_failed_pull_requests(owner, repo, token)
for pull in failed_pulls:
    print(f"Failed PR #{pull['number']}: {pull['title']}")
