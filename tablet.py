import requests
import shutil

# URL of the Flask server
server_url = "http://10.100.0.62:5000/"

# Send GET request to retrieve the screenshot image
response = requests.get(f"{server_url}/static/screenshot.png", stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Set the filename for saving the screenshot
    filename = "received_screenshot.png"

    # Open the file in binary write mode
    with open(filename, 'wb') as f:
        # Iterate over the response content and write it to the file
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)

    print(f"Screenshot saved as {filename}")
else:
    print("Error retrieving the screenshot")