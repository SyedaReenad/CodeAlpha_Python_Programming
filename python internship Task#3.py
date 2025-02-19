# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:06:46 2025

@author: SOFTLINK COMPUTERS
"""

import nltk
import random
import string  # To process standard python strings
from nltk.chat.util import Chat, reflections

# Sample responses
pairs = [
    [
        r"hi|hello|hey", 
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ],
    [
        r"how are you", 
        ["I'm doing well, thank you! How about you?", "I'm great! How can I assist you?"]
    ],
    [
        r"what is your name", 
        ["I am a chatbot created to assist you!", "You can call me ChatBot."]
    ],
    [
        r"(.*) your name(.*)", 
        ["I am ChatBot, nice to meet you!"]
    ],
    [
        r"bye|goodbye", 
        ["Goodbye! Have a nice day!", "See you later!"]
    ],
    [
        r"(.*)", 
        ["I'm not sure I understand. Can you rephrase that?", "Interesting... Tell me more!"]
    ]
]

# Create Chatbot
chatbot = Chat(pairs, reflections)

def chatbot_response():
    print("Hello! I am a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chatbot_response()
