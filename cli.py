import subprocess
import json
import os
import getpass
from tqdm import tqdm

CONFIG_FILE = 'config.json'

def save_credentials(username, token):
    config_data = {
        "username": username,
        "token": token
    }
    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config_data, config_file)

def load_credentials():
    if not os.path.exists(CONFIG_FILE):
        username = input("Enter your username: ")
        token = getpass.getpass("Enter your token (input will be hidden): ")
        save_credentials(username, token)
    with open(CONFIG_FILE, 'r') as config_file:
        return json.load(config_file)

def run_curl_command(username, token, repo, files):
    for file in tqdm(files, desc="Deleting files", unit="file"):
        url = f"https://aabg.jfrog.io/artifactory/{repo}/{file}"
        curl_command = [
            'curl',
            '-u', f'{username}:{token}',
            '-X', 'DELETE',
            url
        ]
        print(f"\nRunning command: {' '.join(curl_command)}")
        try:
            result = subprocess.run(curl_command, check=True, capture_output=True, text=True)
            print(f'Success: {result.stdout}')
        except subprocess.CalledProcessError as e:
            print(f'Error: {e.stderr}')

def main():
    credentials = load_credentials()
    username = credentials['username']
    token = credentials['token']

    repo = input("Enter the repository name: ")

    files = []
    while True:
        file_name = input("Enter the file name with extension (e.g., file.zip, file.json) or 'done' to finish: ")
        if file_name.lower() == 'done':
            break
        files.append(file_name)

    print(f"\nRepository: {repo}")
    print("Files to delete:")
    for file in files:
        print(f"  - {file}")

    confirm = input("\nDo you want to proceed with the deletion? (yes/no): ").lower()
    if confirm == 'yes':
        run_curl_command(username, token, repo, files)
    else:
        print("Operation cancelled.")

if __name__ == '__main__':
    main()
