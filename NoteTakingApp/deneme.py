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
label=Label(master,text="THIS IS MAIN WINDOW")
label.pack(pady=10)


# Adding a button to view saved notes
def view_notes(id):
    mycursor.execute(f"SELECT * FROM notes WHERE id={id}")
    myresult = mycursor.fetchall()
    for x in myresult:
        pass
    newWindow = Toplevel(master)
    newWindow.title(x[1])
    newWindow.geometry("300x300")
    # note
    Label(newWindow, text=x[3], wraplength=200).pack()

    # Delete Note
    def delete_note(id):
        query = "DELETE FROM notes WHERE id = %s"
        mycursor.execute(query, (id,))
        mydb.commit()
        newWindow.destroy()

    delete_button = Button(newWindow, text="Delete", command=lambda x = id: delete_note(x))
    delete_button.pack()

    # Buttons to see titles of notes
mycursor.execute("SELECT * FROM notes")
myresult = mycursor.fetchall()
for x in myresult:
    btn = Button(master, text =f"{x[1]} | Category : {x[2]}",  command=lambda id=x[0]: view_notes(id)) # lambda function creates an anonymous function that takes the value of x[0] at the moment the button is created and then passes it to view_notes when the button is clicked.
    btn.pack(pady = 10)

# Create a function to display the Add Note section
def display_add_note_section():
    add_note_window = Toplevel(master)
    add_note_window.title("Add Note")
    add_note_window.geometry("300x300")

    # Title Entry
    Label(add_note_window, text="Title:").pack()
    title_entry = Entry(add_note_window)
    title_entry.pack()

    # Category Entry
    Label(add_note_window, text="Category:").pack()
    category_entry = Entry(add_note_window)
    category_entry.pack()

    # Content Entry (use a Text widget for multi-line input)
    Label(add_note_window, text="Content:").pack()
    content_entry = Text(add_note_window, height=10, width=30)
    content_entry.pack()

    # Add Note Button
    add_button = Button(add_note_window, text="Save!",  command=lambda: add_note(title_entry.get(), content_entry.get("1.0", END), category_entry.get()))
    add_button.pack()

def add_note(title, content, category):
    today = date.today()
    print("Title:", title)
    print("Category:", category)
    print("Content:", content)
    print(today)
    # Insert the new note into the database
    mycursor.execute("INSERT INTO notes (Title, Category, Context, Date) VALUES (%s, %s, %s, %s)", (title, category, content, today))
    mydb.commit()
    # Clear the entry fields after adding the note

add_note_button = Button(master, text="Add Note", command=display_add_note_section)
add_note_button.pack()


# Run the application
master.mainloop()

