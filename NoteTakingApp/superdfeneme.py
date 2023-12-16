from datetime import date
from tkinter import *
from tkinter.ttk import *
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="notetaking"
)

mycursor = mydb.cursor()

# Create the main window
master = Tk()
master.title("Note Taking App")
master.geometry("600x700")

# Banner
label = Label(master, text="THIS IS MAIN WINDOW")
label.pack(pady=10)

displayed_notes = None  # Initializing the displayed_notes variable

def clear_notes():
    global displayed_notes
    if displayed_notes:
        displayed_notes.destroy()
        displayed_notes = None

def view_notes(id):
    mycursor.execute(f"SELECT * FROM notes WHERE id={id}")
    myresult = mycursor.fetchall()
    for x in myresult:
        pass
    newWindow = Toplevel(master)
    newWindow.title(x[1])
    newWindow.geometry("300x300")
    Label(newWindow, text=x[3], wraplength=200).pack()

    def delete_note(id):
        query = "DELETE FROM notes WHERE id = %s"
        mycursor.execute(query, (id,))
        mydb.commit()
        newWindow.destroy()
        view_master()

    delete_button = Button(newWindow, text="Delete", command=lambda x=id: delete_note(x))
    delete_button.pack()

def view_master():
    clear_notes()
    mycursor.execute("SELECT * FROM notes")
    myresult = mycursor.fetchall()
    global displayed_notes
    for x in myresult:
        btn = Button(master, text=f"{x[1]} | Category : {x[2]}", command=lambda id=x[0]: view_notes(id))
        btn.pack(pady=10)

def display_add_note_section():
    add_note_window = Toplevel(master)
    add_note_window.title("Add Note")
    add_note_window.geometry("300x300")

    Label(add_note_window, text="Title:").pack()
    title_entry = Entry(add_note_window)
    title_entry.pack()

    Label(add_note_window, text="Category:").pack()
    category_entry = Entry(add_note_window)
    category_entry.pack()

    Label(add_note_window, text="Content:").pack()
    content_entry = Text(add_note_window, height=10, width=30)
    content_entry.pack()

    add_button = Button(add_note_window, text="Save!", command=lambda: add_note(title_entry.get(), content_entry.get("1.0", END), category_entry.get()))
    add_button.pack()
    view_master()

def add_note(title, content, category):
    today = date.today()
    mycursor.execute("INSERT INTO notes (Title, Category, Context, Date) VALUES (%s, %s, %s, %s)", (title, category, content, today))
    mydb.commit()
    view_master()

add_note_button = Button(master, text="Add Note", command=display_add_note_section)
add_note_button.pack()

viewNotesButton = Button(master, text="View Notes", command=view_master)
viewNotesButton.pack()

master.mainloop()
