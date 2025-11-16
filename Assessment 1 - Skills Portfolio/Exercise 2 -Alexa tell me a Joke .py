from tkinter import *
import random

# Reading the jokes file
with open(r"Assessment 1 - Skills Portfolio\randomJokes.txt", "r") as file:
    jokes_list = file.readlines()


# Function for random joke
def get_random_joke():
    global setup, punchline
    joke = random.choice(jokes_list)

    # split at question mark
    parts = joke.split("?")
    setup = parts[0] + "?"
    punchline = parts[1]

    # display setup only
    setup_label.config(text=setup)
    punchline_label.config(text="")   # clearing previous punchline


# Function to show punchline
def show_punchline():
    punchline_label.config(text=punchline)


# Main Window
root = Tk()
root.title("Joke")
root.geometry("450x300")
root.config(bg="#000000")


# Frame for main joke button
center_frame = Frame(root, 
                     bg="#000000"
                     )
center_frame.pack(expand=True)

# Alexa button 
joke_button = Button(center_frame, 
                     text="Alexa tell me a Joke",
                     font=("Arial", 12), 
                     bg="#000000", 
                     fg="white",
                     command=get_random_joke
                     )
joke_button.pack()


# Labels to display joke setup and punchline
setup_label = Label(root, 
                    text="", 
                    font=("Arial", 12, "bold"), 
                    bg="#000000",
                    fg="white"
                    )
setup_label.pack(pady=5)

punchline_label = Label(root, 
                        text="", 
                        font=("Arial", 12, "italic"), 
                        bg="#000000",
                        fg="white"
                        )
punchline_label.pack(pady=5)


# Show Punchline button
punchline_button = Button(root, 
                          text="Show Punchline",
                          bg="#001111", 
                          fg="white",
                          font=("Arial", 11),
                          command=show_punchline
                          )
punchline_button.pack(pady=5)

# Next Joke button
next_button = Button(root, 
                     text="Next Joke",
                     bg="#000000", 
                     fg="white",
                     font=("Arial", 11),
                     command=get_random_joke
                     )
next_button.pack(pady=5)

# Quit button
quit_button = Button(root, 
                     text="Quit",
                     bg="red", 
                     fg="white",
                     font=("Arial", 11),
                     command=root.quit
                     )
quit_button.pack(pady=10)

# Main GUI event loop
root.mainloop()
