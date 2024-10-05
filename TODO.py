# Task List Using Python

import tkinter as tk
import sqlite3 as db
from tkinter import messagebox

class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("TO DO List")
        self.master.geometry("500x450")
        self.master.resizable(False, False)

        self.tasks = []
        self.db_conn = db.connect('tasks.db')
        self.db_cursor = self.db_conn.cursor()
        self.db_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (task TEXT)')

        self.header_frame = tk.Frame(self.master, bg="#455A64")
        self.controls_frame = tk.Frame(self.master, bg="#F7F7F7")
        self.list_frame = tk.Frame(self.master, bg="#455A64")

        self.header_frame.pack(fill="both")
        self.controls_frame.pack(side="left", expand=True, fill="both")
        self.list_frame.pack(side="right", expand=True, fill="both")

        self.header_label = tk.Label(self.header_frame, text="TO DO List", font=("Segoe UI", "24", "bold"), bg="#455A64", fg="#FFFFFF")
        self.header_label.pack(padx=20, pady=20)

        self.task_label = tk.Label(self.controls_frame, text="Enter Task:", font=("Segoe UI", "14"), bg="#F7F7F7", fg="#333333")
        self.task_label.place(x=30, y=40)

        self.task_entry = tk.Entry(self.controls_frame, font=("Segoe UI", "14"), width=18, bg="#FFFFFF", fg="#333333")
        self.task_entry.place(x=30, y=80)

        self.add_button = tk.Button(self.controls_frame, text="Add Task", width=24, command=self.add_task, bg="#4CAF50", fg="#FFFFFF")
        self.add_button.place(x=30, y=120)

        self.delete_button = tk.Button(self.controls_frame, text="Delete Task", width=24, command=self.delete_task, bg="#E74C3C", fg="#FFFFFF")
        self.delete_button.place(x=30, y=160)

        self.clear_button = tk.Button(self.controls_frame, text="Clear All Tasks", width=24, command=self.clear_tasks, bg="#E74C3C", fg="#FFFFFF")
        self.clear_button.place(x=30, y=200)

        self.exit_button = tk.Button(self.controls_frame, text="Exit", width=24, command=self.close, bg="#4CAF50", fg="#FFFFFF")
        self.exit_button.place(x=30, y=240)

        self.task_list = tk.Listbox(self.list_frame, width=26, height=13, selectmode='SINGLE', bg="#FFFFFF", fg="#333333", selectbackground="#4CAF50", selectforeground="#FFFFFF")
        self.task_list.place(x=10, y=20)

        self.load_tasks()
        self.update_list()

    def add_task(self):
        task = self.task_entry.get()
        if not task:
            messagebox.showinfo('Error', 'Field is empty.')
        else:
            self.tasks.append(task)
            self.db_cursor.execute('INSERT INTO tasks VALUES (?)', (task,))
            self.update_list()
            self.task_entry.delete(0, 'end')

    def delete_task(self):
        try:
            task = self.task_list.get(self.task_list.curselection())
            if task in self.tasks:
                self.tasks.remove(task)
                self.update_list()
                self.db_cursor.execute('DELETE FROM tasks WHERE task = ?', (task,))
        except:
            messagebox.showinfo('Error', 'No task selected.')

    def clear_tasks(self):
        if messagebox.askyesno('Clear All', 'Are you sure?'):
            self.tasks.clear()
            self.db_cursor.execute('DELETE FROM tasks')
            self.update_list()

    def update_list(self):
        self.task_list.delete(0, 'end')
        for task in self.tasks:
            self.task_list.insert('end', task)

    def load_tasks(self):
        self.tasks.clear()
        for row in self.db_cursor.execute('SELECT task FROM tasks'):
            self.tasks.append(row[0])

    def close(self):
        print(self.tasks)
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
    app.db_conn.commit()
    app.db_cursor.close()