from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #


# creating window by using Tk()
window = Tk()

# giving title to on window screen
window.title("Password manager")
window.config(padx=20, pady=20)

# creating a canvas to hold an image
canvas = Canvas(width=200, height=200)

# holding an image
image = PhotoImage(file="logo.png")

# create image
canvas.create_image(100, 100, image=image)
# canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
canvas.grid(row=0, column=1)
# canvas.pack()

# using label to print Website on screen
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

# create an Entry to store the name of website
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1)

# using label to print eamil/usernamee on screen
email_label = Label(text="Email/UserName:")
email_label.grid(column=0, row=2)

# create an Entry to store the name of website
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2)

 # create Pasword label to display pasword on screen

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# creating a label of Password_entry to store a password
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

# create generate password from Button to auto generate password
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

# create add button from Button class
add_button = Button(text="Add", width=33)
add_button.grid(column=1, row=4)
window.mainloop()
