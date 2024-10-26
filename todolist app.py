import tkinter as tk

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_label = tk.Label(root, text="", justify="left")
        self.tasks_label.pack(pady=10)

        self.clear_button = tk.Button(root, text="Clear Tasks", command=self.clear_tasks)
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks()
            self.task_entry.delete(0, tk.END)

    def clear_tasks(self):
        self.tasks.clear()
        self.update_tasks()

    def update_tasks(self):
        self.tasks_label.config(text="\n".join(self.tasks) if self.tasks else "No tasks added.")

root = tk.Tk()
todo_app = ToDoList(root)
root.mainloop()
