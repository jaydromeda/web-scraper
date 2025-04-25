import tkinter as tk
from tkinter import ttk

def search_book():
    title = entry_title.get()
    author = entry_author.get()
    condition = combo_condition.get()
    rating = combo_rating.get()
    binding = combo_binding.get()
    # Add more fields as needed

    # Call your search function with the provided details
    # For example:
    # search_results = search_function(title, author, condition, rating, binding)

# Create main window
root = tk.Tk()
root.title("Book Search")

# Title entry
label_title = tk.Label(root, text="Title:")
label_title.grid(row=0, column=0, sticky="e")
entry_title = tk.Entry(root)
entry_title.grid(row=0, column=1)

# Author entry
label_author = tk.Label(root, text="Author:")
label_author.grid(row=1, column=0, sticky="e")
entry_author = tk.Entry(root)
entry_author.grid(row=1, column=1)

# Condition dropdown
label_condition = tk.Label(root, text="Condition:")
label_condition.grid(row=2, column=0, sticky="e")
conditions = ["Used", "New", "N/A"]
combo_condition = ttk.Combobox(root, values=conditions)
combo_condition.grid(row=2, column=1)
combo_condition.current(0)  # Default selection

# Rating dropdown
label_rating = tk.Label(root, text="Rating:")
label_rating.grid(row=3, column=0, sticky="e")
ratings = ["1 Star", "2 Stars", "3 Stars", "4 Stars", "5 Stars"]
combo_rating = ttk.Combobox(root, values=ratings)
combo_rating.grid(row=3, column=1)
combo_rating.current(0)  # Default selection

# Binding dropdown
label_binding = tk.Label(root, text="Binding:")
label_binding.grid(row=4, column=0, sticky="e")
bindings = ["Hardcover", "Softcover", "N/A"]
combo_binding = ttk.Combobox(root, values=bindings)
combo_binding.grid(row=4, column=1)
combo_binding.current(0)  # Default selection

# Search button
search_button = tk.Button(root, text="Search", command=search_book)
search_button.grid(row=5, columnspan=2)

root.mainloop()
