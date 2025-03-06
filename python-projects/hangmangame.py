import tkinter as tk
from tkinter import messagebox
import random
import requests

# Function to fetch a random word from the API
def fetch_random_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    if response.status_code == 200:
        word = response.json()[0]
        return word
    else:
        messagebox.showinfo("Error", "Failed to fetch a random word.")
        return None

# Function to start a new game
def new_game():
    global secret_word, attempts_left, guessed_letters
    secret_word = fetch_random_word()
    if secret_word is None:
        return
    attempts_left = 15  # Update the number of attempts to 15
    guessed_letters = []
    update_word_label()
    update_attempts_label()

# Function to check if the guessed letter is correct
def check_letter():
    global attempts_left  # Add this line
    letter = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        messagebox.showinfo("Invalid Input", "Please enter a single letter.")
        return

    if letter in guessed_letters:
        messagebox.showinfo("Already Guessed", "You've already guessed that letter.")
        return

    guessed_letters.append(letter)

    if letter not in secret_word:
        attempts_left -= 1
        update_attempts_label()
        if attempts_left == 0:
            messagebox.showinfo("Game Over", f"The word was {secret_word}. You lost!")
            new_game()
    else:
        update_word_label()

        if "_" not in word_label["text"]:
            messagebox.showinfo("Congratulations", "You won!")
            new_game()

# Function to update the word label
def update_word_label():
    word_label["text"] = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

# Function to update the attempts label
def update_attempts_label():
    attempts_label["text"] = f"Attempts Left: {attempts_left}"

# Create the main window
window = tk.Tk()
window.title("Hangman Game")
window.configure(bg="#e1f5fe")  # Set the background color to light blue

# Create the word label
word_label = tk.Label(window, font=("Arial", 24), bg="#e1f5fe")
word_label.pack(pady=10)

# Create the attempts label
attempts_label = tk.Label(window, font=("Arial", 14), bg="#e1f5fe")
attempts_label.pack()

# Create the letter entry
letter_entry = tk.Entry(window, font=("Arial", 14))
letter_entry.pack(pady=10)

# Create the check button
check_button = tk.Button(window, text="Check", font=("Arial", 14), command=check_letter)
check_button.pack()

# Start a new game
new_game()

# Run the main loop
window.mainloop()
