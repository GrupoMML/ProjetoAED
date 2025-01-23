import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

def edit_item():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        print(f"Editing item: {item['values']}")

def delete_item():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
        print("Item deleted")

root = tk.Tk()
root.title("Treeview with Buttons")
root.geometry("600x400")

# Create Treeview
tree = ttk.Treeview(root, columns=("Name", "Age"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.pack(fill=tk.BOTH, expand=True)

# Add sample data
tree.insert("", "end", values=("John Doe", 30))
tree.insert("", "end", values=("Jane Smith", 25))

# Create buttons
edit_button = ctk.CTkButton(root, text="Edit", command=edit_item)
edit_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ctk.CTkButton(root, text="Delete", command=delete_item)
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
