"""This file is a math game that involves different levels to test the user's skills""" # Docstring to explain purpose
import tkinter as tk
from tkinter import messagebox
import random
import re
from PIL import Image, ImageTk # Let's us upload jpg



class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Ninjas by Flow Computing")
        self.root.configure(bg="#8ec9c1")
        # Load the GIF image once in the constructor
        self.gif = tk.PhotoImage(file="ninja.png")
        # Initialize game state variables
        self.timer_id = None
        self.time_remaining = 10
        self.points = 0
        self.questions_asked = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.correct_answer = None
        self.problem_text = None
        #Create all widgets and layouts
        self.create_widgets()

        # Quit function 
    def quit(self):
        self.root.destroy()  # Close the main window


    def create_widgets(self):
        """
        Create and layout all widgets for the game.
        """
        # Load the background image using Pillow
        self.bg_image = Image.open("ninjabg.jpg")
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        # Welcome frame setup
        self.welcome_frame = tk.Frame(self.root, width=600, height=600, bg="#8ec9c1")
        self.welcome_frame.pack_propagate(False)
        self.welcome_frame.pack()
        # Background image label
        bg_label = tk.Label(self.welcome_frame, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)  # Cover the entire frame
        # Welcome label
        welcome_label = tk.Label(self.welcome_frame, text="Welcome to Number Ninjas!", font=("Georgia", 30), bg="#8ec9c1", fg="#000000")
        welcome_label.grid(row=0, column=0, columnspan=3, pady=20)
        # Name entry prompt
        name_label = tk.Label(self.welcome_frame, text="What's your name?", font=("Georgia", 22), bg="#8ec9c1", fg="#000000")
        name_label.grid(row=1, column=1, pady=10)  # Align label to the right
        # Entry field for the players name
        self.name_entry = tk.Entry(self.welcome_frame, font=("Georgia", 18))
        self.name_entry.grid(row=2, column=1, pady=10, padx=5)  # Place entry next to label
        # Button to start game
        start_button = tk.Button(self.welcome_frame, text="Start", font=("Georgia", 18), fg="#000000", highlightbackground='#8ec9c1', command=self.go_to_main_menu)
        start_button.grid(row=3, column=1, pady=10, padx=5)  # Place button next to entry field
        # Button to quit game
        self.quit_button = tk.Button(self.welcome_frame, text="Quit", font=("Georgia", 18), fg="#000000", highlightbackground='#8ec9c1', command=self.quit)
        self.quit_button.grid(row=7, column=5, columnspan=3, pady=10)  # Adjusted to match grid layout
        # Main Menu frame setup
        self.main_menu_frame = tk.Frame(self.root, width=600, height=600, bg="#8ec9c1")
        self.main_menu_frame.pack_propagate(False)
        # Buttons for main menu
        play_button = tk.Button(self.main_menu_frame, text="Play", font=("Georgia", 18), fg="#000000", highlightbackground='#8ec9c1', command=self.show_levels_page)
        play_button.pack(pady=50)
        # Button for 'How to' page
        how_to_button = tk.Button(self.main_menu_frame, text="How To", font=("Georgia", 18), fg="#000000", highlightbackground='#8ec9c1', command=self.show_how_to_page)
        how_to_button.pack(pady=50)
        # Button for Scoreboard
        scoreboard_button = tk.Button(self.main_menu_frame, text="Scoreboard", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=self.show_scoreboard_page)
        scoreboard_button.pack(pady=50)
        # Button to quit game
        self.quit_button = tk.Button(self.main_menu_frame, text="Quit", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=self.quit)
        self.quit_button.pack(pady=50)

        # Levels frame setup
        self.levels_frame = tk.Frame(self.root, width=600, height=600, bg="#8ec9c1")
        self.levels_frame.pack_propagate(False)
        # Buttons for selecting difficulty levels
        easy_button = tk.Button(self.levels_frame, text="Easy", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=lambda: self.start_game('easy'))
        easy_button.pack(pady=35)

        medium_button = tk.Button(self.levels_frame, text="Medium", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=lambda: self.start_game('medium'))
        medium_button.pack(pady=35)

        hard_button = tk.Button(self.levels_frame, text="Hard", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=lambda: self.start_game('hard'))
        hard_button.pack(pady=35)

        ninja_button = tk.Button(self.levels_frame, text="Ninja", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=lambda: self.start_game('ninja'))
        ninja_button.pack(pady=35)
        # Back button for returning to main menu
        back_button_levels = tk.Button(self.levels_frame, text="Back", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=self.show_main_menu)
        back_button_levels.pack(pady=35)
        # Quit button for quiting application
        self.quit_button = tk.Button(self.levels_frame, text="Quit", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=self.quit)
        self.quit_button.pack(pady=35)
        # How To frame setup
        self.how_to_frame = tk.Frame(self.root, width=600, height=600, bg="#8ec9c1")
        self.how_to_frame.pack_propagate(False)
        # Instructions on how to play the game
        how_to_text = tk.Label(self.how_to_frame, text="How to play:\n\n1. Solve the math problem displayed.\n2. Enter your answer and press Check.\n3. You have a limited time to answer each question.\n4. Your score is based on correct answers and time left.\n5. Try to get as many correct answers as possible!", font=("Georgia", 18), bg="#8ec9c1", fg="#000000")
        how_to_text.pack(pady=20)
        # Back Button for returning to main menu
        back_button_how_to = tk.Button(self.how_to_frame, text="Back", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=self.show_main_menu)
        back_button_how_to.pack(pady=10)
        # Quit button for quitting application
        self.quit_button = tk.Button(self.how_to_frame, text="Quit", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=self.quit)
        self.quit_button.pack(pady=10)
        # Scoreboard frame setup
        self.scoreboard_frame = tk.Frame(self.root, width=600, height=600, bg="#8ec9c1")
        self.scoreboard_frame.pack_propagate(False)
        # Placeholder for scoreboard text
        self.scoreboard_text = tk.Label(self.scoreboard_frame, text="Top Scores:\n", font=("Georgia", 18), bg="#8ec9c1", fg="#000000")
        self.scoreboard_text.pack(pady=20)
        # Back button for returning to main menu
        back_button_scoreboard = tk.Button(self.scoreboard_frame, text="Back", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=self.show_main_menu)
        back_button_scoreboard.pack(pady=10)
        # Quit button for quitting the application
        self.quit_button = tk.Button(self.scoreboard_frame, text="Quit", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=self.quit)
        self.quit_button.pack(pady=10)
        # Game frame setup
        self.game_frame = tk.Frame(self.root, width=600, height=600, bg="#8ec9c1")
        self.game_frame.pack_propagate(False)
        # Label for displaying the math problem
        self.problem_label = tk.Label(self.game_frame, text="", font=("Georgia", 24), bg="#8ec9c1")
        self.problem_label.pack(pady=20)
        # Entry field for user to input their answer in
        self.entry = tk.Entry(self.game_frame, font=("Georgia", 24), width=5)
        self.entry.pack(pady=10)
        # Button to check the user's answer
        check_button = tk.Button(self.game_frame, text="Check", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=self.check_answer)
        check_button.pack()
        # Label for displaying the remaining time
        self.timer_label = tk.Label(self.game_frame, text="Time left: 10 seconds", font=("Georgia", 18), bg="#8ec9c1")
        self.timer_label.pack()
        # Label for displaying the current score
        self.score_label = tk.Label(self.game_frame, text="Score: 0", font=("Georgia", 18), bg="#8ec9c1")
        self.score_label.pack()

        # Quit button for quitting the game
        self.quit_button = tk.Button(self.game_frame, text="Quit", font=("Georgia", 18),fg="#000000", highlightbackground='#8ec9c1', command=self.quit)
        self.quit_button.pack(pady=10)

        # Bingo grid frame and initialization
        bingo_frame = tk.Frame(self.game_frame, bg="#8ec9c1")
        bingo_frame.pack(pady=20)
        self.bingo_grid = [[None for _ in range(5)] for _ in range(2)]

        # Create and position the bingo grid cells
        for i in range(2):
            for j in range(5):
                self.bingo_grid[i][j] = tk.Label(bingo_frame, text="", width=5, height=2, borderwidth=1, relief="solid", font=("Georgia", 16))
                self.bingo_grid[i][j].grid(row=i, column=j)

        self.game_frame.pack_forget() # Initially hide the game's frame

    def go_to_main_menu(self):
        # Validate and process the player's name input
        player_name = self.name_entry.get().strip()
        if not player_name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        if not re.match(r"^[a-zA-Z]+$", player_name):
            messagebox.showerror("Error", "Please enter only letters for your name.")
            return
        
        self.welcome_frame.pack_forget() # Hide the welcome frame
        self.main_menu_frame.pack() # Show the main menu

    def show_levels_page(self):
        # Switch to the levels selection page
        self.main_menu_frame.pack_forget()
        self.levels_frame.pack()

    def show_how_to_page(self):
        # Switch to the How to page
        self.main_menu_frame.pack_forget()
        self.how_to_frame.pack()

    def show_scoreboard_page(self):
        # Switch to the scoreboard page and display top scores
        self.main_menu_frame.pack_forget()
        self.scoreboard_frame.pack()
        self.display_top_scores()

    def show_main_menu(self):
        # Switch back to the main menu
        self.levels_frame.pack_forget()
        self.how_to_frame.pack_forget()
        self.scoreboard_frame.pack_forget()
        self.main_menu_frame.pack()
    def calculate_hcf(self, a, b): # Define the method and calculate HCF of 2 numbers
        while b:
            a, b = b, a % b
        return a
    def generate_problem(self):
        # Generate a math problem based on difficulty
        if self.level == 'easy':
            operation = random.choice(['+', '-']) # Randomly choose between addition and subtraction
            num1 = random.randint(20, 30)
            num2 = random.randint(1, 10)
            return f"{num1} + {num2}", num1 + num2
        elif self.level == 'medium': # Medium level 
            operation = '*' # Multiplication questions
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 15)

        elif self.level == 'hard':  # Hard level
            operation = random.choice(['*', '/'])  # Multiplication or division
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 15)
            if operation == '/':  # Make sure there's no division by zero
                num1 = num1 * num2

        elif self.level == 'ninja':  # Ninja level: HCF questions only
            num1 = random.randint(10, 100)
            num2 = random.randint(10, 100)
            return f"HCF of {num1} and {num2}", self.calculate_hcf(num1, num2)
        else:
            raise ValueError("Invalid difficulty level")
        
        if operation == '+':
            return f"{num1} + {num2}", num1 + num2
        elif operation == '-':
            return f"{num1} - {num2}", num1 - num2
        elif operation == '*':
            return f"{num1} * {num2}", num1 * num2
        elif operation == '/':
            return f"{num1} / {num2}", num1 // num2  # Use integer division 

    def check_answer(self):
        # Cancel any existing timer if the answer is being checked
        if self.timer_id:
            self.game_frame.after_cancel(self.timer_id)
        # Validate and check the user's answer
        user_answer = self.entry.get().strip()# Strip white spaces from the input
        if not user_answer.isdigit():
        # Store the remaining time
            remaining_time = self.time_remaining
            # Display an error message if input is not a valid number
            messagebox.showerror("Error", "Please enter a valid number")
            # Clear the input field
            self.entry.delete(0, tk.END)
            # Restart the timer from where it left off
            self.restart_timer(remaining_time)
            return  # Return early to keep the current question and timer running
        user_answer = int(user_answer)
        
        if user_answer == self.correct_answer:
            messagebox.showinfo("Correct", "Great job!")
            self.update_bingo_board('X')
            self.correct_answers += 1
            self.points += 10
        else:
            messagebox.showerror("Incorrect", f"Wrong answer. The correct answer is {self.correct_answer}")
            self.update_bingo_board('O')
            self.incorrect_answers += 1
            self.points -= 5
        
        self.questions_asked += 1
        self.display_score()

        if self.questions_asked < 10:
            self.new_problem() # Generate a new problem
        else:
            self.end_game() # End the game if maximum questions have been asked
        
    def restart_timer(self, remaining_time):

        # Update the remaining time and restart the timer

        self.time_remaining = remaining_time

        self.timer_label.config(text=f"Time left: {self.time_remaining} seconds")

        self.timer_id = self.game_frame.after(1000, self.update_timer)
    # Generate a new math problem and reset the timer
    def new_problem(self):
        self.problem_text, self.correct_answer = self.generate_problem()
        self.problem_label.config(text=self.problem_text)
        self.entry.delete(0, tk.END)
        
        self.time_remaining = 10
        self.timer_label.config(text=f"Time left: {self.time_remaining} seconds")
        self.timer_id = self.game_frame.after(1000, self.update_timer)

    def update_timer(self):
        # Update the timer display and check for timeout
        self.time_remaining -= 1
        self.timer_label.config(text=f"Time left: {self.time_remaining} seconds")
        if self.time_remaining > 0:
            self.timer_id = self.game_frame.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's up!", "Out of time!")
            self.update_bingo_board('O')
            self.incorrect_answers += 1
            self.points -= 5
            self.questions_asked += 1

            self.entry.delete(0, tk.END)  # Clear the input box
            if self.questions_asked < 10:
                self.new_problem()  # Generate a new question and restart the timer
            else:
                self.end_game() # End the game if the maximum questions have been asked

    def start_game(self, level):
        # Reset all game state variables
        self.level = level
        self.points = 0
        self.questions_asked = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

        # Clear the bingo grid
        for i in range(2):
            for j in range(5):
                self.bingo_grid[i][j].config(text="")

        # Update the score display
        self.display_score()

        # Switch to the game frame and start a new problem
        self.levels_frame.pack_forget()
        self.game_frame.pack()
        self.new_problem()
    def display_score(self):
        # Update the score display
        self.score_label.config(text=f"Score: {self.points}")

    def update_bingo_board(self, mark):
        # Update the bingo board with the mark
        for i in range(2):
            for j in range(5):
                if self.bingo_grid[i][j].cget("text") == "":
                    self.bingo_grid[i][j].config(text=mark)
                    return

    def end_game(self):
        # End the game and display final results
        player_name = self.name_entry.get().strip()
        if self.correct_answers > self.incorrect_answers:
            messagebox.showinfo("Game Over", f"You win! X: {self.correct_answers}, O: {self.incorrect_answers}, Score: {self.points}")
        else:
            messagebox.showinfo("Game Over", f"You lose! X: {self.correct_answers}, O: {self.incorrect_answers}, Score: {self.points}")
        
        self.save_score(player_name, self.points)
        self.game_frame.pack_forget()
        self.main_menu_frame.pack()
        self.display_top_scores()

    def save_score(self, name, score):
        scores = []  # Initialize a empty list to store the top scores
        updated = False  # A flag to check if the score for the user has been updated

        # Try to open the scores file in read mode to load existing scores
        try:
            with open("scores.txt", "r") as file:
                scores = file.readlines()  # Read all lines from the file into a list
        except FileNotFoundError:
            # If the file does not exist then start with an empty list
            scores = []

        # Go through the list of existing scores to check if the username is already present
        for i in range(len(scores)):
            # Split each line into a username and their score
            existing_name, existing_score = scores[i].strip().split(": ")
            
            if existing_name == name:  # Check if the current username matches the one being saved
                if int(existing_score) < score:  # Compare existing score with the new score
                    scores[i] = f"{name}: {score}\n"  # Update the score if the new one is higher
                updated = True  # Set the flag to indicate that the score was updated
                break  # Exit the loop since the user's score is found and updated 

        if not updated:
            # If the user's name was not found in the list, add their new score to the list
            scores.append(f"{name}: {score}\n")

        # Open the file in write mode to save the updated list of scores
        with open("scores.txt", "w") as file:
            file.writelines(scores)  # Write all the scores back to the file


    def display_top_scores(self):
        # Read and display the top scores from the file
        try:
            with open("scores.txt", "r") as file:
                scores = file.readlines()
        except FileNotFoundError:
            scores = []

        scores = [score.strip() for score in scores]
        scores.sort(key=lambda x: int(x.split(": ")[1]), reverse=True)

        self.scoreboard_text.config(text="Scores:\n" + "\n".join(scores[:10]))

            # Load the GIF image
        if not hasattr(self.scoreboard_frame, 'gif'):  # Check if GIF is already loaded
            self.scoreboard_frame.gif = tk.PhotoImage(file="ninja.png")

        # Create or update the label to display the GIF
        if not hasattr(self.scoreboard_frame, 'image_label'):  # Check if image label already exists
            self.scoreboard_frame.image_label = tk.Label(self.scoreboard_frame, image=self.scoreboard_frame.gif, bg='#8ec9c1')
            self.scoreboard_frame.image_label.pack(side=tk.BOTTOM, pady=20)
        else:
            self.scoreboard_frame.image_label.config(image=self.scoreboard_frame.gif)  # Update existing label

# Create the main window and start the game
root = tk.Tk()
game = MathGame(root)
root.mainloop()

