from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #





# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    password = input_password.get()
    email = input_email.get()

    is_ok =  messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                      f"\nPassword: {password}\nIs it ok?")

    if is_ok:
        with open('data.txt', 'a') as file:
            file.write(f"{website} | {password} | {email}\n")


            website_input.delete(0, END)
            input_password.delete(0, END)










# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, background="White", highlightthickness=0)
lock = PhotoImage(file='logo - Copy.png')
canvas.create_image(100, 112, image=lock)
canvas.grid(column=2, row=0)

website = Label(text="Website:")
website.grid(column=1, row=5)

website_input = Entry(width=35)
website_input.grid(row=5, column=2, columnspan=2)
website_input.focus()

email = Label(text="Email/Username:")
email.grid(column=1, row=6)

input_email = Entry(width=35)
input_email.grid(row=6, column=2)
input_email.insert(0, "sharim@gmail.com")

password = Label(text="Password:")
password.grid(column=1, row=7)

input_password = Entry(width=21)
input_password.grid(row=7, column=2)

gen_password = Button(text="Generate Password", )
gen_password.grid(row=7, column=3)

Add = Button(text='Add', width=36, command=save)
Add.grid(row=8, column=2, columnspan=2)

window.mainloop()