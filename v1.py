import tkinter as tk
from tkinter import messagebox
import random

# Function to generate a new math problem
def generate_problem():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    return f"{num1} + {num2}", num1 + num2

# Function to check the answer
def check_answer():
    user_answer = entry.get()
    try:
        user_answer = int(user_answer)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return
    
    if user_answer == correct_answer:
        messagebox.showinfo("Correct", "Great job!")
    else:
        messagebox.showerror("Incorrect", f"Wrong answer. The correct answer is {correct_answer}")
    
    # Generate a new problem after checking answer
    new_problem()

# Function to display a new problem
def new_problem():
    global problem_text, correct_answer
    problem_text, correct_answer = generate_problem()
    problem_label.config(text=problem_text)
    entry.delete(0, tk.END)  # Clear the entry widget

# Function to start the game
def start_game():
    welcome_frame.pack_forget()  # Hide the welcome frame
    game_frame.pack()  # Show the game frame
    new_problem()  # Start the first problem

# Create the main window
root = tk.Tk()
root.title("Simple Math Game")

# Welcome frame
welcome_frame = tk.Frame(root, padx=50, pady=30)
welcome_frame.pack()

welcome_label = tk.Label(welcome_frame, text="Welcome to Simple Math Game", font=("Helvetica", 24))
welcome_label.pack(pady=20)

start_button = tk.Button(welcome_frame, text="Start Game", font=("Helvetica", 18), command=start_game)
start_button.pack()

# Game frame
game_frame = tk.Frame(root, padx=50, pady=30)

problem_label = tk.Label(game_frame, text="", font=("Helvetica", 24))
problem_label.pack(pady=20)

entry = tk.Entry(game_frame, font=("Helvetica", 24), width=5)
entry.pack(pady=10)

check_button = tk.Button(game_frame, text="Check", font=("Helvetica", 18), command=check_answer)
check_button.pack()

# Hide the game frame at first
game_frame.pack_forget()

# Run the main loop
root.mainloop()
