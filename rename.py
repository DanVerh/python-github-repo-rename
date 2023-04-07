import requests
import re

# Replace these values with your own information
token = 'TOKEN' # https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
repo_filter = "FILTER_FOR_REPOS"
new_prefix = "NEW_PREFIX"

headers = {'Authorization': f'token {token}'}

# Get a list of repositories
url = 'https://api.github.com/user/repos'
response = requests.get(url, headers=headers)
repos = response.json()
print("All repos:")
print(repos)

# Rename each repository that contains metioned substring in repo_filter
for repo in repos:
    if re.search(repo_filter, repo['name']):
        old_name = repo['name']
        match = re.search(repo_filter, repo['name'])
        print(repo['name'])
        new_name = new_prefix + repo['name']
        url = f'https://api.github.com/repos/{repo["full_name"]}'
        data = {'name': new_name}
        response = requests.patch(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f'Renamed {old_name} to {new_name}')
        else:
            print(f'Error renaming {old_name}: {response.json()}')