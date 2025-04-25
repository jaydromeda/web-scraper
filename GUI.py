import tkinter as tk
from tkinter import messagebox
import UserData as user
import AdminCredentials as Admin
import BookSearch as book
from tkinter import ttk
import OutputCSV as CSV
import csv
# Import your other modules here

username = ''
password = ''
number_of_users = 0

def progress_bar():
    prg = tk.Tk()
    prg.title("Working...")

    label_message = tk.Label(prg, text="Creating your account...")
    label_message.pack()

    progressbar = ttk.Progressbar(prg, orient='horizontal', length=200, mode='determinate')
    progressbar.pack()

    cancel_button = tk.Button(prg, text="Cancel", command=prg.destroy)
    cancel_button.pack()

    for i in range(10000):
        progressbar['value'] = i + 1
        prg.update_idletasks()
        if i == 9999:
            prg.destroy()

    prg.mainloop()

def legal():

    window = tk.Tk()
    window.title("Legal Notice")

    legal_notice = """
    THIS IS A LEGAL NOTICE:

    NOTICE: It is important to be aware of legal issues that come with scraping websites, as not all of them appreciate having web crawlers on their server, as they can slow down their processes and even perform criminal activity. While book searching can be considered innocuous, it may keep web administrators on alert. 

    Do not scrape websites without permission.
    """

    label_legal_notice = tk.Label(window, text="Legal Notice", font=("Helvetica", 18))
    label_legal_notice.pack()

    text_legal_notice = tk.Text(window, wrap='word', font=("Helvetica", 12), height=20, width=60)
    text_legal_notice.insert(tk.END, legal_notice)
    text_legal_notice.config(state=tk.DISABLED)
    text_legal_notice.pack()

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack()

    window.mainloop()

def create_account():
    window = tk.Tk()
    global username, password, number_of_users
    window.title("Sign Up")

    label_signup = tk.Label(window, text="Sign Up", font=("Helvetica", 20))
    label_signup.pack()

    label_email = tk.Label(window, text="E-mail")
    label_email.pack()
    entry_email = tk.Entry(window)
    entry_email.pack()

    label_re_email = tk.Label(window, text="Re-enter E-mail")
    label_re_email.pack()
    entry_re_email = tk.Entry(window)
    entry_re_email.pack()

    label_username = tk.Label(window, text="Create Username")
    label_username.pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    label_password = tk.Label(window, text="Create Password")
    label_password.pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    def submit():
        global username, password, number_of_users

        password = entry_password.get()
        username = entry_username.get()
        email = entry_email.get()
        re_email = entry_re_email.get()

        if email != re_email:
            messagebox.showerror("Error", "E-mails do not match")
            return
        else:
            progress_bar()

    button_submit = tk.Button(window, text="Submit", command=submit)
    button_submit.pack()

    button_cancel = tk.Button(window, text="Cancel", command=window.destroy)
    button_cancel.pack()

    window.mainloop()
def admin_login():

    window = tk.Tk()
    window.title("Log In")

    label_login = tk.Label(window, text="Log In", font=("Helvetica", 20))
    label_login.pack()

    label_username = tk.Label(window, text="Username")
    label_username.pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    label_password = tk.Label(window, text="Password")
    label_password.pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    def check_admin_login():
        entered_username = entry_username.get()
        entered_password = entry_password.get()
        admins = [
     ["RayenBenAoun",  "RayenBenAoun"],
    ["AlexanderCooreman", "AlexanderCooreman"],
    ["ChrisCharles", "ChrisCharles"],
    ["JeremiahDillard", "JeremiahDillard"],
    ["RahulGopalan", "RahulGopalan"]]
        success = False
        while True:
            for row in admins:
                    if(entered_username == row[0] and entered_password == row[1]):
                        success = True
                        break
                    else:
                        continue
            if(success):
                messagebox.showinfo("Welcome", "Login Successful!")
                window.destroy()
                break
            else:
                messagebox.showerror("Error", "Invalid login. Try again")
                window.destroy()
                admin_login()

    button_ok = tk.Button(window, text="Ok", command=check_admin_login)
    button_ok.pack()

    button_cancel = tk.Button(window, text="Cancel", command=window.destroy)
    button_cancel.pack()
    window.mainloop()


def login():
    global username, password
    window = tk.Tk()
    window.title("Log In")

    label_login = tk.Label(window, text="Log In", font=("Helvetica", 20))
    label_login.pack()

    label_username = tk.Label(window, text="Username")
    label_username.pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    label_password = tk.Label(window, text="Password")
    label_password.pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    def check_login():
        global username, password
        entered_username = entry_username.get()
        entered_password = entry_password.get()
        if entered_username == username and entered_password == password:
            messagebox.showinfo("Welcome", "Login Successful!")
            window.destroy()
        else:
            messagebox.showerror("Error", "Invalid login. Try again")

    button_ok = tk.Button(window, text="Ok", command=check_login)
    button_ok.pack()

    button_cancel = tk.Button(window, text="Cancel", command=window.destroy)
    button_cancel.pack()

    window.mainloop()
def admin_page():
    messagebox.showinfo('Welcome', 'Welcome to the Admin Page!')
    legal()
    admin_login()


def user_page():
    messagebox.showinfo('Welcome', 'Welcome to the User Page!')
    legal()
    create_account()
    login()
    book.main()


start = tk.Tk()
def on_admin_click():
        global start
        start.destroy()
        admin_page()


def on_user_click():
    global start
    start.destroy()
    user_page()



def main():
    start.title('TitleScreen')
    start.resizable(True, True)

    label_title = tk.Label(start, text='Welcome to the Application!', font=('Helvetica', 18))
    label_title.pack(pady=10)

    admin_button = tk.Button(start, text='Admin', width=10, height=2, command=on_admin_click)
    admin_button.pack(side='left', padx=5)

    user_button = tk.Button(start, text='User', width=10, height=2, command=on_user_click)
    user_button.pack(side='left', padx=5)

    start.mainloop()


if __name__ == "__main__":
    main()
