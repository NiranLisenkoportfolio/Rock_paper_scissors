import tkinter as tk
from tkinter import ttk
import random


"""In this project I will be creating a rock paper scissors game with a graphic interface"""
#I will make this project in the following steps, phase one I will create a regular rock paper scissors game
#phase 2 I will refine the rock paper scissors game
#Phase 3 I will add the gui
#step 4 I will imporve the gui

def game_code(user_choice,comp_choice):
    user_pick = user_choice.get()
    if user_pick == "rock":
        rock_options(user_pick,comp_choice)
    elif user_pick == "paper":
        paper_options(user_pick,comp_choice)
    elif user_pick == "scissors":
        scissors_options(user_pick,comp_choice)
    else:
        result.config("Make sure to enter rock, paper, or scissors. ")
    
            

def scissors_options(user_pick, comp_choice):
    if user_pick == "scissors" and comp_choice == "rock":
        result.config(text=f"You chose {user_pick} and computer chose {comp_choice}, you lose:(")
    else:
        result.config(text=f"You chose {user_pick} and computer chose {comp_choice}, you win:)")
        
def rock_options(user_pick, comp_choice):
    if user_pick == "rock" and comp_choice == "paper":
        result.config(text=f"You chose {user_pick} and computer chose {comp_choice}, you lose:(")
    else:
        result.config(text=f"You chose {user_pick} and computer chose {comp_choice}, you win:)")

def paper_options(user_pick,comp_choice):
    if user_pick == "paper" and comp_choice == "scissors":
        result.config(text=f"You chose {user_pick} and computer chose {comp_choice}, you lose:(")
    else:
        result.config(text=f"You chose {user_pick} and computer chose {comp_choice}, you win:)")
        

choices = ["rock","paper","scissors"]
comp_choice = random.choice(choices)


win = tk.Tk()
page_title = win.title("Rock paper scissors game")
size = win.geometry("650x600")

style = ttk.Style()
style.theme_use("classic")

intro = ttk.Label(win,text="Welcome to rock paper scissors!\nPick rock, paper, or scissors!!!")
intro.pack()

user_choice = ttk.Entry(win)
user_choice.pack()

play_button = ttk.Button(win, text="Enter",command=lambda: game_code(user_choice,comp_choice))
play_button.pack()

result = ttk.Label(win,text="")
result.pack()

win.mainloop()


"""
Things to improve:
Create better debugging.
Create better gui
add users
add images
add a tie version
"""