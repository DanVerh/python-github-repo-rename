import requests

# Replace these values with your own information
token = 'YOUR_ACCESS_TOKEN'
repo_filter = 'substring'
new_prefix = 'new-prefix'

headers = {'Authorization': f'token {token}'}

# Get a list of repositories
url = 'https://api.github.com/user/repos'
response = requests.get(url, headers=headers)
repos = response.json()

# Rename each repository that starts with the old prefix
for repo in repos:
    if repo['name'].find(repo_filter):
        old_name = repo['name']
        new_name = new_prefix + repo['name']
        url = f'https://api.github.com/repos/{repo["full_name"]}'
        data = {'name': new_name}
        response = requests.patch(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f'Renamed {old_name} to {new_name}')
        else:
            print(f'Error renaming {old_name}: {response.json()}')