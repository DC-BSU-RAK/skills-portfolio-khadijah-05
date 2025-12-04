from tkinter import *
import random

# --- Read jokes from the text file ---
with open("randomJokes.txt", "r") as file:
    jokes_list = file.readlines()


# Function to pick a random joke (setup + punchline)
def get_random_joke():
    global setup, punchline
    joke = random.choice(jokes_list)

    # split at question mark
    parts = joke.split("?")
    setup = parts[0] + "?"
    punchline = parts[1]

    # display setup only
    setup_label.config(text=setup)
    punchline_label.config(text="")   # clear previous punchline


# Function to show punchline
def show_punchline():
    punchline_label.config(text=punchline)


# --- Main Window ---
root = Tk()
root.title("Joke Assistant")
root.geometry("450x300")
root.config(bg="#ffffff")

# Title label
title_label = Label(root, text="Joke Telling Assistant", 
                    font=("Arial", 14, "bold"), bg="#ffffff")
title_label.pack(pady=10)

# Button to get a joke
joke_button = Button(root, text="Alexa tell me a Joke",
                     font=("Arial", 12), bg="#22263d", fg="white",
                     command=get_random_joke)
joke_button.pack(pady=10)

# Labels to display joke setup and punchline
setup_label = Label(root, text="", font=("Arial", 12), bg="#ffffff")
setup_label.pack(pady=5)

punchline_label = Label(root, text="", font=("Arial", 12, "italic"), bg="#ffffff")
punchline_label.pack(pady=5)

# Show Punchline button
punchline_button = Button(root, text="Show Punchline",
                          bg="#001111", fg="yellow",
                          font=("Arial", 11),
                          command=show_punchline)
punchline_button.pack(pady=5)

# Next Joke button
next_button = Button(root, text="Next Joke",
                     bg="#234567", fg="white",
                     font=("Arial", 11),
                     command=get_random_joke)
next_button.pack(pady=5)

# Quit button
quit_button = Button(root, text="Quit",
                     bg="red", fg="white",
                     font=("Arial", 11),
                     command=root.quit)
quit_button.pack(pady=10)

root.mainloop()