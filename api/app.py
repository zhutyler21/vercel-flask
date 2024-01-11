import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Get list of files in /static/img
    img_files = os.listdir(os.path.join(app.root_path, 'static/img'))

    # Filter out non-image file types if necessary
    img_files = [img for img in img_files if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Select the first image file
    img_file = img_files[0] if img_files else None

    return render_template('index.html', img_file=img_file)

if __name__ == '__main__':
    app.run(debug=True)
