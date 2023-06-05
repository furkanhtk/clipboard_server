from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image
from io import BytesIO
import socket
import qrcode

app = Flask(__name__)
clipboard_data = []
port_number=5000

@app.route('/')
def home():
    # Get the IP address of the server
    ip_address = socket.gethostbyname(socket.gethostname())
    ip_address = "http://"+ip_address+":{}/static/screenshot.png".format(port_number)
    # Generate a QR code for the IP address
    qr = qrcode.QRCode()
    qr.add_data(ip_address)
    qr.make()

    # Create a BytesIO object to save the QR code image
    qr_image = BytesIO()
    qr.make_image().save(qr_image, 'PNG')

    # Encode the QR code image as a base64 string
    qr_base64 = base64.b64encode(qr_image.getvalue()).decode('utf-8')

    # Render the template with clipboard items, IP address, and QR code
    return render_template('index.html', clipboard_items=clipboard_data, ip_address=ip_address, qr_code=qr_base64)

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
    screenshot_path = "static/screenshot.png"
    screenshot_image.save(screenshot_path)

    return "Clipboard data and screenshot updated successfully!"

@app.route('/check_connection')
def check_connection():
    return jsonify({'status': 'online'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port_number)
