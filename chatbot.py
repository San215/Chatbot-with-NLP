import random
import re
from datetime import datetime
import pyjokes 
import requests  

class ChatBot:
    def __init__(self, name="Alexa"):
        self.name = name
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
            "farewell": ["Goodbye! Have a great day!", "See you soon! Take care!"],
            "time": ["The current time is {}"],
            "joke": ["Here's a joke for you: {}"],
            "quickrecipe": [
                "Sure, here is a simple recipe for Pancakes: Mix flour, milk, eggs, and sugar. Cook on a skillet until golden brown.",
                "Here’s a quick recipe for a Sandwich: Take two slices of bread, spread butter, add veggies or meat, and enjoy!",
                "Try this easy recipe for Pasta: Boil pasta, sauté garlic in olive oil, add sauce, mix pasta, and serve.",
                "Make a Smoothie: Blend bananas, berries, milk, and a spoon of honey together.",
                "Simple Salad: Chop cucumbers, tomatoes, onions, add olive oil, lemon juice, and a pinch of salt."
            ],
            "motivation": [
                "Believe in yourself! Every day is a new opportunity to achieve your goals.",
                "Success is not final, failure is not fatal: It is the courage to continue that counts.",
                "Keep pushing forward. Great things take time.",
                "You are capable of amazing things. Stay focused and stay strong.",
                "Your potential is endless. Go do what you were created to do.",
                "One step at a time is all it takes to get you there.",
                "Dream big and dare to fail.",
                "Don’t watch the clock; do what it does. Keep going.",
                "Act as if what you do makes a difference. It does.",
                "Opportunities don’t happen, you create them."
            ],
            "fact": [
                "Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
                "Bananas are berries, but strawberries are not!",
                "Octopuses have three hearts. Two pump blood to the gills, and one pumps it to the rest of the body.",
                "Sharks existed before trees!",
                "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
                "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
                "A day on Venus is longer than a year on Venus.",
                "Sloths can hold their breath longer than dolphins can.",
                "Wombat poop is cube-shaped.",
                "The hottest chili pepper in the world is so hot it could kill you."
            ],
            "advice": [
                "Always take some time to relax and recharge. Balance is key to success and happiness.",
                "Don’t be afraid to ask for help. Seeking guidance is a sign of strength, not weakness.",
                "Start small but stay consistent. Progress is built one step at a time.",
                "Prioritize your health—mental, physical, and emotional. Without it, nothing else matters.",
                "Learn to say no. Protect your time and energy.",
                "Don’t compare yourself to others. Your journey is unique.",
                "Take breaks when you need them. Resting is part of the process.",
                "Listen more than you speak. You’ll learn more that way.",
                "Focus on what you can control, and let go of what you can’t.",
                "Invest in yourself—it’s the best investment you can make."
            ]
        }
        self.weather_api_key = None

    def get_response(self, user_input):
        user_input = user_input.lower()
        if re.search(r'\bhello|hi|hey\b', user_input):
            return random.choice(self.responses["greeting"])
        elif re.search(r'\bbye|goodbye|see you\b', user_input):
            return random.choice(self.responses["farewell"])
        elif re.search(r'\btime\b', user_input):
            return self.responses["time"][0].format(datetime.now().strftime("%H:%M:%S"))
        elif re.search(r'\bjoke\b', user_input):
            return self.responses["joke"][0].format(pyjokes.get_joke())
        elif re.search(r'\bweather\b', user_input):
            return self.ask_for_api_key()
        elif re.search(r'\bquickrecipe\b', user_input):
            return random.choice(self.responses["quickrecipe"])
        elif re.search(r'\bmotivate|motivation\b', user_input):
            return random.choice(self.responses["motivation"])
        elif re.search(r'\bfact\b', user_input):
            return random.choice(self.responses["fact"])
        elif re.search(r'\badvice\b', user_input):
            return random.choice(self.responses["advice"])
        else:
            return "I'm sorry, I didn't understand that. Could you rephrase?"

    def ask_for_api_key(self):
        if not self.weather_api_key:
            self.weather_api_key = input("Please enter your OpenWeather API key: ")
        city = input("Enter the city for weather information: ")
        return self.get_weather_update(city)

    def get_weather_update(self, city):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temp = data['main']['temp']
                weather = data['weather'][0]['description']
                return f"The current weather in {city} is {weather} with a temperature of {temp}°C."
            else:
                return f"Sorry, I couldn't fetch the weather details for {city}. Please check the API key or city name."
        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == "__main__":
    bot = ChatBot("Alexa")
    print(f"{bot.name}: Hi! I'm {bot.name}. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit"]:
            print(f"{bot.name}: {random.choice(bot.responses['farewell'])}")
            break
        else:
            print(f"{bot.name}: {bot.get_response(user_input)}")