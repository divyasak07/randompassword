
import secrets
import string
import tkinter as tk
from tkinter import messagebox

# Character sets
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 8 or length > 128:
            messagebox.showwarning(
                "Invalid Length",
                "Choose a length between 8 and 128."
            )
            return

        characters = LOWER + UPPER + DIGITS + SYMBOLS

        password = ''.join(
            secrets.choice(characters) for _ in range(length)
        )

        password_output.config(state="normal")
        password_output.delete(0, tk.END)
        password_output.insert(0, password)
        password_output.config(state="readonly")

        check_strength(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")

def check_strength(password):
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in SYMBOLS for c in password):
        score += 1

    if len(password) >= 16 and score == 4:
        strength_label.config(
            text="Strength: Strong",
            fg="green"
        )
    elif len(password) >= 12 and score >= 3:
        strength_label.config(
            text="Strength: Good",
            fg="blue"
        )
    else:
        strength_label.config(
            text="Strength: Moderate",
            fg="orange"
        )

def copy_password():
    password = password_output.get()

    if not password:
        messagebox.showwarning(
            "Empty",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )

# Main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("450x350")
root.resizable(False, False)
root.configure(bg="#1e293b")

# Title
title_label = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 18, "bold"),
    bg="#1e293b",
    fg="white"
)
title_label.pack(pady=20)

# Password length
length_label = tk.Label(
    root,
    text="Enter password length (8-128):",
    font=("Arial", 11),
    bg="#1e293b",
    fg="white"
)
length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center"
)
length_entry.insert(0, "16")
length_entry.pack(pady=10)

# Generate button
generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12, "bold"),
    bg="#38bdf8",
    fg="black",
    padx=10,
    pady=5
)
generate_button.pack(pady=10)

# Password output
password_output = tk.Entry(
    root,
    font=("Consolas", 12),
    width=35,
    justify="center",
    state="readonly"
)
password_output.pack(pady=10)

# Strength indicator
strength_label = tk.Label(
    root,
    text="Strength: Waiting",
    font=("Arial", 11, "bold"),
    bg="#1e293b",
    fg="white"
)
strength_label.pack(pady=5)

# Copy button
copy_button = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 11),
    bg="#86efac",
    padx=10,
    pady=5
)
copy_button.pack(pady=10)

# Footer
footer = tk.Label(
    root,
    text="Created with Python",
    bg="#1e293b",
    fg="gray",
    font=("Arial", 9)
)
footer.pack(side="bottom", pady=10)

root.mainloop()