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