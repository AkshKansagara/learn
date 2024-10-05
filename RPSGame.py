import tkinter as tk
from random import choice

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock-Paper-Scissors")
        self.root.geometry("300x300")
        self.root.configure(background="#455A64")  

        self.user_score = 0
        self.computer_score = 0

        self.score_frame = tk.Frame(self.root, bg="#F7F7F7")  
        self.score_frame.pack(pady=10)

        self.user_score_label = tk.Label(self.score_frame, text="Your Score: 0", font=("Segoe UI", 14, "bold"), fg="#333333", bg="#F7F7F7")
        self.user_score_label.pack(side=tk.LEFT, padx=10)

        self.computer_score_label = tk.Label(self.score_frame, text="Computer Score: 0", font=("Segoe UI", 14, "bold"), fg="#333333", bg="#F7F7F7")
        self.computer_score_label.pack(side=tk.LEFT, padx=10)

        self.result_frame = tk.Frame(self.root, bg="#455A64")  
        self.result_frame.pack(pady=10)

        self.result_label = tk.Label(self.result_frame, text="", font=("Segoe UI", 12, "italic"), fg="#FFFFFF", bg="#455A64", wraplength=250)
        self.result_label.pack(padx=10, pady=10)

        self.button_frame = tk.Frame(self.root, bg="#E74C3C")  
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play("rock"), font=("Segoe UI", 12, "bold"), fg="#FFFFFF", bg="#E74C3C", width=10)
        self.rock_button.grid(row=0, column=0, padx=10, pady=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play("paper"), font=("Segoe UI", 12, "bold"), fg="#FFFFFF", bg="#E74C3C", width=10)
        self.paper_button.grid(row=0, column=1, padx=10, pady=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("scissors"), font=("Segoe UI", 12, "bold"), fg="#FFFFFF", bg="#E74C3C", width=10)
        self.scissors_button.grid(row=0, column=2, padx=10, pady=10)

        self.play_again_button = tk.Button(self.button_frame, text="Play Again", command=self.play_again, font=("Segoe UI", 12, "bold"), fg="#FFFFFF", bg="#E74C3C", width=30)
        self.play_again_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.game_over = False

    def play(self, user_choice):
        if not self.game_over:
            choices = ["rock", "paper", "scissors"]
            computer_choice = choice(choices)

            if user_choice == computer_choice:
                result = "It's a tie!"
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "scissors" and computer_choice == "paper") or \
                 (user_choice == "paper" and computer_choice == "rock"):
                result = "You win this round!"
                self.user_score += 1
            else:
                result = "Computer wins this round!"
                self.computer_score += 1

            self.result_label.config(text=f"You chose: {user_choice}, Computer chose: {computer_choice}\n{result}")
            self.user_score_label.config(text=f"Your Score: {self.user_score}")
            self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

            if self.user_score == 3 or self.computer_score == 3:
                self.game_over = True
                self.result_label.config(text=f"Game Over! Final Score - You: {self.user_score}, Computer: {self.computer_score}")

    def play_again(self):
        self.game_over = False
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text="Your Score: 0")
        self.computer_score_label.config(text="Computer Score: 0")
        self.result_label.config(text="")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Game()
    game.run()