import tkinter as tk
import random
import string

def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            password_label.config(text="Please enter a valid length")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_label.config(text="Generated Password: " + password)
    except ValueError:
        password_label.config(text="Please enter a valid number")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create a label and entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Create a button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Create a label to display generated password
password_label = tk.Label(window, text="")
password_label.pack()

# Start the GUI event loop
window.mainloop()