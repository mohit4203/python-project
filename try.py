import tkinter as tk
from tkinter import*
# from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
import index

root=Tk()
root.title("text to speed")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#305065")

# image_icon=PhotoImage(file='')
# root.iconphoto(False,image_icon)

# top frame

engin=pyttsx3.init()

def speak():
    text=text_area.get("1.0",END).strip()
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voice=engin.getProperty("voice",)
    
    def setvoice():
     if(gender=="Male"):
      engin.setProperty("voice","1")
      engin.say(text)
      engin.runAndWait()
            
     else:
        engin.setProperty("voice","512")
        engin.say(text)
        engin.runAndWait()
            
            
    if(text):
        if(speed=="Fast"):
         engin.setProperty("rate",250)
         setvoice()
        elif(speed=="Normal"):
         engin.setProperty("rate",150)
         setvoice()
        else:
         engin.setProperty("rate",60)
         setvoice()
      
def download():
 print()
#  import index


top_frame=Frame(root,bg="#39c790",width=900,height=100)
top_frame.place(x=0,y=0)

logo=PhotoImage(file="")
Label(top_frame,image=logo, bg='white').place(x=10,y=5)

Label(top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="#39c790",fg="black").place(x=100,y=30)
text_area=Text(root,font="robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="Voice",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="Speed",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)

gender_combobox=Combobox(root,value=["Male",],font="arial 14",state="r",width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,value=["Fast","Slow","Normal"],font="arial 14",state="r",width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

btn=Button(root,text="speak",width=10,font="arial 14 bold")
btn.place(x=550,y=280)
#
imageicon=PhotoImage(file="")
btn=Button(root,text="speak",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",command=speak)
btn.place(x=550,y=280)

imageicon2=PhotoImage(file="")
save=Button(root,text="Download",compound=LEFT,image=imageicon2, bg="#39c790" ,width=130,font="arial 14 bold",command=download)
save.place(x=730,y=280)


#


root.mainloop()