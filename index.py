from tkinter import *
import tkinter as tk
# from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

# Create the main window
window = Tk()
window.title("Login and Signup Page")
window.geometry('1000x500+500+200')
window.configure(bg='#fff')
window.resizable(False,False)



def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "password":
        status_label.config(text="Login Successful!", fg="green")
    else:
        status_label.config(text="Login Failed!", fg="red")

#56788765798765433456789
# def login():
    
    
    
    
    
    
    
    



#123456789987654321234567890987654321234567898765432

def signup():
    username = username_entry.get()
    password = password_entry.get()
    
    # Here, you can write the code to save the username and password to a file or database
    # For simplicity, we are just printing them here
    print("Signup successful!")
    print("Username:", username)
    print("Password:", password)




img=PhotoImage(file='mahi.png')
map=Label(window,image=img,border=0,bg='white').place(x=50,y=90)
frame=Frame(window,width=350,height=390,bg='white')
frame.place(x=600,y=120)
heading=Label(frame,text='LogIn/SignUp',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

# Create the username label and entry
username_label = Label(window, text="Username:" ,bg="white")
username_label.place(x=580,y=200)
username_entry = Entry(window)
# username_entry.insert(0,"Username")
username_entry.place(x=750,y=200)

# Create the password label and entry
password_label = Label(window, text="Password:",bg="white")
password_label.place(x=580,y=250)
password_entry = Entry(window, show="")
# password_entry.insert(0,"Password")
password_entry.place(x=750,y=250)

# Create the login button
login_button = Button(window, text="Login", command=login,bg="white",fg="red")
login_button.place(x=760,y=350)

# Create the signup button
signup_button = Button(window, text="Signup", command=signup,bg="white",fg="red")
signup_button.place(x=810,y=350)

# Create the status label
status_label = Label(window, text="", bg="white")
status_label.place(x=770,y=310)

# Start the main loop
window.mainloop()