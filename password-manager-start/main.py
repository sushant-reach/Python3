from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    passwd=passwd_entry.get()
    if len(website) == 0 or len(email) == 0 or len(passwd) == 0 :
        messagebox.showinfo(title="Oops !", message="Please enter valid data for !!!!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered:\nEmail:{email}"
                                               f"\nPassword:{passwd}\n Is it okay to sva ?" )

        if is_ok:
            with open("pass.cfg","a") as data_file:
                data_file.write(f"{website}|{email}|{passwd}\n")
                website_entry.delete(0,END)
                passwd_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(row=0,column=1)

website_lable = Label(text="Website :")
website_lable.grid(row=1, column=0)

email_lable = Label(text="Email/username :")
email_lable.grid(row=2, column=0)

passwd_lable = Label(text="Password :")
passwd_lable.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"sushant.reach@gmail.com")

passwd_entry = Entry(width=21)
passwd_entry.grid(row=3, column=1)

generate_passwd_button = Button(text = "Generate Password")
generate_passwd_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save,)
add_button.grid(row=4, column=1, columnspan=2)

windows.mainloop()