from tkinter import *
from tkinter import messagebox
import random
import pyperclip

all_fill = None


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letter = [random.choice(letters) for _ in range(0, 3)]

    password_number = [random.choice(numbers) for _ in range(0, 3)]

    password_symbol = [random.choice(symbols) for _ in range(0, 3)]

    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)

    string_pas = "".join(password_list)

    print(f"Your password is: {string_pas}")

    password_entry.insert(END, string_pas)
    pyperclip.copy(string_pas)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# defining a data function to collect data from user and create a file and use in Add Button Command
def data():
    global all_fill
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # check if the user don fill all entry than a Warn message appear
    if len(web) <= 0 or len(password) <= 0:

        messagebox.showinfo(title="Something missing", message="Please fill all the entries  ")
    else:
        # print message Box to make sure user ok to add data
        it_ok = messagebox.askokcancel(title="Data", message=f" The website you entered: {web} "
                                                             f"and the Password you entered:"
                                                             f" {password} is ok ?")
        if it_ok:
            with open("./Passwords.txt", "a") as pas:
                pas.write(f"{web}||  {email}||  {password}\n")
                # applying to delete function that delete  the entry data man make it clear for ready to another data
                web_entry.delete(0, END)
                password_entry.delete(0, END)


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
canvas.grid(row=0, column=1)
# canvas.pack()

# using label to print Website on screen
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

# create an Entry to store the name of website
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1)

# add functionality to Make focus on box
web_entry.focus()

# using label to print email /user_name on screen
email_label = Label(text="Email/UserName:")
email_label.grid(column=0, row=2)

# create an Entry to store the name of website
email_entry = Entry(width=35)
# add some email text for improvig UI exp
email_entry.insert(END, "uzii@gmail.com")
email_entry.grid(column=1, row=2)

# create Password label to display password on screen

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# creating a label of Password_entry to store a password
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

# create generate password from Button to auto generate password
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# create add button from Button class
add_button = Button(text="Add", width=33, command=data)
add_button.grid(column=1, row=4)
window.mainloop()
