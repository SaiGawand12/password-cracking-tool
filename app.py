from flask import Flask, render_template, request, jsonify
import itertools
import string
from utils import check_password
from cracker import brute_force_password
from config import CHARSET, PASSWORD_LENGTH, NUM_THREADS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', string=string)  # Pass the string module to the template

@app.route('/crack_password', methods=['POST'])
def crack_password():
    password_length = int(request.form['password_length'])
    charset = request.form['charset']  # Charset from user input (e.g., lowercase, digits, special chars)

    cracked_password, attempts = brute_force_password(password_length, charset, num_threads=NUM_THREADS)
    
    if cracked_password:
        return jsonify({'status': 'success', 'password': cracked_password, 'attempts': attempts})
    else:
        return jsonify({'status': 'failure', 'message': 'Password not found.'})

if __name__ == '__main__':
    app.run(debug=True)
