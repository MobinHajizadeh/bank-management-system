from tkinter.ttk import Treeview, Style
from report import report
from data import *

FONT_NAME = "Courier"
BLUE = "#7393B3"
GRAY = "#E8E8E8"


def window_2(window, table, columns):
    window.config(padx=50, pady=50, width=650, height=500, bg=GRAY)

    style_tree_view = Style()
    style_tree_view.configure("style.Treeview", background=BLUE, foreground="white", fieldbackground=BLUE)

    tree_view = Treeview(window, columns=columns, show="headings", height=14, style="style.Treeview")

    for col in columns:
        # set column width
        tree_view.column(column=col, width=120)
        # fill columns heading
        tree_view.heading(col, text=col)

    tree_view.place(x=300, y=5)

    label_1 = Label(window, text=columns[0].capitalize(), bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_1.place(x=5, y=40)
    entry_1 = Entry(window, width=15)
    entry_1.place(x=100, y=40)

    label_2 = Label(window, text=columns[1].upper(), bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_2.place(x=5, y=75)
    entry_2 = Entry(window, width=15)
    entry_2.place(x=100, y=75)

    button_show = Button(window, text="Show", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                         command=lambda: show_data(table, tree_view))
    button_show.place(x=70, y=160)

    button_insert = Button(window, text="Insert", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"insert into {table} value('{entry_1.get()}', '{entry_2.get()}');"))
    button_insert.place(x=170, y=160)

    button_delete = Button(window, text="Delete", fg=BLUE, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"delete from {table} where {columns[0]}='{entry_1.get()}' and {columns[1]}='{entry_2.get()}';"))
    button_delete.place(x=70, y=210)

    button_update = Button(window, text="Update", fg=BLUE, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"update {table} set {columns[0]}='{entry_1.get()}' where {columns[1]}='{entry_2.get()}';"))
    button_update.place(x=170, y=210)

    label_search_1 = Label(window, text=f"Search By {columns[0].capitalize()}", bg=GRAY, fg=BLUE, font=(FONT_NAME, 12))
    label_search_1.place(x=5, y=300)
    entry_search_1 = Entry(window, width=15)
    entry_search_1.place(x=5, y=325)
    button_search_1 = Button(window, text="Search", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                             command=lambda: search_data(table,
                                                         f"{columns[0]} like '{entry_search_1.get()}%'",
                                                         tree_view))
    button_search_1.place(x=40, y=360)

    label_search_2 = Label(window, text=f"Search By {columns[1].upper()}", bg=GRAY, fg=BLUE, font=(FONT_NAME, 12))
    label_search_2.place(x=200, y=300)
    entry_search_2 = Entry(window, width=15)
    entry_search_2.place(x=200, y=325)
    button_search_2 = Button(window, text="Search", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                             command=lambda: search_data(table,
                                                         f"{columns[1]} like '{entry_search_2.get()}%'",
                                                         tree_view))
    button_search_2.place(x=235, y=360)

    button_report = Button(window, text="Report", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                           command=lambda: report(table))
    button_report.place(x=120, y=260)


def window_3(window, table, columns):
    window.config(padx=50, pady=50, width=800, height=500, bg=GRAY)

    style_tree_view = Style()
    style_tree_view.configure("style.Treeview", background=BLUE, foreground="white", fieldbackground=BLUE)

    tree_view = Treeview(window, columns=columns, show="headings", height=14, style="style.Treeview")

    for col in columns:
        # set column width
        tree_view.column(column=col, width=120)
        # fill columns heading
        tree_view.heading(col, text=col)

    tree_view.place(x=300, y=5)

    label_1 = Label(window, text=columns[0].capitalize(), bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_1.place(x=5, y=40)
    entry_1 = Entry(window, width=15)
    entry_1.place(x=100, y=40)

    label_2 = Label(window, text=columns[1].capitalize(), bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_2.place(x=5, y=75)
    entry_2 = Entry(window, width=15)
    entry_2.place(x=100, y=75)

    label_3 = Label(window, text=columns[2].capitalize(), bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_3.place(x=5, y=110)
    entry_3 = Entry(window, width=15)
    entry_3.place(x=100, y=110)

    button_show = Button(window, text="Show", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                         command=lambda: show_data(table, tree_view))
    button_show.place(x=70, y=160)

    button_insert = Button(window, text="Insert", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"insert into {table} value('{entry_1.get()}', '{entry_2.get()}', '{entry_3.get()}');"))
    button_insert.place(x=170, y=160)

    button_delete = Button(window, text="Delete", fg=BLUE, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"delete from {table} where {columns[0]}='{entry_1.get()}';"))
    button_delete.place(x=70, y=210)

    button_update = Button(window, text="Update", fg=BLUE, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"update {table} set {columns[1]}='{entry_2.get()}', {columns[2]}='{entry_3.get()}' where {columns[0]}='{entry_1.get()}';"))
    button_update.place(x=170, y=210)

    label_search_1 = Label(window, text=f"Search By {columns[0].capitalize()}", bg=GRAY, fg=BLUE, font=(FONT_NAME, 12))
    label_search_1.place(x=5, y=300)
    entry_search_1 = Entry(window, width=15)
    entry_search_1.place(x=5, y=325)
    button_search_1 = Button(window, text="Search", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                             command=lambda: search_data(table, f"{columns[0]} like '%{entry_search_1.get()}%'",
                                                         tree_view))
    button_search_1.place(x=40, y=360)

    label_search_2 = Label(window, text=f"Search By {columns[1].capitalize()}", bg=GRAY, fg=BLUE, font=(FONT_NAME, 12))
    label_search_2.place(x=200, y=300)
    entry_search_2 = Entry(window, width=15)
    entry_search_2.place(x=200, y=325)
    button_search_2 = Button(window, text="Search", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                             command=lambda: search_data(table, f"{columns[1]} like '%{entry_search_2.get()}%'",
                                                         tree_view))
    button_search_2.place(x=235, y=360)

    label_search_3 = Label(window, text=f"Search By {columns[2].capitalize()}", bg=GRAY, fg=BLUE,
                           font=(FONT_NAME, 12))
    label_search_3.place(x=395, y=300)
    entry_search_3 = Entry(window, width=15)
    entry_search_3.place(x=395, y=325)
    button_search_3 = Button(window, text="Search", fg=BLUE, highlightthickness=0,
                             font=(FONT_NAME, 20),
                             command=lambda: search_data(table, f"{columns[2]} like '%{entry_search_3.get()}%'",
                                                         tree_view))
    button_search_3.place(x=430, y=360)

    button_report = Button(window, text="Report", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                           command=lambda: report(table))
    button_report.place(x=120, y=260)


def window_4(window, table, columns):
    window.config(padx=50, pady=50, width=860, height=500, bg=GRAY)

    style_tree_view = Style()
    style_tree_view.configure("style.Treeview", background=BLUE, foreground="white", fieldbackground=BLUE)

    tree_view = Treeview(window, columns=columns, show="headings", height=14, style="style.Treeview")

    for col in columns:
        # set column width
        tree_view.column(column=col, width=120)
        # fill columns heading
        tree_view.heading(col, text=col)

    tree_view.place(x=300, y=5)

    label_1 = Label(window, text=columns[0].capitalize(), bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_1.place(x=5, y=40)
    entry_1 = Entry(window, width=15)
    entry_1.place(x=100, y=40)

    label_2 = Label(window, text=columns[1].capitalize(), bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_2.place(x=5, y=75)
    entry_2 = Entry(window, width=15)
    entry_2.place(x=100, y=75)

    label_3 = Label(window, text=columns[2].capitalize(), bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_3.place(x=5, y=110)
    entry_3 = Entry(window, width=15)
    entry_3.place(x=100, y=110)

    label_4 = Label(window, text=columns[3].capitalize(), bg=GRAY, fg=BLUE, font=(FONT_NAME, 15))
    label_4.place(x=5, y=145)
    entry_4 = Entry(window, width=15)
    entry_4.place(x=100, y=145)

    button_show = Button(window, text="Show", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                         command=lambda: show_data(table, tree_view))
    button_show.place(x=70, y=190)

    button_insert = Button(window, text="Insert", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"insert into {table} value('{entry_1.get()}', '{entry_2.get()}', '{entry_3.get()}',"
                               f" '{entry_4.get()}');"))
    button_insert.place(x=170, y=190)

    button_delete = Button(window, text="Delete", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"delete from {table} where {columns[0]}='{entry_1.get()}';"))
    button_delete.place(x=70, y=240)

    button_update = Button(window, text="Update", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                           command=lambda: manipulate_data(
                               f"update {table} set {columns[1]}={entry_2.get()}, {columns[2]}='{entry_3.get()}',"
                               f" {columns[3]}='{entry_4.get()}' where {columns[0]}='{entry_1.get()}';"))
    button_update.place(x=170, y=240)

    label_search_1 = Label(window, text=f"Search By {columns[0].capitalize()}", bg=GRAY, fg=BLUE, font=(FONT_NAME, 12))
    label_search_1.place(x=5, y=325)
    entry_search_1 = Entry(window, width=15)
    entry_search_1.place(x=5, y=350)
    button_search_1 = Button(window, text="Search", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                             command=lambda: search_data(table,
                                                         f"{columns[0]} like '{entry_search_1.get()}%'",
                                                         tree_view))
    button_search_1.place(x=40, y=390)

    label_search_2 = Label(window, text=f"Search By {columns[1].capitalize()}", bg=GRAY, fg=BLUE, font=(FONT_NAME, 12))
    label_search_2.place(x=200, y=325)
    entry_search_2 = Entry(window, width=15)
    entry_search_2.place(x=200, y=350)
    button_search_2 = Button(window, text="Search", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                             command=lambda: search_data(table,
                                                         f"{columns[1]} like '%{entry_search_2.get()}%'",
                                                         tree_view))
    button_search_2.place(x=235, y=390)

    label_search_3 = Label(window, text=f"Search By {columns[2].capitalize()}", bg=GRAY, fg=BLUE, font=(FONT_NAME, 12))
    label_search_3.place(x=395, y=325)
    entry_search_3 = Entry(window, width=15)
    entry_search_3.place(x=395, y=350)
    button_search_3 = Button(window, text="Search", fg=BLUE, highlightthickness=0,
                             font=(FONT_NAME, 20),
                             command=lambda: search_data(table, f"{columns[2]} like '%{entry_search_3.get()}%'",
                                                         tree_view))
    button_search_3.place(x=430, y=390)

    label_search_by_4 = Label(window, text=f"Search By {columns[3].capitalize()}", bg=GRAY, fg=BLUE,
                              font=(FONT_NAME, 12))
    label_search_by_4.place(x=590, y=325)
    entry_search_by_4 = Entry(window, width=15)
    entry_search_by_4.place(x=590, y=350)
    button_search_by_4 = Button(window, text="Search", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                                command=lambda: search_data(table,
                                                            f"{columns[3]} like '%{entry_search_by_4.get()}%'",
                                                            tree_view))
    button_search_by_4.place(x=625, y=390)

    button_report = Button(window, text="Report", fg=BLUE, highlightthickness=0, font=(FONT_NAME, 20),
                           command=lambda: report(table))
    button_report.place(x=120, y=290)
