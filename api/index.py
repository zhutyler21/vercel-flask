from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    image = Image.open(file.stream).convert('L')
    img_io = io.BytesIO()
    image.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
