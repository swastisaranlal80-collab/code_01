import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Define global variables
player_score = 0
computer_score = 0
rounds_played = 0
player_name = ""  # initialize to avoid reference errors
choices = ["rock", "paper", "scissors"]

# Function to get random computer choice
def generate_computer_choice():
    return random.choice(choices)

# Function to determine the winner of a round
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

# Function to handle a game round
def play_game(player_choice, player_name):
    global player_score, computer_score, rounds_played
    computer_choice = generate_computer_choice()
    winner = determine_winner(player_choice, computer_choice)

    if winner == "player":
        player_score += 1
        result = "You win!"
    elif winner == "computer":
        computer_score += 1
        result = "You lose!"
    else:
        result = "It's a tie!"

    rounds_played += 1

    player_score_label.config(text=f"{player_name} Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    player_result_label.config(text=f"{player_name} > {player_choice}")
    computer_result_label.config(text=f"Computer > {computer_choice}")
    rounds_label.config(text=f"Round {rounds_played + 1}/5")

    if rounds_played == 5:
        if player_score > computer_score:
            winner_label.config(text=f"{player_name}, you win the game!", fg="green")
        elif player_score < computer_score:
            winner_label.config(text="Computer wins the game!", fg="red")
        else:
            winner_label.config(text="It's a tie game!", fg="blue")

        play_again_button.pack(side="top", pady=10)
        rock_button.config(state="disabled")
        paper_button.config(state="disabled")
        scissors_button.config(state="disabled")

# Function to restart the game
def restart_game():
    global player_score, computer_score, rounds_played
    player_score = 0
    computer_score = 0
    rounds_played = 0
    player_score_label.config(text=f"{player_name} Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    player_result_label.config(text="")
    computer_result_label.config(text="")
    winner_label.config(text="")
    play_again_button.pack_forget()
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")
    rounds_label.config(text=f"Round 1/5")

# Function to get player's name
def get_player_name():
    global player_name_var
    player_name_var = tk.StringVar()
    name_window = tk.Toplevel(root)
    name_window.title("Enter your name")

    name_label = tk.Label(name_window, text="Please enter your name:", font="Arial 20 bold", fg="blue")
    name_label.pack(pady=10)

    name_entry = tk.Entry(name_window, textvariable=player_name_var, font="Arial 20 bold", fg="blue")
    name_entry.pack(pady=10)

    def submit_name():
        global player_name
        player_name = player_name_var.get()
        name_window.destroy()
        player_score_label.config(text=f"{player_name} Score: {player_score}")
        computer_score_label.config(text=f"Computer Score: {computer_score}")
        rounds_label.config(text="Round 1/5")

        # Enable game buttons after name entry
        rock_button.config(state="normal")
        paper_button.config(state="normal")
        scissors_button.config(state="normal")

    name_button = tk.Button(name_window, text="Submit", command=submit_name, font="Arial 20 bold", bg="green", fg="white")
    name_button.pack(pady=10)

# GUI Labels
head = tk.Label(text='Rock Paper Scissors', font='Arial 35 bold', bg='orange', fg='white')
head.pack()

player_score_label = tk.Label(root, text="", font="Arial 20 bold", fg="blue")
player_score_label.pack(pady=10)

computer_score_label = tk.Label(root, text="", font="Arial 20 bold", fg="red")
computer_score_label.pack(pady=10)

player_result_label = tk.Label(root, text="", font="Arial 20 bold", fg="blue")
player_result_label.pack(pady=10)

computer_result_label = tk.Label(root, text="", font="Arial 20 bold", fg="red")
computer_result_label.pack(pady=10)

winner_label = tk.Label(root, text="", font="Arial 20 bold")
winner_label.pack(pady=10)

rounds_label = tk.Label(root, text="", font="Arial 20 bold", fg="blue")
rounds_label.pack(pady=10)

# Load images or use text fallback
try:
    rock_img = tk.PhotoImage(file="rock2.png")
    paper_img = tk.PhotoImage(file="paper2.png")
    scissors_img = tk.PhotoImage(file="scissors2.png")
    use_images = True
except Exception:
    use_images = False

# Buttons (disabled initially)
if use_images:
    rock_button = tk.Button(root, image=rock_img, command=lambda: play_game("rock", player_name), state="disabled")
    paper_button = tk.Button(root, image=paper_img, command=lambda: play_game("paper", player_name), state="disabled")
    scissors_button = tk.Button(root, image=scissors_img, command=lambda: play_game("scissors", player_name), state="disabled")
else:
    rock_button = tk.Button(root, text="Rock", font="Arial 15", command=lambda: play_game("rock", player_name), state="disabled")
    paper_button = tk.Button(root, text="Paper", font="Arial 15", command=lambda: play_game("paper", player_name), state="disabled")
    scissors_button = tk.Button(root, text="Scissors", font="Arial 15", command=lambda: play_game("scissors", player_name), state="disabled")

rock_button.pack(side="left", padx=20, pady=10)
paper_button.pack(side="left", padx=20, pady=10)
scissors_button.pack(side="left", padx=20, pady=10)

# Play Again Button
play_again_button = tk.Button(root, text="Play Again", command=restart_game, font="Arial 20 bold", fg="green")

# Start the game
get_player_name()
root.mainloop()
