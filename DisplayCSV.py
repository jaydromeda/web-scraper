import tkinter as tk
from tkinter import ttk
import pandas as pd

def display_csv():
    # Read the CSV file
    try:
        df = pd.read_csv('boooks.csv', encoding='latin1')
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return

    # Create a new window for displaying the CSV data
    display_window = tk.Toplevel(root)
    display_window.title("Book Data")

    # Create a treeview widget
    tree = ttk.Treeview(display_window)

    # Define columns
    tree["columns"] = list(df.columns)
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the default first column

    # Add column headings
    for column in df.columns:
        tree.heading(column, text=column)

    # Add data rows
    for index, row in df.iterrows():
        tree.insert("", index, values=list(row))

    # Pack the treeview widget
    tree.pack(expand=True, fill=tk.BOTH)

# Create main window
root = tk.Tk()
root.title("CSV Viewer")

# Display CSV button
display_button = tk.Button(root, text="Display CSV", command=display_csv)
display_button.pack(pady=10)

root.mainloop()