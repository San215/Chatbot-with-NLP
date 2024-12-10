from flask import Flask, request, jsonify
from chatbot import ChatBot 

app = Flask(__name__)
bot = ChatBot("Alexa")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    bot_response = bot.get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
