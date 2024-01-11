<<<<<<< HEAD
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reply', methods=['POST'])
def reply():
    apiKey = request.form['apiKey']
    content = request.form['content']
    client = OpenAI(apiKey)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content}
        ]
    )
    message = completion.choices[0].message
    return message

if __name__ == '__main__':
    app.run(debug=True)
=======
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
>>>>>>> 9e4588d740b521069291d68f29ff8133b89d9b11
