from tkinter import *
# import pandas
import pandas

BG_COLOR = "#dddddd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    data_entry = {
        "Website": f"{website_entry.get()}",
        "User": f"{user_entry.get()}",
        "Password": f"{password_entry.get()}"
    }
    # data_df = pandas.DataFrame([data_entry])

    with open("data_test.txt", "a") as f:
        f.write(f"{str(data_entry)}\n")
        # f.write(str(data_df))

    website_entry.delete(0, END)
    # user_entry.delete(0, END)
    password_entry.delete(0, END)
    save_button.config(text="Password Stored", fg="green")

    window.after(1000, lambda: save_button_behaviour())


def save_button_behaviour():
    save_button.config(text="Save", fg="black")


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
website_entry = Entry(font=("Arial", 10, "normal"), width=40, highlightthickness=0)
website_entry.focus()
website_entry.grid(column=2, row=2, columnspan=2, sticky="w", pady=3)

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

generate_button = Button(text="Generate ", highlightthickness=0, width=8)
generate_button.grid(column=3, row=4, sticky="w", pady=3)

save_button = Button(text="Save", highlightthickness=0, width=40, command=lambda: save_data())
save_button.grid(column=2, row=5, columnspan=2, sticky="w", pady=3)


window.mainloop()
