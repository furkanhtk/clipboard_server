from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image
from io import BytesIO
import socket

app = Flask(__name__)
clipboard_data = []
port_number=5000
app.static_folder = 'tmp'

@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/clipboard', methods=['POST'])
def clipboard():
    global clipboard_data

    # Get the clipboard text and the screenshot data from the request
    data = request.get_json()
    clipboard_text = data.get('clipboard_text')
    screenshot_base64 = data.get('screenshot_base64')

    # Add the clipboard item to the list
    clipboard_data.append(clipboard_text)

    # Convert the screenshot from base64 to PIL Image
    screenshot_bytes = base64.b64decode(screenshot_base64)
    screenshot_image = Image.open(BytesIO(screenshot_bytes))

    # Save the screenshot image to a file
    screenshot_path = "/tmp/screenshot.png"
    screenshot_image.save(screenshot_path)

    return "Clipboard data and screenshot updated successfully!"

@app.route('/check_connection')
def check_connection():
    return jsonify({'status': 'online'})