import tkinter as tk
from tkinter import messagebox
from random import randint

def start_game():
    global number, attempts
    attempts = 3
    number = int(randint(1, 100))
    messagebox.showinfo("Guess the Number", "I'm thinking of a number between 1 and 100. Try to guess it!")

def guess_number():
    global number, attempts

    try:
        guess = int(entry_1.get())

        if guess <= 100 and guess >= 1:
            if attempts > 0:
                if guess == number:
                    messagebox.showinfo("Guess the Number", "Congratulations! You guessed the number.")
                elif guess > number:
                    attempts -= 1
                    messagebox.showinfo("Guess the Number", f"Too high remainining attemps {attempts}.")
                elif guess < number:
                    attempts -= 1
                    messagebox.showinfo("Guess the Number", f"Too low remainining attemps {attempts}.")
            else:
                messagebox.showinfo("Guess the Number", "You have no more attempts.")
        else:
            messagebox.showinfo("Guess the Number", "Please enter a valid number.")
    except ValueError:
        messagebox.showinfo("Guess the Number", "Please enter a valid number.")

root = tk.Tk()
root.title("Guess the Number")

label_1 = tk.Label(root, text="Guess the number between 1 and 100")
label_1.grid(row=0, column=0, padx=5, pady=5)

entry_1 = tk.Entry(root)
entry_1.grid(row=0, column=1, padx=5, pady=5)

button_1 = tk.Button(root, text="Start", command=start_game)
button_1.grid(row=0, column=2, padx=5, pady=5)

button_2 = tk.Button(root, text="Guess", command=guess_number)
button_2.grid(row=1, column=2, columnspan=3, padx=5, pady=5)

root.mainloop()