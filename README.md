# Artifactory Deletion CLI

This Python CLI application allows you to delete files from an Artifactory repository using the `curl` command. It supports secure input of credentials and provides a progress bar for file deletion.

## Features

- Secure input of username and token
- Stores credentials in a JSON file (`config.json`)
- Prompts user for repository name and file names
- Confirmation prompt before executing deletions
- Progress bar for file deletions

## Requirements

- Python 3.x
- `tqdm` library for the progress bar

## Installation

1. Clone the repository or download the script.

2. Install the `tqdm` library if not already installed:

    ```sh
    pip install tqdm
    ```

## Usage

1. Run the script from the command line:

    ```sh
    python cli_app.py
    ```

2. Enter your username and token when prompted. The token input will be hidden:

    ```plaintext
    Enter your username: your-username
    Enter your token (input will be hidden): 
    ```

3. Enter the repository name and file names interactively:

    ```plaintext
    Enter the repository name: dlf-cft-dev
    Enter the file name with extension (e.g., file.zip, file.json) or 'done' to finish: auto-ml_2.4.5.zip
    Enter the file name with extension (e.g., file.zip, file.json) or 'done' to finish: some-file.json
    Enter the file name with extension (e.g., file.zip, file.json) or 'done' to finish: done
    ```

4. Confirm the files to be deleted:

    ```plaintext
    Repository: dlf-cft-dev
    Files to delete:
      - auto-ml_2.4.5.zip
      - some-file.json

    Do you want to proceed with the deletion? (yes/no): yes
    ```

5. The script will delete each specified file and show a progress bar:

    ```plaintext
    Deleting files:   0%|          | 0/2 [00:00<?, ?file/s]
    Running command: curl -u <username>:<token> -X DELETE https://aabg.jfrog.io/artifactory/dlf-cft-dev/auto-ml_2.4.5.zip
    Success: 
    Deleting files:  50%|#####     | 1/2 [00:01<00:01,  1.00s/file]
    Running command: curl -u <username>:<token> -X DELETE https://aabg.jfrog.io/artifactory/dlf-cft-dev/some-file.json
    Success: 
    Deleting files: 100%|##########| 2/2 [00:02<00:00,  1.00s/file]
    ```

## Configuration File

The script saves your credentials in a `config.json` file located in the same directory as the script. This file is used to avoid re-entering your username and token on subsequent runs.

### Example `config.json`:

```json
{
    "username": "your-username",
    "token": "your-token"
}
