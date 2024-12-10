## Overview
This project involves the development of an intelligent chatbot that uses Natural Language Processing and machine learning techniques to assist users. The chatbot is designed to handle various queries by classifying inputs into predefined categories and providing relevant responses. It is built using Python libraries like 'pyjokes' and offers a user-friendly interface for real-time interaction. Its modular design allows for easy customization, making it suitable for various applications and offering a basic conversational assistance.

----

## Features
- Understands user intents such as greetings,farewell etc
- Generates responses based on the input.
- Able to get information like weather and time.

----

## Technologies Used
- Python
- HTML & CSS
- pyjokes, weather_api
- Flask

## Installation 

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

### 3. Create Flask API for Chatbot
Save the Python chatbot code to a file.
Modify the Python code to expose the chatbot functionality via a Flask endpoint:
```bash
from flask import Flask, request, jsonify

app = Flask(__name__)

bot = ChatBot("HelperBot")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    bot_response = bot.get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
```
This creates a REST API at http://127.0.0.1:5000/chat where the chatbot will respond to incoming messages.

### 4. Link Front and Backend code
Save the provided HTML code
The fetch URL in the code already points to http://127.0.0.1:5000/chat. Ensure this URL matches the Python Flask server's address.

### 5. Run the Backend
Navigate to the directory containing chatbot.py and run:
```bash
python chatbot.py
```
You should see Flask server logs indicating that the API is running on http://127.0.0.1:5000.

### 6. Open Frontend

Open the index.html file in a web browser or any code editors

Test the interface by typing messages into the chatbox. The frontend sends your message to the Flask server, which processes it via the chatbot logic and returns a response displayed in the chat.

After following these steps, you’ll have a working chatbot where the Python backend handles logic, and the frontend interacts with users

## Acknowledgments
- **Open Weather API** for providing real-time weather data
- **Flask Framework** for connecting the chatbot logic with the user interface.



