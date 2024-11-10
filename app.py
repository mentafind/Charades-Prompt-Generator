import random
import tkinter as tk

# retreiving list from txt file
file = open("prompts.txt", "r")
data = file.read()

charadeslist = data.split("\n")

file.close()

# setting up the counter for remaining prompts
original_length = len(charadeslist)


# setting up the window
window = tk.Tk()
window.geometry("1000x300")
window.title("Charades Prompt Generator")

# random prompt generator
def generateprompt():
    length = len(charadeslist)
    if length == 0: 
        Prompt = "Oops! Looks like we have run out of prompts :("
    else:
        Prompt = charadeslist[random.randint(0,length-1)]
    label.config(text = Prompt)
    charadeslist.remove(Prompt)

    # counter for remaining prompts
    remaining.config(text = length-1)

def hideprompt():
    label.config(text = "Click the button to generate a prompt!")


# text
label = tk.Label(window, text = "Click the button to generate a prompt!", font=("Arial", 40))
space = tk.Label(window, text = "", font=("Arial", 15))
remainingtext = tk.Label(window, text = "Number of Remaining Prompts:")
remaining = tk.Label(window, text = original_length)

# creating buttons
Generate = tk.Button(window,
                   text="Generate Prompt",
                   font=("Arial", 15),
                   command=generateprompt)

HidePrompt = tk.Button(window,
                    text="Hide Prompt",
                    font=("Arial", 7),
                    command=hideprompt)

# pack
Generate.pack()
label.pack()
space.pack()
remainingtext.pack()
remaining.pack()
HidePrompt.pack()


window.mainloop()