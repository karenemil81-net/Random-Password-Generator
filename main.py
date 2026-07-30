import secrets
import string
import pyperclip
from tkinter import *


history = []

def get_character_sets():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?"

    if exclude_var.get():
        ambiguous = "O0Il1"
        uppercase = "".join(c for c in uppercase if c not in ambiguous)
        lowercase = "".join(c for c in lowercase if c not in ambiguous)
        numbers = "".join(c for c in numbers if c not in ambiguous)

    return uppercase, lowercase, numbers, symbols


def password_strength(password):
    score = 0
    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Weak",fg="red")
    elif score <= 4:
        strength_label.config(text="Medium",fg="orange")
    else:
        strength_label.config(text="Strong",fg="green")


def generate_password():
    try:
        length = int(length_box.get())
    except ValueError:
        message_label.config(text="Invalid length")
        return

    if length < 8:
        message_label.config(text="Minimum password length is 8 characters")
        return

    uppercase, lowercase, numbers, symbols = get_character_sets()
    selected = []

    if upper_var.get():
        selected.append(uppercase)

    if lower_var.get():
        selected.append(lowercase)

    if number_var.get():
        selected.append(numbers)

    if symbol_var.get():
        selected.append(symbols)

    if len(selected) < 2:
        message_label.config(text="Select at least 2 character types")
        return

    password = []

    for group in selected:
        password.append(secrets.choice(group))

    all_characters = "".join(selected)

    while len(password) < length:
        password.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password)
    password = "".join(password)
    message_label.config(text="")
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)
    password_strength(password)
    history.append(password)

    if len(history) > 5:
        history.pop(0)

    history_box.delete(0, END)

    for item in history:
        history_box.insert(END,item)


def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)

def show_or_hide():

    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        show_button.config(text="Show")

    else:
        password_entry.config(show="")
        show_button.config(text="Hide")


def clear_password():
    password_entry.delete(0, END)
    message_label.config(text="")
    strength_label.config(text="Not Generated",fg="black")

def reset():
    length_box.delete(0, END)
    length_box.insert(0, 12)
    upper_var.set(True)
    lower_var.set(True)
    number_var.set(True)
    symbol_var.set(True)
    exclude_var.set(False)
    password_entry.delete(0, END)
    strength_label.config(text="Not Generated",fg="black")
    message_label.config(text="")
    history.clear()
    history_box.delete(0, END)


window = Tk()
window.title("Random Password Generator")
window.geometry("650x600")
window.configure(bg="#EEF2F7")
window.resizable(False,False)


title = Label(window,text="Random Password Generator",font=("Segoe UI",20,"bold"),bg="#EEF2F7",fg="#1E3A5F")
title.pack(pady=15)


password_frame = Frame(window,bg="#EEF2F7")
password_frame.pack(pady=10)


password_entry = Entry(password_frame,width=35,font=("Consolas",13),show="*")
password_entry.grid(row=0,column=0,padx=5) 

message_label = Label(window,text="",bg="#EEF2F7",fg="red",font=("Segoe UI", 10, "bold"))
message_label.pack()

Button(
    password_frame,
    text="Generate",
    command=generate_password,
    bg="#3498DB",
    fg="white"
).grid(row=0,column=1,padx=5)

Button(
    password_frame,
    text="Copy",
    command=copy_password,
    bg="#2ECC71",
    fg="white"
).grid(row=0,column=2,padx=5)

show_button = Button(
    password_frame,
    text="Show",
    command=show_or_hide,
    bg="#9B59B6",
    fg="white"
)
show_button.grid(row=0,column=3,padx=5)


length_frame = LabelFrame(window,text="Password Length",bg="#EEF2F7",padx=20,pady=10)
length_frame.pack(pady=10)


length_box = Spinbox(length_frame,from_=8,to=128,width=10)
length_box.delete(0, END)
length_box.insert(0, 12)
length_box.pack()


options = LabelFrame(window,text="Character Types",bg="#EEF2F7",padx=20,pady=10)
options.pack(pady=10)


upper_var = BooleanVar(value=True)
lower_var = BooleanVar(value=True)
number_var = BooleanVar(value=True)
symbol_var = BooleanVar(value=True)
exclude_var = BooleanVar()

Checkbutton(options,text="Uppercase",variable=upper_var,bg="#EEF2F7").grid(row=0,column=0)
Checkbutton(options,text="Lowercase",variable=lower_var,bg="#EEF2F7").grid(row=0,column=1)
Checkbutton(options,text="Numbers",variable=number_var,bg="#EEF2F7").grid(row=1,column=0)
Checkbutton(options,text="Symbols",variable=symbol_var,bg="#EEF2F7").grid(row=1,column=1)
Checkbutton(options,text="Exclude ambiguous characters",variable=exclude_var,bg="#EEF2F7").grid(row=2,columnspan=2)


Label(window,text="Password Strength:",bg="#EEF2F7",font=("Segoe UI",11)).pack()
strength_label = Label(window,text="Not Generated",bg="#EEF2F7",font=("Segoe UI",11,"bold"))
strength_label.pack()


history_frame = LabelFrame(window,text="Last 5 Generated Passwords",bg="#EEF2F7")
history_frame.pack(pady=10)


history_box = Listbox(history_frame,width=45,height=5)
history_box.pack()


Button(window,text="Clear",command=clear_password,width=12).pack(side=LEFT,padx=20,pady=10)
Button(window,text="Reset",command=reset,width=12).pack(side=RIGHT,padx=20,pady=10)


window.mainloop()