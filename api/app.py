from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.get_json()
    headers = {
        'Authorization': 'Bearer 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',
        'Content-Type': 'application/json'
    }

    response = requests.post('https://api.openai.com/v1/images/generations', json=data, headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"message": "Failed to generate image."}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)