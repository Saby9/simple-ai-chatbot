from flask import Flask, request, jsonify
from transformers import pipeline

# Initialized Flask app
app = Flask(__name__)

# Loaded a pre-trained conversational model
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

# Generate a response
    bot_response = chatbot(user_input)[0]["generated_text"]
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
