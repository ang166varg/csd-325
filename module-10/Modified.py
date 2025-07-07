import tkinter as tk
from tkinter import Menu

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vargas-ToDo")
        self.root.geometry("300x400")

        self.tasks = []

        # Menu
        menu_bar = Menu(self.root, bg='purple', fg='white')  # Menu background
        file_menu = Menu(menu_bar, tearoff=0, bg='gold', fg='black')  # Submenu
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

        # Entry for new task
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)

        # Instruction Label
        self.label = tk.Label(self.root, text="Right-click a task to delete it", bg='mediumPurple1')
        self.label.pack(fill=tk.X)

        # Listbox for tasks
        self.tasks_listbox = tk.Listbox(self.root, height=15, bg='lavender')
        self.tasks_listbox.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.tasks_listbox)
        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tasks_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Right-click to delete
        self.tasks_listbox.bind("<Button-3>", self.delete_task)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_tasks()
            self.task_entry.delete(0, tk.END)

    def delete_task(self, event):
        try:
            index = self.tasks_listbox.nearest(event.y)
            if index >= 0:
                del self.tasks[index]
                self.update_tasks()
        except IndexError:
            pass

    def update_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            if index % 2 == 0:
                self.tasks_listbox.insert(tk.END, task)
                self.tasks_listbox.itemconfig(index, {'bg': 'gold'})
            else:
                self.tasks_listbox.insert(tk.END, task)
                self.tasks_listbox.itemconfig(index, {'bg': 'mediumPurple1', 'fg': 'white'})

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()