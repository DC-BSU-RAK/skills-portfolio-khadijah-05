from tkinter import *
from tkinter import messagebox

# Loading student record from file
def load_students():
    students = []
    try:
        # Opening file using "with statement"
        with open(r"Assessment 1 - Skills Portfolio\studentMarks.txt", "r") as f:
            lines = f.readlines() # Read all lines
            count = int(lines[0].strip()) # First line is number of students

            # Looping each remaining line 
            for line in lines[1:]:
                data = line.strip().split(",")

                # Handling incomplete lines
                if len(data) < 6:
                    data.append("0")    

                # Extract fields
                code = data[0]
                name = data[1]

                # Converting numeric fields
                c1 = int(data[2])
                c2 = int(data[3])
                c3 = int(data[4])
                exam = int(data[5])

                # Adding to list
                students.append({
                    "code": code,
                    "name": name,
                    "cw": c1 + c2 + c3, # coursework total /60
                    "exam": exam,  # Exam mark /100
                    "overall": (c1 + c2 + c3 + exam) / 160 * 100
                })
        return students

    except:
        messagebox.showerror("Error")
        return [] 

# Saving after adding, deleting and updating file
def save_students_to_file():
    with open(r"Assessment 1 - Skills Portfolio\studentMarks.txt", "w") as f:
        f.write(str(len(students)) + "\n")

        # Looping each student with their detail
        for stu in students:

            # Split coursework 
            cw1 = cw2 = cw3 = stu["cw"] // 3
            f.write(f"{stu['code']},{stu['name']},{cw1},{cw2},{cw3},{stu['exam']}\n")

# Computing grade on bases of percentage
def get_grade(p):

    # Conditional statements for decision-making 
    if p >= 70: return "A"
    elif p >= 60: return "B"
    elif p >= 50: return "C"
    elif p >= 40: return "D"
    else: return "F"

# Displaying single student record

def show_one(student):

    # Clear the text box
    result_box.delete("1.0", END)

    result_box.insert(END, f"Student Name: {student['name']}\n") # name
    result_box.insert(END, f"Student Number: {student['code']}\n") # student code

    # f-strings for formatted outcome
    result_box.insert(END, f"Coursework Total: {student['cw']} / 60\n") # coursework total  
    result_box.insert(END, f"Exam Mark: {student['exam']} / 100\n") # exam mark

    # percentage to 2 decimal places  
    result_box.insert(END, f"Overall %: {student['overall']:.2f}%\n")

    # using helper function get_grade
    result_box.insert(END, f"Grade: {get_grade(student['overall'])}\n")

# Viewing All Student Record in the list
def view_all():
    result_box.delete("1.0", END)

    total_percent = 0 # To calculate class average total

    for stu in students:

        # feilds for the record
        result_box.insert(END, f"Student Name: {stu['name']}\n")
        result_box.insert(END, f"Student Number: {stu['code']}\n")
        result_box.insert(END, f"Coursework Total: {stu['cw']} / 60\n")
        result_box.insert(END, f"Exam Mark: {stu['exam']} / 100\n")
        result_box.insert(END, f"Overall %: {stu['overall']:.2f}%\n")
        result_box.insert(END, f"Grade: {get_grade(stu['overall'])}\n")
        result_box.insert(END, "--------------------------------------------\n\n")
        total_percent += stu["overall"]

    # total for later average calculation
    avg = total_percent / len(students)

    # dispalys the total student in the list and average percentage
    result_box.insert(END, f"\nTotal Students: {len(students)}\n")
    result_box.insert(END, f"Average Percentage: {avg:.2f}%\n")

# Searching for the student in the list using student name or number

def search_student():
    query = entry_search.get().strip().lower()
    result_box.delete("1.0", END)

    # Validate the input
    if query == "":
        messagebox.showwarning("Enter a student name or number.")
        return

    for stu in students:
        if query in stu["code"].lower() or query in stu["name"].lower():
            show_one(stu)
            return

    #if not found
    result_box.insert(END, "Not Found")

    entry_search.delete(0, END)

# Highest Student Record
def view_highest():
    stu = max(students, key=lambda x: x["overall"])
    show_one(stu) # result

# Lowest Student Record
def view_lowest():
    stu = min(students, key=lambda x: x["overall"])
    show_one(stu) # result  

# Sorting Student Record 
def sort_records():
    
    # Creating new window
    win = Toplevel(root)
    win.title("Sort Students")
    win.geometry("250x150")
    win.config(bg="black")

    # label to sort 
    Label(
        win,
        text="Sort by Overall %",
        bg="black",     
        fg="white"       
    ).pack(pady=10)

    # Ascending Order
    def asc():
        students.sort(key=lambda x: x["overall"])
        win.destroy()
        view_all()

    # Descending Order
    def desc():
        students.sort(key=lambda x: x["overall"], reverse=True)
        win.destroy()
        view_all()

    # Button for Ascending
    Button(
        win, 
        text="Ascending", 
        command=asc
    ).pack(pady=5)
    
    # Button for Descending
    Button(
        win, 
        text="Descending", 
        command=desc
    ).pack(pady=5)

# Adding New Student Record to the List 
def add_student_window():

    # New Window
    win = Toplevel(root)
    win.title("Add Student")
    win.geometry("200x200")
    win.config(bg="black")

    # Label for sttudent code
    Label(
        win, 
        text="Student Code",
        bg="black",     
        fg="white"
    ).pack()
    e_code = Entry(win); e_code.pack()

    #label  for student name
    Label(
        win, 
        text="Student Name",
        bg="black",     
        fg="white"
    ).pack()
    e_name = Entry(win); e_name.pack()

    # Label for the coursework total
    Label(
        win, 
        text="Coursework Total (0–60)",
        bg="black",     
        fg="white"
    ).pack()
    e_cw = Entry(win); e_cw.pack()

    # Label for exam marks
    Label(
        win, 
        text="Exam Mark (0–100)",
        bg="black",     
        fg="white"
    ).pack()
    e_exam = Entry(win); e_exam.pack()

# Saving the New Student Record
    def save_new():

        # Retrieve data
        code = e_code.get()
        name = e_name.get()
        cw = int(e_cw.get())
        exam = int(e_exam.get())
        overall = (cw + exam) / 160 * 100

        # Adding new record to list
        students.append({
            "code": code,
            "name": name,
            "cw": cw,
            "exam": exam,
            "overall": overall
        })

        # Saving updated list
        save_students_to_file()
        win.destroy()
        messagebox.showinfo("Student Added")

    # Button to save the record
    Button(
        win, 
        text="Save", 
        command=save_new
        ).pack(pady=10)

#  Deleting Student Record
def delete_student_window():
    win = Toplevel(root)
    win.title("Delete Student")
    win.geometry("200x100")
    win.config(bg="black")

    # Aking user for name or code pf the student that is to be deleted
    Label(
        win, 
        text="Enter Name or Code",
        bg="black",     
        fg="white"
    ).pack(pady=10)

    e_query = Entry(win)
    e_query.pack()

    def delete():
        q = e_query.get().strip().lower()
        for s in students:

             # Checking if it matches student code or name
            if q in s["name"].lower() or q in s["code"].lower():
                students.remove(s) #removed

                # Saving the updated list back to file
                save_students_to_file()
                win.destroy()
                messagebox.showinfo("Deleted")
                return
            
            # If not found
            messagebox.showerror("Not Found")

    # Button for deleting 
    Button(
        win, 
        text="Delete", 
        command=delete
    ).pack(pady=10)

# Updating Sudent Record
def update_student_window():
    win = Toplevel(root)
    win.title("Update Student")
    win.geometry("200x150")
    win.config(bg="black")

     # Label to enter name or code of the student
    Label(
        win, 
        text="Enter Student Name or Code",
        bg="black",     
        fg="white"
    ).pack(pady=10)

    e_query = Entry(win); 
    e_query.pack()

# Searching for student Record that is to be Updated
    def find():
        q = e_query.get().strip().lower()
        for stu in students:
            if q in stu["name"].lower() or q in stu["code"].lower():
                win.destroy()
                edit_student(stu)
                return
        messagebox.showerror("Not Found")
 
    # for the Search of the Record
    Button(
        win, 
        text="Search", 
        command=find
    ).pack(pady=10)

# Editing New Student Record 
def edit_student(stu):
    win = Toplevel(root)
    win.title("Edit Student")
    win.geometry("300x300")
    win.config(bg="black")

    # Label for Update Coursework Total
    Label(
        win, 
        text="Update Coursework Total",
        bg="black",     
        fg="white"
        ).pack()
    
    # Pre-filled with current coursework value
    e_cw = Entry(win); 
    e_cw.insert(0, stu["cw"]); 
    e_cw.pack()

    # Label for update exam mark
    Label(
        win, 
        text="Update Exam Mark",
        bg="black",
        fg="white"
    ).pack()
    
    e_exam = Entry(win); 
    e_exam.insert(0, stu["exam"]);
    e_exam.pack()

# Saving the edited record
    def save_edit():
        stu["cw"] = int(e_cw.get())
        stu["exam"] = int(e_exam.get())
        stu["overall"] = (stu["cw"] + stu["exam"]) / 160 * 100
        
        save_students_to_file()
        win.destroy()
        messagebox.showinfo("Updated")

    # Button to save the Updated Record
    Button(
        win, 
        text="Save",
        command=save_edit
    ).pack(pady=10)

# GUI Layout
root = Tk()
root.title("Student Manager")
root.geometry("360x400")
root.config(bg="black")

students = load_students()

# Left menu
menu_frame = Frame(root, 
                   bg="#000000", 
                   width=200)
menu_frame.pack(side=LEFT, fill=Y)

# Label for the menu
Label(menu_frame, 
      text="MENU",
        bg="#000", 
        fg="white",
      font=("Arial", 18, "bold")
    ).pack(pady=20)

# Button for the view All
Button(menu_frame, 
       text="All Records", 
       width=18, 
       command=view_all
    ).pack(pady=10)

# Button for the highest score
Button(menu_frame, 
       text="Highest Score", 
       width=18, command=view_highest
    ).pack(pady=10)

# Button for the lowest score
Button(menu_frame, 
       text="Lowest Score", 
       width=18, 
       command=view_lowest
    ).pack(pady=10)

# Button to Short Student record
Button(menu_frame, 
       text="Sort Records", 
       width=18, 
       command=sort_records
    ).pack(pady=10)

# Button To Add New Student Record
Button(menu_frame, 
       text="Add Student", 
       width=18, 
       command=add_student_window
       ).pack(pady=10)

# Button to Delete the Student Record
Button(menu_frame, 
       text="Delete Student", 
       width=18, 
       command=delete_student_window
       ).pack(pady=10)

# Button to Update the Student Record
Button(menu_frame, 
       text="Update Student", 
       width=18, 
       command=update_student_window
       ).pack(pady=10)

# Right content
content_frame = Frame(root, 
                      bg="white")
content_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Label for individual Record
Label(content_frame, 
      text="Individual Record", 
      bg="white",
      font=("Arial", 14, "bold")
      ).pack(pady=10)

entry_search = Entry(content_frame, 
                     width=40, 
                     font=("Arial", 12))
entry_search.pack()

# Button For the search pf the individual Record
Button(content_frame, 
       text="Search",
       command=search_student,
       bg="#000", 
       fg="white", 
       width=15).pack(pady=10)

# Result box
result_box = Text(content_frame, 
                  height=20, 
                  width=60, 
                  font=("Arial", 11))
result_box.pack(pady=10)

root.mainloop()