import requests

# Define the URL of your Flask server's "/paste" endpoint
url = "http://127.0.0.1:80/paste"

# Send a GET request to retrieve the clipboard data
response = requests.get(url)

# Check the response from the server
if response.status_code == 200:
    data = response.json()
    clipboard_data = data.get('clipboard_data')
    print(f"Clipboard Data: {clipboard_data}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
