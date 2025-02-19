# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:40:09 2025

@author: SOFTLINK COMPUTERS
"""

import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "challenge", "computer", "keyboard"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_attempts:
        print("\nWord: ", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            incorrect_guesses += 1
            print("Incorrect guess!")
        else:
            print("Good guess!")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return
    
    print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()

