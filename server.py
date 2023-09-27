from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the clipboard data in a variable (you can use a database for this purpose)
clipboard_data = ""

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
