import os
import base64


from flask import (Flask, redirect, render_template, request, jsonify,
                   send_from_directory, url_for)

app = Flask(__name__)

app.static_folder = 'tmp'

clipboard_data = ""
clipboard_array = []

bytes screenshot_bytes



@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/copy', methods=['POST'])
def copy_text():
    global clipboard_data
    data = request.json
    clipboard_data = data.get('clipboard_data')

    return jsonify({'message': 'Clipboard data received successfully'}), 200


@app.route('/paste', methods=['GET'])
def paste_text():
    global clipboard_data

    return jsonify({'clipboard_data': clipboard_data}), 200

@app.route('/screenshotpaste', methods=['GET'])
def paste_text():
    global screenshot_bytes

    return jsonify({'screenshot_base64': screenshot_bytes}), 200

@app.route('/clipboard', methods=['POST'])
def clipboard():
    global clipboard_array
    global screenshot_bytes

    # Get the clipboard text and the screenshot data from the request
    data = request.get_json()
    clipboard_text = data.get('clipboard_text')
    screenshot_base64 = data.get('screenshot_base64')

    # Add the clipboard item to the list
    clipboard_array.append(clipboard_text)

    # Convert the screenshot from base64 to PIL Image
    screenshot_bytes = base64.b64decode(screenshot_base64)

    return "Clipboard data and screenshot updated successfully!"


@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
