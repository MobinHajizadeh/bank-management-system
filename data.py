from tkinter import *
from tkinter import messagebox
import mysql.connector

HOST = ""
USER = ""
PASSWORD = ""
DATABASE = ""


def show_data(table, tree_view):
    db = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    cursor = db.cursor()

    cursor.execute(f"select * from {table};")

    # clear
    for item in tree_view.get_children():
        tree_view.delete(item)

    for _ in cursor.fetchall():
        # add to root node last child
        tree_view.insert(parent="", index=END, values=_)

    # Make sure data is committed to the database
    db.commit()
    cursor.close()
    db.close()


def manipulate_data(query):
    try:
        db = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)

        cursor = db.cursor()

        cursor.execute(query)

        # Make sure data is committed to the database
        db.commit()
        cursor.close()
        db.close()
    except mysql.connector.Error as error:
        messagebox.showerror("error", f"Something went wrong: {error}")


def search_data(table, condition, tree_view):
    db = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    cursor = db.cursor()

    cursor.execute(f"select * from {table} where {condition};")

    for item in tree_view.get_children():
        tree_view.delete(item)

    for _ in cursor.fetchall():
        # add to root node last child
        tree_view.insert(parent="", index=END, values=_)

    # Make sure data is committed to the database
    db.commit()
    cursor.close()
    db.close()
