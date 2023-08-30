import tkinter as tk
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def submit_task():
    add_task()
    task_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Add a heading box with color
heading_frame = tk.Frame(window, bg="#3498db", padx=10, pady=10)
heading_frame.pack(fill="x")

heading_label = tk.Label(heading_frame, text="To-Do List", font=("Helvetica", 16), fg="white", bg="#3498db")
heading_label.pack()

# Create an entry and buttons for tasks
task_entry = tk.Entry(window)
task_entry.pack()

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

submit_button = tk.Button(window, text="Submit Task", command=submit_task)
submit_button.pack()

remove_button = tk.Button(window, text="Remove Task", command=remove_task)
remove_button.pack()

# Create a listbox to display tasks
tasks_listbox = tk.Listbox(window)
tasks_listbox.pack()

# Add colored borders
frame = tk.Frame(window, relief="ridge", borderwidth=2)
frame.pack(padx=10, pady=10, fill="both", expand="true")

# Start the GUI event loop
window.mainloop()