import os

from flask import (Flask, redirect, render_template, request, jsonify,
                   send_from_directory, url_for)

app = Flask(__name__)

clipboard_data = ""


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
