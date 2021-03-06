import json
from tkinter import *
from tkinter import messagebox
from generator import generate
import pyperclip

# import pandas

BG_COLOR = "#dddddd"


# ---------------------------- FIND PASSWORD------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="No Data File Found.")

    else:
        if str(website_entry.get()) in data:
            found_website = data[str(website_entry.get())]
            pyperclip.copy(found_website['password'])
            messagebox.showinfo(title=website_entry.get().upper(),
                                message=f"EMAIL: {found_website['user']} \n\n"
                                        f"PASSWORD: {found_website['password']}\n\n"
                                        f"(Password was copied to clipboard)")
        else:
            messagebox.showwarning(title="WError", message="No details for the website exist.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_strong_password():
    password_entry.delete(0, END)
    strong_password = generate()
    pyperclip.copy(strong_password)
    generate_button.config(text="Copied ", fg="green")
    window.after(1000, lambda: copy_to_clipboard())
    password_entry.insert(0, strong_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    data_entry = {
        str(website_entry.get()): {
            "user": str(user_entry.get()),
            "password": str(password_entry.get()),
        }
    }

    if len(website_entry.get()) == 0 or len(user_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Empty Fields", message="Some fields were left empty")
        return
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"These are the details entered:\n\n"
                                               f"Email: {user_entry.get()} \n"
                                               f"Password: {password_entry.get()}\n\n"
                                               f"Is it OK to save?")

        if not is_ok: return
        elif is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)  # Reading old data

            except FileNotFoundError:
                json_dump(data_entry)

            except json.decoder.JSONDecodeError:
                json_dump(data_entry)

            else:
                data.update(data_entry)
                json_dump(data)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    save_button.config(text="Password Stored ✓", fg="green")

    window.after(1000, lambda: save_button_behaviour())


def json_dump(d):
    with open("data.json", "w") as data_file:
        json.dump(d, data_file, indent=4)


def save_button_behaviour():
    save_button.config(text="SAVE TO FILE  ", fg="black")


def copy_to_clipboard():
    generate_button.config(text="Generate", fg="black")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=BG_COLOR)
window.resizable(False, False)
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BG_COLOR)
lock_img = PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=2, row=1)

website_label = Label(text="Website: ", bg=BG_COLOR)
website_label.grid(column=1, row=2, sticky="e", pady=3)
website_entry = Entry(font=("Arial", 10, "normal"), width=30, highlightthickness=0)
website_entry.focus()
website_entry.grid(column=2, row=2, sticky="w", pady=3)

extra_col = Label(text=" ", bg=BG_COLOR)
extra_col.grid(column=4, row=1, sticky="e", padx=15)

user_label = Label(text="Email/Username: ", bg=BG_COLOR)
user_label.grid(column=1, row=3, sticky="e", pady=3)
user_entry = Entry(font=("Arial", 10, "normal"), width=40, highlightthickness=0)
user_entry.grid(column=2, row=3, columnspan=2, sticky="w", pady=3)
user_entry.insert(0, "luisfernandoca@hotmail.com")

password_label = Label(text="Password: ", bg=BG_COLOR)
password_label.grid(column=1, row=4, sticky="e", pady=3)
password_entry = Entry(font=("Arial", 10, "normal"), width=30, highlightthickness=0)
password_entry.grid(column=2, row=4, sticky="w", pady=3)

search_button = Button(text=" Search", highlightthickness=0, width=8, command=lambda: find_password())
search_button.grid(column=3, row=2, sticky="w", pady=3)

generate_button = Button(text=" Generate", highlightthickness=0, width=8, command=lambda: generate_strong_password())
generate_button.grid(column=3, row=4, sticky="w", pady=3)

save_button = Button(text="SAVE TO FILE ", highlightthickness=0, width=40, command=lambda: save_data())
save_button.grid(column=2, row=5, columnspan=2, sticky="w", pady=3)

window.mainloop()
