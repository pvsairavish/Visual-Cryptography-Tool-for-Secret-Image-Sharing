import cv2
import numpy as np
from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Allowed formats
ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'bmp', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if 'file' not in request.files:
        return "No file uploaded"
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        # Load image
        img = cv2.imread(path)
        rows, cols, ch = img.shape

        # Generate random share
        share1 = np.random.randint(0, 256, size=(rows, cols, ch), dtype=np.uint8)
        share2 = cv2.bitwise_xor(img, share1)

        cv2.imwrite("static/share1.png", share1)
        cv2.imwrite("static/share2.png", share2)

        return render_template("encrypt.html", share1="static/share1.png", share2="static/share2.png")

@app.route('/decrypt')
def decrypt():
    share1 = cv2.imread("static/share1.png")
    share2 = cv2.imread("static/share2.png")
    decrypted = cv2.bitwise_xor(share1, share2)
    cv2.imwrite("static/decrypted.png", decrypted)
    return render_template("decrypt.html", result="static/decrypted.png")
