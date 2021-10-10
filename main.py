from window import *
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os

HOST = ""
USER = ""
PASSWORD = ""
DATABASE = ""

FONT_NAME = "Courier"
BLUE = "#7393B3"
GRAY = "#E8E8E8"

# root
window = Tk()


def login():
    window.title("Login")
    window.config(padx=100, pady=50, bg=GRAY)

    label_username = Label(window, text="Username", bg=GRAY, fg=BLUE, font=(FONT_NAME, 30))
    label_username.pack()

    entry_username = Entry(width=30)
    entry_username.pack()

    label_password = Label(text="Password", bg=GRAY, fg=BLUE, font=(FONT_NAME, 30))
    label_password.pack()

    entry_password = Entry(width=30, show="*")
    entry_password.pack()

    def submit():
        try:
            db = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
            cursor = db.cursor()

            cursor.execute(
                f"select * from users where username='{entry_username.get()}' and password='{entry_password.get()}'")

            if cursor.fetchall():
                main()
                messagebox.showinfo("logged in", "Logged in successfully")
                # hide login window
                window.withdraw()
            else:
                if not messagebox.askretrycancel("askretrycancel", "Try again?"):
                    window.quit()
                else:
                    # clear entry 0 to END
                    entry_username.delete(0, END)
                    entry_password.delete(0, END)
            # Make sure data is committed to the database
            db.commit()
            cursor.close()
            db.close()
        except mysql.connector.Error as error:
            messagebox.showerror("error", f"Something went wrong: {error}")

    button = Button(text="login", command=submit, fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20))
    button.place(x=110, y=150)

    window.mainloop()


def main():
    window_main = Toplevel(window)
    window_main.title("Main")
    window_main.config(height=400, width=600, padx=100, pady=50, bg=GRAY)

    button_bank = Button(window_main, text="Banks", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 30), command=bank)
    button_bank.place(x=5, y=5)

    button_branch = Button(window_main, text="Branches", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 30),
                           command=branch)
    button_branch.place(x=5, y=55)

    button_customer = Button(window_main, text="Customers", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 30),
                             command=customer)
    button_customer.place(x=5, y=105)

    button_account = Button(window_main, text="Accounts", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 30),
                            command=account)
    button_account.place(x=5, y=155)

    button_loan = Button(window_main, text="Loans", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 30), command=loan)
    button_loan.place(x=5, y=205)

    button_lc = Button(window_main, text="LC", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 30), command=lc)
    button_lc.place(x=5, y=255)

    button_ac = Button(window_main, text="AC", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 30), command=ac)
    button_ac.place(x=60, y=255)

    button_user = Button(window_main, text="Users", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 30), command=user)
    button_user.place(x=255, y=55)

    button_query = Button(window_main, text="Queries", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 30),
                          command=query)
    button_query.place(x=255, y=105)

    button_backup = Button(window_main, text="Backup", fg=BLUE, highlightthickness=0,
                           font=(FONT_NAME, 30), command=backup)
    button_backup.place(x=255, y=155)

    button_restore = Button(window_main, text="Restore", fg=BLUE, highlightthickness=0,
                            font=(FONT_NAME, 30), command=restore)
    button_restore.place(x=255, y=205)


def bank():
    window_bank = Toplevel(window)
    window_bank.title("Banks")
    window_3(window_bank, "bank", ["code", "name", "address"])


def branch():
    window_branch = Toplevel(window)
    window_branch.title("Branches")
    window_3(window_branch, "bank_branch", ["branch_no", "address", "bank_code"])


def loan():
    window_loan = Toplevel(window)
    window_loan.title("Loans")
    window_4(window_loan, "loan", ["loan_no", "amount", "type", "branch_no"])


def account():
    window_account = Toplevel(window)
    window_account.title("Accounts")
    window_4(window_account, "account", ["account_no", "balance", "type", "branch_no"])


def customer():
    window_customer = Toplevel(window)
    window_customer.title("Customers")
    window_4(window_customer, "customer", ["ssn", "name", "address", "phone"])


def lc():
    window_lc = Toplevel(window)
    window_lc.title("LC")
    window_2(window_lc, "lc", ["loan_no", "ssn"])


def ac():
    window_ac = Toplevel(window)
    window_ac.title("AC")
    window_2(window_ac, "ac", ["account_no", "ssn"])


def user():
    window_user = Toplevel(window)
    window_user.title("Users")
    window_user.config(padx=50, pady=50, width=650, height=500, bg=GRAY)

    style_tree_view = Style()
    style_tree_view.configure("style.Treeview", background=BLUE, foreground="white", fieldbackground=BLUE)

    columns = ("Username", "Password")
    tree_view = Treeview(window_user, columns=columns, show="headings", height=14, style="style.Treeview")

    for col in columns:
        # set column width
        tree_view.column(column=col, width=120)
        # fill columns heading
        tree_view.heading(col, text=col)

    tree_view.place(x=300, y=5)

    label_username = Label(window_user, text="Username", bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_username.place(x=5, y=40)
    entry_username = Entry(window_user, width=15)
    entry_username.place(x=100, y=40)

    label_password = Label(window_user, text="Password", bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_password.place(x=5, y=75)
    entry_password = Entry(window_user, width=15)
    entry_password.place(x=100, y=75)

    button_show = Button(window_user, text="Show", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                         command=lambda: show_data("users", tree_view))
    button_show.place(x=70, y=160)

    button_insert = Button(window_user, text="Insert", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"insert into users value('{entry_username.get()}', '{entry_password.get()}');"))
    button_insert.place(x=170, y=160)

    button_delete = Button(window_user, text="Delete", fg=BLUE, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"delete from users where username='{entry_username.get()}';"))
    button_delete.place(x=70, y=210)

    button_update = Button(window_user, text="Update", fg=BLUE, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"update users set password='{entry_password.get()}' where username='{entry_username.get()}';"))
    button_update.place(x=170, y=210)

    label_search_by_username = Label(window_user, text="Search By Username", bg=GRAY, fg=BLUE, font=(FONT_NAME, 12))
    label_search_by_username.place(x=5, y=300)
    entry_search_by_username = Entry(window_user, width=15)
    entry_search_by_username.place(x=5, y=325)
    button_search_by_username = Button(window_user, text="Search", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                                       command=lambda: search_data("users",
                                                                   f"username like '{entry_search_by_username.get()}%'",
                                                                   tree_view))
    button_search_by_username.place(x=40, y=360)


def backup():
    os.system(f"/usr/local/mysql/bin/mysqldump -u {USER} -p{PASSWORD} {DATABASE} > dump.sql")
    messagebox.showinfo("showinfo", "Successful!")


def restore():
    os.system(f"/usr/local/mysql/bin/mysql -u {USER} -p{PASSWORD} dump < dump.sql")
    messagebox.showinfo("showinfo", "Successful!")


login()
