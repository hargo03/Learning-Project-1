#!/usr/bin/env python3
"""
Simple Tkinter GUI to collect user's name and age information.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class UserInfoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("User Information")
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        
        # Variables to store user input
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title label
        title_label = ttk.Label(main_frame, text="User Information Form", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Name label and entry
        name_label = ttk.Label(main_frame, text="Name:")
        name_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        name_entry = ttk.Entry(main_frame, textvariable=self.name_var, width=30)
        name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        name_entry.focus()  # Set focus to name field initially
        
        # Age label and entry
        age_label = ttk.Label(main_frame, text="Age:")
        age_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        
        age_entry = ttk.Entry(main_frame, textvariable=self.age_var, width=30)
        age_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Submit button
        submit_btn = ttk.Button(button_frame, text="Submit", command=self.submit_info)
        submit_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_btn = ttk.Button(button_frame, text="Clear", command=self.clear_form)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Results frame
        self.results_frame = ttk.LabelFrame(main_frame, text="User Information", 
                                           padding="10")
        self.results_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), 
                               pady=20)
        
        # Results labels
        self.result_label = ttk.Label(self.results_frame, text="", 
                                     font=("Arial", 10), justify=tk.LEFT)
        self.result_label.pack()
        
        # Bind Enter key to submit
        self.root.bind('<Return>', lambda event: self.submit_info())
        
    def validate_input(self):
        """Validate the input fields."""
        name = self.name_var.get().strip()
        age_str = self.age_var.get().strip()
        
        # Check if name is provided
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return False
            
        # Check if age is provided
        if not age_str:
            messagebox.showerror("Error", "Please enter your age.")
            return False
            
        # Validate age is a number
        try:
            age = int(age_str)
            if age < 0 or age > 150:
                messagebox.showerror("Error", "Please enter a valid age (0-150).")
                return False
        except ValueError:
            messagebox.showerror("Error", "Age must be a whole number.")
            return False
            
        return True
        
    def submit_info(self):
        """Handle form submission."""
        if self.validate_input():
            name = self.name_var.get().strip()
            age = self.age_var.get().strip()
            
            # Display the information
            result_text = f"Name: {name}\nAge: {age} years old"
            self.result_label.config(text=result_text)
            
            # Show confirmation message
            messagebox.showinfo("Success", f"Information saved!\n\nName: {name}\nAge: {age}")
            
    def clear_form(self):
        """Clear all form fields and results."""
        self.name_var.set("")
        self.age_var.set("")
        self.result_label.config(text="")


def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = UserInfoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()