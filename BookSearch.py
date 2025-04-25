import tkinter as tk
from tkinter import ttk
import pandas as pd
import ScrapeAbeBooks as scrape
import SearchAbeBooks as search
import PrintBookList as PR
import csv
import BookClass as dict

def OutputCSV(books, fileName):
    with open(fileName+'.csv', mode='w', newline='') as csvfile:
        fieldNames = ['Title', 'ISBN', 'Author', 'Condition', 'Publisher', 'Date Published', 'Format', 'Rating', 'Price', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

        writer.writeheader()  # Write the header row

        for book in books:
            writer.writerow(book.to_dict())


def create_main_window():
    root = tk.Tk()
    root.title("Book Search")
    return root

def create_search_widgets(root):
    # Declare variables to store user selections
    title = tk.StringVar()
    product_type = tk.StringVar()
    condition = tk.StringVar()
    rating = tk.StringVar()
    binding = tk.StringVar()

    # Title and/or product entry
    label_title_product = tk.Label(root, text="Title and/or Author:")
    label_title_product.grid(row=0, column=0, sticky="e")
    entry_title = tk.Entry(root, textvariable=title)
    entry_title.grid(row=0, column=1)

    # product type dropdown
    label_product_type = tk.Label(root, text="Product Type:")
    label_product_type.grid(row=1, column=0, sticky="e")
    product_types = ["Books", "Magazines & Periodicals", "Comics", "Sheet Music", "Art, Prints & Posters", "Photographs", "Maps", "Manuscripts"]
    combo_product_type = ttk.Combobox(root, values=product_types, textvariable=product_type)
    combo_product_type.grid(row=1, column=1)
    combo_product_type.current(0)  # Default selection

    # Condition dropdown
    label_condition = tk.Label(root, text="Condition:")
    label_condition.grid(row=2, column=0, sticky="e")
    conditions = ["Used", "New", "N/A"]
    combo_condition = ttk.Combobox(root, values=conditions, textvariable=condition)
    combo_condition.grid(row=2, column=1)
    combo_condition.current(0)  # Default selection

    # Rating dropdown
    label_rating = tk.Label(root, text="Rating:")
    label_rating.grid(row=3, column=0, sticky="e")
    ratings = ["1 Star", "2 Stars", "3 Stars", "4 Stars", "5 Stars"]
    combo_rating = ttk.Combobox(root, values=ratings, textvariable=rating)
    combo_rating.grid(row=3, column=1)
    combo_rating.current(0)  # Default selection

    # Binding dropdown
    label_binding = tk.Label(root, text="Binding:")
    label_binding.grid(row=4, column=0, sticky="e")
    bindings = ["Hardcover", "Softcover", "N/A"]
    combo_binding = ttk.Combobox(root, values=bindings, textvariable=binding)
    combo_binding.grid(row=4, column=1)
    combo_binding.current(0)  # Default selection

    return title, product_type, condition, rating, binding

def search_book(title, product_type, condition, rating, binding):
    # Perform search and scraping
    book_list = []
    URL = search.SearchAbeBook(title.get(), product_type.get(), condition.get(), binding.get(), rating.get())
    scrape.ScrapeBook(URL, book_list)
    PR.PrintBookList(book_list)
    OutputCSV(book_list, "books")

def display_csv(root):
    # Read the CSV file
    try:
        df = pd.read_csv('books.csv', encoding='latin1')
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

# Create main window and search widgets
def main():
    root = create_main_window()
    title, product_type, condition, rating, binding = create_search_widgets(root)

    # Search button
    search_button = tk.Button(root, text="Search", command=lambda: search_book(title, product_type, condition, rating, binding))
    search_button.grid(row=5, columnspan=2)

    # Display CSV button
    display_button = tk.Button(root, text="Display CSV", command=lambda: display_csv(root))
    display_button.grid(row=6, columnspan=2)

    root.mainloop()
