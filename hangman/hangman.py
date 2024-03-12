import tkinter as tk
import ttkbootstrap as ttk
import requests

global total_guess, word

page = requests.get("https://random-word-api.herokuapp.com/word")
list = list(page.json())
x = str(list[0])
print(x)
word = []
for char in x: 
    word.append(char)

total_guess = ["_" for x in word]

def guess():
    old_guesses = guess_string.get()
    new_guess = entry_letter.get()
    if len(new_guess) == 1 and new_guess not in old_guesses:
        new_guess_string = old_guesses + new_guess
        guess_string.set(new_guess_string)
    guess_count = guesses.get()

    for i, char in enumerate(word):
        if word[i] == new_guess:
            total_guess[i] = char
    word_string.set(total_guess)
    

    if new_guess not in word:
        guess_count = guess_count + 1
        guesses.set(guess_count)
    if guess_count == 6:
        new_string = "YOU LOSE"
        guess_string.set(new_string)
    entry_letter.set("")

    match guess_count:
        case 0:
            hangman = ""
        case 1:
            hangman = """
        O"""
        case 2:
            hangman = """
        O
      \ """
        case 3:
            hangman = """
        O
      \ |"""
        case 4:
            hangman = """
        O
      \ | /"""
        case 5:
            hangman = """
        O
      \ | / 
        /"""
        case 6:
            hangman = """
        O 
      \ | /
        /\ """
        
    hangman_string.set(hangman)



# main window

window = ttk.Window(themename ="darkly")
window.title("Hangman")
window.geometry("325x250")

# title 
title_lable = ttk.Label(master = window,
                        text = "Hangman",
                        font = "Calibri 20")
title_lable.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_letter = tk.StringVar()
entry = ttk.Entry(master = input_frame,
                  textvariable = entry_letter)
button = ttk.Button(master = input_frame,
                    text = "Guess",
                    command = guess)
entry.pack(side = "left")
button.pack(side = "right")
input_frame.pack()

# display word field 
word_string = tk.StringVar()
word_label = ttk.Label(master = window,
                       text = "_ _ _ _ _ _", 
                       font = "Calibri 14 bold",
                       textvariable = word_string)
word_label.pack()


# guess field
guess_string = tk.StringVar()
guesses = tk.IntVar()
guess_label = ttk.Label(master = window,
                         text = "",
                         font = "Calibri 14 bold",
                         textvariable = guess_string)
guess_label.pack(padx=0)

# hangman field
hangman_string = tk.StringVar()
hangman_label = ttk.Label(master = window, 
                          text = "",
                          font = "Calibri 14 bold",
                          textvariable = hangman_string)
hangman_label.pack()

window.mainloop()