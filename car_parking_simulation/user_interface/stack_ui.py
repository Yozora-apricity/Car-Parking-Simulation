import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import tkinter as tk
from tkinter import ttk, messagebox
from car_park_stack import Stack, Car

class StackUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack Visualizer (Car Parking)")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")

        self.stack = Stack()

        # Title
        tk.Label(self.root, text="Parking Stack", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)

        # --- Controls Frame ---
        control_frame = tk.Frame(self.root, bg="#d9d9d9", padx=10, pady=10)
        control_frame.pack(fill=tk.X, padx=20, pady=10)

        # Row 1: Push Operations
        row1 = tk.Frame(control_frame, bg="#d9d9d9")
        row1.pack(fill=tk.X, pady=5)
        
        self.plate_entry = ttk.Entry(row1, width=15)
        self.plate_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(row1, text="Arrive (Manual)", command=self.push_manual).pack(side=tk.LEFT, padx=5)
        ttk.Button(row1, text="Arrive (Random)", command=self.push_random).pack(side=tk.LEFT, padx=5)

        # Row 2: Pop/Remove Operations
        row2 = tk.Frame(control_frame, bg="#d9d9d9")
        row2.pack(fill=tk.X, pady=5)

        ttk.Button(row2, text="Depart (Pop Top)", command=self.pop_car).pack(side=tk.LEFT, padx=5)
        
        self.remove_entry = ttk.Entry(row2, width=15)
        self.remove_entry.pack(side=tk.LEFT, padx=(20, 5))
        ttk.Button(row2, text="Remove Specific", command=self.remove_specific).pack(side=tk.LEFT, padx=5)

        # Row 3: Info
        self.info_label = tk.Label(control_frame, text="Total Cars: 0", bg="#d9d9d9", font=("Arial", 10))
        self.info_label.pack(anchor="w", pady=5)

        # --- Canvas for Visualization ---
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

    def update_display(self):
        self.canvas.delete("all")
        self.info_label.config(text=f"Total Cars: {self.stack.size()}")
        
        if self.stack.isEmpty():
            self.canvas.create_text(300, 300, text="Parking Lot Empty", fill="gray", font=("Arial", 14))
            return

        # Draw Stack (Bottom to Top)
        car_width = 200
        car_height = 40
        start_x = 200
        start_y = 550  # Start from bottom of canvas

        for i, car in enumerate(self.stack.stack):
            y_pos = start_y - (i * (car_height + 5))
            
            # Draw Car Body
            self.canvas.create_rectangle(start_x, y_pos, start_x + car_width, y_pos + car_height, fill="#4a90e2", outline="black")
            
            # Draw Text
            info_text = f"{car.plate_number} (A:{car.arrivals} | D:{car.departures})"
            self.canvas.create_text(start_x + car_width//2, y_pos + car_height//2, text=info_text, fill="white", font=("Arial", 10, "bold"))

    def push_manual(self):
        plate = self.plate_entry.get().strip().upper()
        if not plate:
            messagebox.showwarning("Input Error", "Please enter a plate number.")
            return
        
        new_car = Car(plate)
        new_car.arrivals += 1 # Increment as per dashboard logic
        self.stack.push(new_car)
        self.plate_entry.delete(0, tk.END)
        self.update_display()

    def push_random(self):
        new_car = Car()
        new_car.arrivals += 1
        self.stack.push(new_car)
        self.update_display()

    def pop_car(self):
        if self.stack.isEmpty():
            messagebox.showinfo("Info", "Lane is empty.")
            return
        
        car = self.stack.pop()
        messagebox.showinfo("Departed", f"Car {car.plate_number} departed.")
        self.update_display()

    def remove_specific(self):
        target = self.remove_entry.get().strip().upper()
        if not target:
            messagebox.showwarning("Input Error", "Please enter a plate number to remove.")
            return
            
        if self.stack.isEmpty():
            messagebox.showinfo("Info", "Lane is empty.")
            return

        # Using the Car().remove_car logic from your file
        temp_car = Car() 
        success = temp_car.remove_car(self.stack, target)
        
        if success:
            messagebox.showinfo("Success", f"Car {target} removed successfully.")
        else:
            messagebox.showerror("Not Found", f"Car {target} not found in lane.")
        
        self.remove_entry.delete(0, tk.END)
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = StackUI(root)
    root.mainloop()