import pyperclip
import requests
import base64
from PIL import ImageGrab
from io import BytesIO

# Capture screenshot from clipboard
clipboard_image = ImageGrab.grabclipboard()

if clipboard_image is not None:
    # Convert screenshot to bytes
    image_buffer = BytesIO()
    clipboard_image.save(image_buffer, format='PNG')
    image_bytes = image_buffer.getvalue()

    # Encode screenshot as base64 string
    screenshot_base64 = base64.b64encode(image_bytes).decode('utf-8')

    # Get clipboard text
    clipboard_text = pyperclip.paste()

    # Send POST request to the server
    url = "http://192.168.1.8:5000/clipboard"
    data = {
        'clipboard_text': clipboard_text,
        'screenshot_base64': screenshot_base64
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Clipboard data and screenshot posted successfully!")
    else:
        print("Error posting clipboard data and screenshot:", response.text)
else:
    print("No screenshot found in clipboard.")
