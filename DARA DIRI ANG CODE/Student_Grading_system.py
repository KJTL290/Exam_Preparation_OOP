import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

# Hide main window
root = tk.Tk()
root.withdraw()

# Store students data
students = []

# Get number of students
num_students = simpledialog.askinteger("Input", "How many students to enroll?")

# Collect student information
for _ in range(num_students):
    name = simpledialog.askstring("Input", "Enter student's name:")
    section = simpledialog.askstring("Input", "Enter student's section:")
    status = simpledialog.askinteger("Input", "Is the student registered? (1 for Yes, 0 for No):")
    
    # Get grade only for registered students
    grade = None
    if status == 1:
        while True:
            grade = simpledialog.askfloat("Input", f"Enter grade for {name} (1.0-5.0):")
            if 1.0 <= grade <= 5.0:
                break
            messagebox.showerror("Error", "Grade must be between 1.0 and 5.0")
    
    students.append({
        'name': name,
        'section': section,
        'status': status,
        'grade': grade
    })
# ...existing code...

# Create display window
display = tk.Tk()
display.title("Student Records")

# Configure window size and position
window_width = 600
window_height = 400

# Get screen dimensions
screen_width = display.winfo_screenwidth()
screen_height = display.winfo_screenheight()

# Calculate center position
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# Set window size and position
display.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Create table with proper spacing
tree = ttk.Treeview(display, columns=('Name', 'Section', 'Status', 'Grade'), show='headings')

# Configure column widths
tree.column('Name', width=150, anchor='center')
tree.column('Section', width=150, anchor='center')
tree.column('Status', width=150, anchor='center')
tree.column('Grade', width=150, anchor='center')

# Set column headings
tree.heading('Name', text='Name')
tree.heading('Section', text='Section')
tree.heading('Status', text='Status')
tree.heading('Grade', text='Grade')

# Add data to table
for student in students:
    status_text = "Registered" if student['status'] == 1 else "Not Registered"
    grade_text = f"{student['grade']:.1f}" if student['grade'] is not None else ""
    tree.insert('', tk.END, values=(student['name'], student['section'], status_text, grade_text))

# Display table with proper padding
tree.pack(padx=20, pady=20, expand=True)
display.mainloop()