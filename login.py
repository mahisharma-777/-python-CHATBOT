from tkinter import * 
from PIL import Image,ImageTk
import signup
import os
from tkinter import messagebox
import main_app

filename = 'user_details.txt'

user_details ={}
def load_details():

    if os.path.exists(filename):
        global user_details
        file = open(filename,'r')
        user_details = eval(file.read())
        file.close()
    else:
        messagebox.showwarning("No User Found", "Kindly signup first")


def login_click(username, password):

    if user_details=={}:
        load_details()

    if username != "" and password != "":
    
        if user_details['username']==username and user_details['password']==password:
            messagebox.showinfo("Login Successful", "Welcome to ChatBot")
            root.destroy()
            main_app.my_app_gui()
        else:
            messagebox.showwarning("Login UnSuccessful", "Try again with correct details")

    else:
        messagebox.showerror("Blank Detected", "kindly fill all the details")




def signup_click():
    root.destroy()
    signup.signup_page()
root = Tk()

root.config(bg='black')
root.geometry("1920x1080")
root.title("Login Screen")

img = Image.open('user.png')
img = img.resize((200,200))
user_img = ImageTk.PhotoImage(image=img)

login_label = Label(root,
                    compound=TOP,
                    image=user_img,
                    text = "LOGIN HERE",
                    bg= 'black',
                    fg='white',
                    font=('Arial', 30,'bold'))
login_label.pack()

user_frame = Frame(root, bg='black')
user_frame.pack(pady=30)

user_label = Label(user_frame,
                    text = "Username",
                    bg= 'black',
                    fg='white',
                    font=('Arial', 20,'bold'))
user_label.pack(side=LEFT, padx=40)

user_entry = Entry(user_frame,
                   bg= 'black',
                   fg='white',
                   font=('Arial', 20,'bold'),

                   )

user_entry.pack()

pass_frame = Frame(root, bg='black')
pass_frame.pack()

pass_label = Label(pass_frame,
                    text = "Password",
                    bg= 'black',
                    fg='white',
                    font=('Arial', 20,'bold'))
pass_label.pack(side=LEFT, padx=40)

pass_entry = Entry(pass_frame,
                   bg= 'black',
                   fg='white',
                   font=('Arial', 20,'bold'),
                   show="*"
                   )

pass_entry.pack()


btn_frame = Frame(root, bg='black')
btn_frame.pack(pady=30)

btn_login = Button(btn_frame,
                   text="Login",
                   command=lambda:login_click(user_entry.get(), pass_entry.get()),
                   bg= 'green',
                   fg='white',
                   font=('Arial', 20,'bold'),
                   width=10,
                   bd=4,
                   relief='flat'

                   )
btn_login.pack(side=LEFT,padx=30)

btn_signup = Button(btn_frame,
                   text="Sign Up",
                   command=signup_click,
                   bg= 'red',
                   fg='white',
                   font=('Arial', 20,'bold'),
                   width=10,
                   bd=4,
                   relief='flat'
                   )
btn_signup.pack()
root.mainloop()