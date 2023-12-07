import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

def addMyNote():
    frame = ttk.Frame(notebook, padding=10)
    notebook.add(frame, text="Create New Note")

    title_label = ttk.Label(frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
    title_entry = ttk.Entry(frame, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=10)
    content_label = ttk.Label(frame, text='Content:')
    content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
    content_entry = tk.Text(frame, width=40, height=10)
    content_entry.grid(row=1, column=1, padx=10, pady=10)

    def save_note():
        title = title_entry.get()
        content = content_entry.get("1.0", tk.END)

        notes[title] = content.strip()

        with open("notes.json", "w") as f:
            json.dump(notes, f)

        note_content = tk.Text(notebook, width=40, height=10)
        note_content.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(note_content, text=title)

    saveButton = ttk.Button(frame, text="Save!", command=save_note, style="secondary.TButton")
    saveButton.grid(row=2, column=1, padx=10, pady=10)

def loadNotes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)
        for title, content in notes.items():
            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.add(note_content, text=title)
    except FileNotFoundError:
        print("Error occurred. Try again")

def deleteNote():
    currentIndex = notebook.index(notebook.select())
    note_title = notebook.tab(currentIndex, "text")

    confirm = messagebox.askyesno("Delete it!", f"Want to delete {note_title}?")
    if confirm:
        notebook.forget(currentIndex)
        notes.pop(note_title)
        with open("notes.json", "w") as f:
            json.dump(notes, f)

root = tk.Tk()
root.title("Notes App")
root.geometry("500x500")

style = Style(theme='journal')

notebook = ttk.Notebook(root, style="TNotebook")
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

notes = {}
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    print("Error occurred. Try again")

loadNotes()

new_button = ttk.Button(root, text="New Note", command=addMyNote, style="info.TButton")
new_button.pack(padx=10, pady=10, side=tk.LEFT)

delete_button = ttk.Button(root, text="Delete", command=deleteNote, style="primary.TButton")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
