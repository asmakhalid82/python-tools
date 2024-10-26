import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")

# Length Label and Entry
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Password Entry
password_entry = tk.Entry(root, width=50)
password_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
