from tkinter import *
from tkinter import messagebox
import random

# Main Function
def Menu():
    """Display difficulty level menu"""

    # To clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Label for the selection of the difficulty level
    Label(root,
          text="SELECT DIFFICULTY LEVEL", 
          font=("Arial", 14, "bold"), 
          bg="#000000", fg="white"
          ).pack(pady=20)
    
    # Easy button
    Button(root, 
           text="Easy", 
           width=20, 
           font=("Arial", 12), 
           command=lambda: Quiz(1)
           ).pack(pady=5)
    
    # Moderate button 
    Button(root,
           text="Moderate", 
           width=20, 
           font=("Arial", 12), 
           command=lambda: Quiz(2)
           ).pack(pady=5)
    
    # Advanced button
    Button(root,
           text="Advanced", 
           width=20, 
           font=("Arial", 12), 
           command=lambda: Quiz(3)
           ).pack(pady=5)

# Random Number Function
def randomInt(level):
    """Return random numbers based on difficulty"""
    if level == 1:
        return random.randint(1, 9) # Easy being single digit
    elif level == 2:
        return random.randint(10, 99) # Moderate being double digit
    else:
        return random.randint(1000, 9999) #Advamced being triple digit

# Random Operation Function
def decideOperation():
    """Randomly decide addition or subtraction"""
    return random.choice(["+", "-"])

# Question Function
def displayProblem():
    """Display current question"""
    global number_1, number_2, operation, attempts

    # Numbers and Operation for the Question
    number_1 = randomInt(level)
    number_2 = randomInt(level)
    operation = decideOperation()
    attempts = 0 # Reset after each Question

    # Labels for the Question Number 
    question_number_label.config(text=f"Question {question_number} of 10")
    question_label.config(text=f"{number_1} {operation} {number_2} = ?")
    answer_entry.delete(0, END) # Clear previous answer

# Answer Function
def isCorrect():
    """Check user's answer"""
    global score, question_number, attempts

    user_answer = answer_entry.get()
    # If it's a number i.e positive or negative
    if not user_answer.isdigit() and not (user_answer.startswith('-') and user_answer[1:].isdigit()):
        messagebox.showwarning("Warning", "Please enter a number!")
        return

    # Correct answer 
    correct_answer = number_1 + number_2 if operation == "+" else number_1 - number_2
    attempts += 1

    if int(user_answer) == correct_answer:
        if attempts == 1:
            score += 10 # If it's correct at first try, the user earns 10 points
            messagebox.showinfo("Correct!", "Got it on first try! \n+10 points")
        else:
            score += 5 #If it's correct at second try, the user earns 5 points
            messagebox.showinfo("Correct!", "Got it on second try! \n+5 points")
        question_number += 1
        if question_number <= 10:
            displayProblem() # Next Question
        else:
            displayResults() # Quiz finished
    else: # Incorrect answer
        if attempts == 1:
            messagebox.showwarning("Try Again", "Try once more.")
            answer_entry.delete(0, END)
        else:
            messagebox.showinfo("Incorrect", f" Correct answer was {correct_answer}")
            question_number += 1
            if question_number <= 10:
                displayProblem() # Next question
            else:
                displayResults() # Quiz finished

# Result Function
def displayResults():
    """Show final score"""

    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()
    
    # Final score
    Label(root, 
          text=f"Final Score: {score}/100",
          font=("Arial", 14), 
          bg="#000000", 
          fg="White"
          ).pack(pady=10)

    # Grading according to the score
    if score >= 90:
        rank = "A+"
    elif score >= 75:
        rank = "A"
    elif score >= 50:
        rank = "B"
    else:
        rank = "C"

    # Grade Label
    Label(root, 
          text=f"Grade: {rank}", 
          font=("Arial", 14), 
          bg="#000000", 
          fg="white"
          ).pack(pady=10)
    
    # Play again button
    Button(root, 
           text="Play Again", 
           width=15, 
           font=("Arial", 12), 
           command=Menu
           ).pack(pady=10)
    
# Start Quiz Function
def Quiz(selected_level):
    """Start the quiz"""
    global level, score, question_number
    level = selected_level
    score = 0
    question_number = 1

    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Display Question Number Label
    global question_number_label
    question_number_label = Label(root, 
                              text=f"Question {question_number} of 10", 
                              font=("Arial", 14, "bold"), 
                              bg="#000000", 
                              fg="White")
    question_number_label.pack(pady=15)

    # Display the math question
    global question_label, answer_entry
    question_label = Label(root, 
                           text="", 
                           font=("Arial", 14), 
                           bg="#000000", 
                           fg="White"
                           )
    question_label.pack(pady=10)

    # Box for user's answer
    answer_entry = Entry(root, 
                         font=("Arial", 14)
                         )
    answer_entry.pack(pady=5)

    # Submit button
    Button(root, 
           text="Submit", 
           width=12, 
           font=("Arial", 12), 
           command=isCorrect
           ).pack(pady=10)

    displayProblem()

# Main Program
root = Tk()
root.title("Maths Quiz")
root.geometry("400x300")
root.config(bg="#000000")

Menu()

# Run the Tkinter event loop
root.mainloop() 
