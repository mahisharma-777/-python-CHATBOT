from tkinter import *
from tkinter import messagebox

def register_details(username, email, passwd, conf_passwd):

    if username!="" and email!="" and passwd!="" and conf_passwd!="":

        if passwd == conf_passwd:
            file = open("user_details.txt", 'w')
            file.write(str({"username":username, "email":email,"password":passwd}))
            file.close()
            messagebox.showinfo("Registration Successful", "Login Now")
            signup_root.destroy()
            import login
        else:
            messagebox.showwarning("Invalid details","Password doesn't match")
            
    else:
        messagebox.showerror("Blank Detected","Kindly fill all the details to register")

def signup_page():
    global signup_root
    signup_root = Tk()

    signup_root.config(bg='black')
    signup_root.geometry("1920x1080")
    signup_root.title("Signup Screen")

    signup_label = Label(signup_root,
                        compound=TOP,
                        text = "SIGN UP FORM",
                        bg= 'black',
                        fg='white',
                        font=('Arial', 30,'bold'))

    signup_label.pack()

    signup_user_frame = Frame(signup_root, bg='black')
    signup_user_frame.pack(pady=30)

    signup_user_label = Label(signup_user_frame,
                        text = "Username",
                        bg= 'black',
                        fg='white',
                        anchor='w',
                        width=20,
                        font=('Arial', 20,'bold'))
    signup_user_label.pack(side=LEFT, padx=30)

    signup_user_entry = Entry(signup_user_frame,
                    bg= 'black',
                    fg='white',
                    font=('Arial', 20,'bold')
                    )

    signup_user_entry.pack()

    signup_email_frame = Frame(signup_root, bg='black')
    signup_email_frame.pack()

    signup_email_label = Label(signup_email_frame,
                        text = "Email",
                        bg= 'black',
                        fg='white',
                        anchor='w',
                        width=20,
                        font=('Arial', 20,'bold'))
    signup_email_label.pack(side=LEFT, padx=30)

    signup_email_entry = Entry(signup_email_frame,
                    bg= 'black',
                    fg='white',
                    font=('Arial', 20,'bold')
                    )

    signup_email_entry.pack()

    signup_pass_frame = Frame(signup_root, bg='black')
    signup_pass_frame.pack(pady=30)

    signup_pass_label = Label(signup_pass_frame,
                        text = "Password",
                        bg= 'black',
                        fg='white',
                        anchor='w',
                        width=20,
                        font=('Arial', 20,'bold'))
    signup_pass_label.pack(side=LEFT, padx=30)

    signup_pass_entry = Entry(signup_pass_frame,
                    bg= 'black',
                    fg='white',
                    font=('Arial', 20,'bold')
                    )

    signup_pass_entry.pack()

    signup_conf_pass_frame = Frame(signup_root, bg='black')
    signup_conf_pass_frame.pack()

    signup_conf_pass_label = Label(signup_conf_pass_frame,
                        text = "Confirm password",
                        bg= 'black',
                        fg='white',
                        anchor='w',
                        width=20,
                        font=('Arial', 20,'bold'))
    signup_conf_pass_label.pack(side=LEFT, padx=30)

    signup_conf_pass_entry = Entry(signup_conf_pass_frame,
                    bg= 'black',
                    fg='white',
                    font=('Arial', 20,'bold')
                    )

    signup_conf_pass_entry.pack()


    signup_btn_frame = Frame(signup_root, bg='black')
    signup_btn_frame.pack(pady=30)

    signup_btn_register = Button(signup_btn_frame,
                    text="Register",
                    command=lambda:register_details(signup_user_entry.get(),  signup_email_entry.get(), signup_pass_entry.get(),signup_conf_pass_entry.get()),
                    bg= 'green',
                    fg='white',
                    font=('Arial', 20,'bold'),
                    width=10,
                    bd=4,
                    relief='flat'

                    )
    signup_btn_register.pack(side=LEFT,padx=30)


    signup_root.mainloop()