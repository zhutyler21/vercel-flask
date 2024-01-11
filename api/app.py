from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data["message"]
    openai.api_key = data["api_key"]

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=user_message,
    max_tokens=150
    )

    return jsonify({"response": response["choices"][0]["text"]["content"]}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # 运行在localhost的5000端口上