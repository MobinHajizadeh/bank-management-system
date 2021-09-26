from PollyReports import *
from reportlab.pdfgen.canvas import Canvas
import mysql.connector
from tkinter import messagebox

HOST = ""
USER = ""
PASSWORD = ""
DATABASE = ""

FONT_NAME = "Helvetica"


def report(table):
    db = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute(f"select * from {table};")
    columns = cursor.column_names
    data = cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()

    elements_detailed_band = [
        Element(pos=(50, 0), font=(FONT_NAME, 11), key=0),
        Element((180, 0), (FONT_NAME, 11), key=1),
        Element((310, 0), (FONT_NAME, 11), key=2),
        Element((440, 0), (FONT_NAME, 11), key=3),
    ]

    i = -2 if len(columns) == 4 else -1
    elements_page_header = [
        Element((35, 0), ("Times-Bold", 20),
                text=f"{table} Report"),
        Element((50, 30), (FONT_NAME, 12),
                text=f"{columns[0].capitalize()}"),
        Element((180, 30), (FONT_NAME, 12),
                text=f"{columns[1].capitalize()}"),
        Element((310, 30), (FONT_NAME, 12),
                text=f"{columns[i].capitalize()}"),
        Element((440, 30), (FONT_NAME, 12),
                text=f"{columns[-1].capitalize()}"),
        Rule((50, 50), 7.5 * 72, thickness=2),
    ]

    rpt = Report(data)
    elements = [element for element in elements_detailed_band[:len(columns)]]
    rpt.detailband = Band(elements)

    elements = [element for element in elements_page_header[:len(columns) + 1]]
    elements.append(elements_page_header[5])
    rpt.pageheader = Band(elements)

    rpt.pagefooter = Band([
        Element((36, 16), ("Helvetica-Bold", 12),
                sysvar="pagenumber",
                format=lambda x: f"Page {x}"),
    ])

    canvas = Canvas(f"00{table}_report.pdf")
    rpt.generate(canvas)
    canvas.save()
    messagebox.showinfo("showinfo", "Successful!")
