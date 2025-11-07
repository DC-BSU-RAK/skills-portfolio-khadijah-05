from tkinter import *
from tkinter import messagebox
import random

def displayMenu():
    """Display difficulty level menu"""
    for widget in root.winfo_children():
        widget.destroy()

    Label(root,
          text="SELECT DIFFICULTY LEVEL", 
          font=("Arial", 14, "bold"), 
          bg="#000000", fg="white"
          ).pack(pady=20)
    
    Button(root, 
           text="Easy", 
           width=20, 
           font=("Arial", 12), 
           command=lambda: startQuiz(1)
           ).pack(pady=5)
    
    Button(root,
           text="Moderate", 
           width=20, 
           font=("Arial", 12), 
           command=lambda: startQuiz(2)
           ).pack(pady=5)
    
    Button(root,
           text="Advanced", 
           width=20, 
           font=("Arial", 12), 
           command=lambda: startQuiz(3)
           ).pack(pady=5)

def randomInt(level):
    """Return random numbers based on difficulty"""
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

def decideOperation():
    """Randomly decide addition or subtraction"""
    return random.choice(["+", "-"])

def displayProblem():
    """Display current question"""
    global number_1, number_2, operation, attempts

    number_1 = randomInt(level)
    number_2 = randomInt(level)
    operation = decideOperation()
    attempts = 0

    question_label.config(text=f"{number_1} {operation} {number_2} = ?")
    answer_entry.delete(0, END)

def isCorrect():
    """Check user's answer"""
    global score, question_no, attempts

    user_answer = answer_entry.get()
    if not user_answer.isdigit() and not (user_answer.startswith('-') and user_answer[1:].isdigit()):
        messagebox.showwarning("Warning", "Please enter a number!")
        return

    correct_answer = number_1 + number_2 if operation == "+" else number_1 - number_2
    attempts += 1

    if int(user_answer) == correct_answer:
        if attempts == 1:
            score += 10
            messagebox.showinfo("Correct!", "✅ Correct on first try! +10 points")
        else:
            score += 5
            messagebox.showinfo("Correct!", "✅ Correct on second try! +5 points")
        question_no += 1
        if question_no <= 10:
            displayProblem()
        else:
            displayResults()
    else:
        if attempts == 1:
            messagebox.showwarning("Try Again", "❌ Wrong! Try once more.")
            answer_entry.delete(0, END)
        else:
            messagebox.showinfo("Incorrect", f"❌ Wrong again! Correct answer was {correct_answer}")
            question_no += 1
            if question_no <= 10:
                displayProblem()
            else:
                displayResults()

def displayResults():
    """Show final score"""
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, 
          text="Quiz Completed!", 
          font=("Arial", 16, "bold"), 
          bg="#234567", fg="white"
          ).pack(pady=20)
    
    Label(root, 
          text=f"Your Final Score: {score}/100",
          font=("Arial", 14), 
          bg="#234567", 
          fg="yellow"
          ).pack(pady=10)

    if score >= 90:
        rank = "A+"
    elif score >= 75:
        rank = "A"
    elif score >= 50:
        rank = "B"
    else:
        rank = "C"

    Label(root, 
          text=f"Your Grade: {rank}", 
          font=("Arial", 14), 
          bg="#234567", 
          fg="white"
          ).pack(pady=10)
    
    Button(root, 
           text="Play Again", 
           width=15, 
           font=("Arial", 12), 
           command=displayMenu
           ).pack(pady=10)
    
    Button(root, 
           text="Exit", 
           width=15, 
           font=("Arial", 12), 
           command=root.destroy
           ).pack(pady=5)

def startQuiz(selected_level):
    """Start the quiz"""
    global level, score, question_no
    level = selected_level
    score = 0
    question_no = 1

    for widget in root.winfo_children():
        widget.destroy()

    Label(root, 
          text="Maths Quiz", 
          font=("Arial", 16, "bold"), 
          bg="#234567", fg="white"
          ).pack(pady=10)

    global question_label, answer_entry
    question_label = Label(root, 
                           text="", 
                           font=("Arial", 14), 
                           bg="#000000", 
                           fg="yellow"
                           )
    question_label.pack(pady=10)

    answer_entry = Entry(root, 
                         font=("Arial", 14)
                         )
    answer_entry.pack(pady=5)

    Button(root, 
           text="Submit", 
           width=12, 
           font=("Arial", 12), 
           command=isCorrect
           ).pack(pady=10)

    displayProblem()


root = Tk()
root.title("Maths Quiz")
root.geometry("400x300")
root.config(bg="#000000")

displayMenu()
root.mainloop()
