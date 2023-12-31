# Keyboard-Listener-and-Google-Drive-Backup

This set of scripts allows you to create a simple keyboard listener using Tkinter and Pynput, logging every key pressed into a file (data.txt). The script then periodically backs up this file to Google Drive using the Google Drive API.

## Prerequisites

1. **Python**: Make sure you have Python installed on your system. You can download it from python.org.

2. **Google API Credentials**:

- Go to the Google Cloud Console.
- Create a new project and enable the Google Drive API.
- Create credentials for a desktop application.
- Download the credentials as credentials.json and place it in the same directory as the scripts.

3. **Install Dependencies**:

  ```bash
  pip install google-auth
  pip install google-auth-oauthlib
  pip install google-auth-httplib2
  pip install google-api-python-client
  pip install pynput
  ```

## Usage

1. **Run the Keyboard Listener**:

- Execute test.py to start the keyboard listener.
- Pressed keys will be logged to the data.txt file in the backupfiles directory.
- Every 50 key presses, the script will automatically back up the data to Google Drive.
  
2. **Google Drive Setup**:

- The backup folder on Google Drive will be named according to your system's username, hostname, and IP address.
     
3. **Drive API Authentication**:

  - The first time you run the script, it will open a browser window for you to authenticate the application with your Google account.
  - Follow the on-screen instructions.
    
4. **Monitor Backup Status**:

  - Check the console for messages indicating whether new data has been backed up or if existing data has been updated.

## Files

- `credentials.json`: Google API credentials file. Must be obtained from the Google Cloud Console.

- `demo.py`: Script for interacting with the Google Drive API, handling authentication, and uploading files.
  
- `test.py`: Main script that utilizes Tkinter and Pynput to create a keyboard listener. It logs key presses to a file and triggers the Google Drive backup when a certain number of key presses is reached.

## Note

- **Security Warning**: Be aware that logging and transmitting user input can raise ethical and legal concerns. Ensure that you have the right to monitor and store this data.
  
- **Token Storage**: The script uses token.json to store authentication tokens. Make sure to keep this file secure.
  
- **Google Drive Quotas**: Be aware of Google Drive API usage limits and quotas to avoid unexpected behavior.
  
- **Dependencies**: Make sure to install the required Python packages before running the scripts.
