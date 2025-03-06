import tkinter as tk
import random

def play():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    player_choice = player_var.get()
    result_text.set(f"Computer chose: {computer_choice}\n")
    
    if player_choice == computer_choice:
        result_text.set(result_text.get() + "It's a tie!")
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        result_text.set(result_text.get() + "You win!")
    else:
        result_text.set(result_text.get() + "Computer wins!")

window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.configure(bg="#B4D8E7")  # Set background color to light blue

player_var = tk.StringVar()

label = tk.Label(window, text="Choose: rock, paper, or scissors", bg="#B4D8E7")
label.pack()

rock_button = tk.Radiobutton(window, text="Rock", variable=player_var, value="rock", bg="#B4D8E7")
rock_button.pack()

paper_button = tk.Radiobutton(window, text="Paper", variable=player_var, value="paper", bg="#B4D8E7")
paper_button.pack()

scissors_button = tk.Radiobutton(window, text="Scissors", variable=player_var, value="scissors", bg="#B4D8E7")
scissors_button.pack()

play_button = tk.Button(window, text="Play", command=play, bg="#90EE90")  # Set button color to light green
play_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, bg="#B4D8E7")
result_label.pack()

window.mainloop()
