import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def generate_bar_chart():
    name = entry_name.get()
    try:
        phy_marks = float(entry_phy.get())
        chem_marks = float(entry_chem.get())
        maths_marks = float(entry_maths.get())
        
        if not (0 <= phy_marks <= 100 and 0 <= chem_marks <= 100 and 0 <= maths_marks <= 100):
            raise ValueError("Marks should be between 0 and 100")
        
        subjects = ['Physics', 'Chemistry', 'Maths']
        marks = [phy_marks, chem_marks, maths_marks]

        plt.figure(figsize=(8, 6))
        plt.bar(subjects, marks, color=['blue', 'green', 'orange'])
        plt.ylim(0, 100)
        plt.title(f'{name} - Subject Marks')
        plt.xlabel('Subjects')
        plt.ylabel('Marks')
        plt.show()
    except ValueError as ve:
        messagebox.showerror("Invalid Input", f"Please enter valid marks: {ve}")

# Create the main window
root = tk.Tk()
root.title("Marks Entry and Bar Chart Generator")
root.geometry("700x700")

# Define font size
font_large = ('Arial', 14)

# Create and place labels and entries
tk.Label(root, text="Name", font=font_large).pack(pady=10)
entry_name = tk.Entry(root, font=font_large, width=30)
entry_name.pack(pady=10)

tk.Label(root, text="Physics Marks", font=font_large).pack(pady=10)
entry_phy = tk.Entry(root, font=font_large, width=30)
entry_phy.pack(pady=10)

tk.Label(root, text="Chemistry Marks", font=font_large).pack(pady=10)
entry_chem = tk.Entry(root, font=font_large, width=30)
entry_chem.pack(pady=10)

tk.Label(root, text="Maths Marks", font=font_large).pack(pady=10)
entry_maths = tk.Entry(root, font=font_large, width=30)
entry_maths.pack(pady=10)

# Create and place the button
generate_button = tk.Button(root, text="Generate Bar Chart", command=generate_bar_chart, font=font_large, width=25)
generate_button.pack(pady=40)

# Start the Tkinter main loop
root.mainloop()
