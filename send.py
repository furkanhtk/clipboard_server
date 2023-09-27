import requests
import json

# Define the URL of your Flask server's "/copy" endpoint
url = "http://127.0.0.1:80/copy"

# Replace this with the data you want to send
data_to_send = {
    "clipboard_data": "This is the data I want to send to the server"
}

# Send a POST request to the server
response = requests.post(url, json=data_to_send)

# Check the response from the server
if response.status_code == 200:
    print("Data sent successfully")
else:
    print(f"Failed to send data. Status code: {response.status_code}")
