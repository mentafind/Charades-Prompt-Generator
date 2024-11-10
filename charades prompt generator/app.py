import random
import tkinter as tk

# creating charadeslist
file = open("prompts.txt", "r")
data = file.read()

charadeslist = data.split("\n")

file.close()


# setting up the window
window = tk.Tk()
window.geometry("1000x300")
window.title("Charades Prompt Generator")

# random prompt generator
def click():
    length = len(charadeslist)
    if length == 0: 
        Prompt = "Oops! Looks like we have run out of prompts :("
    else:
        Prompt = charadeslist[random.randint(0,length-1)]
    label.config(text = Prompt)
    charadeslist.remove(Prompt)

label = tk.Label(window, text="Click the button to generate a prompt!", font=(60))

# creating the button
button = tk.Button(window,
                   text="Generate Prompt",
                   font=(40),
                   command=click)

# pack
button.pack()
label.pack()


window.mainloop()