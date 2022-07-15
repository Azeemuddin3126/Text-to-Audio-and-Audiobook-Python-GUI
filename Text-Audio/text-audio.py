from cProfile import label
from cgitb import text
from email.mime import image
from operator import imod
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from traceback import format_tb
from turtle import title
import pyttsx3
import os
import pyttsx3
import PyPDF2
from tkinter.filedialog import *





#Pyttsx3 code
engine = pyttsx3.init()
def speaknow():
    text = area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()

    def setvoice():
        if (gender == 'Male'):
                sound = engine.getProperty('voices')
                engine.setProperty('voice',sound[0].id)
                engine.say(text)
                engine.runAndWait()
        else:
                sound = engine.getProperty('voices')
                engine.setProperty('voice',sound[1].id)
                engine.say(text)
                engine.runAndWait()
    setvoice()

    if (text):
        if (speed == 'Fast'):
            engine.setProperty('rate',250)
        elif (speed == "Normal"):
            engine.setProperty('rate',120)
        else:
            engine.setProperty('rate',60)

def download():
    text = area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()

    def setvoice():
        if (gender == 'Male'):
                sound = engine.getProperty('voices')
                engine.setProperty('voice',sound[0].id)
                path = filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'text.mp3')
                engine.runAndWait()
        else:
                sound = engine.getProperty('voices')
                engine.setProperty('voice',sound[1].id)
                path = filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'text.mp3')
                engine.runAndWait()
    setvoice()

    if (text):
        if (speed == 'Fast'):
            engine.setProperty('rate',250)
        elif (speed == "Normal"):
            engine.setProperty('rate',150)
        else:
            engine.setProperty('rate',60)
            


def audiobook():

    book = askopenfilename()
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    for num in range(0, pages):
        page = pdfreader.getPage(num)
        text = page.extractText()
        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()
        
        
    

    
            

    

###############################  GUI  ####################################

root = tk.Tk()
root.title("Text To Speech")
root.geometry("750x350")
root.resizable(False,False)
root.configure(bg="grey")

engine = pyttsx3.init()


#################################  frames #######################################################

#icon
icon = PhotoImage(file="C:\\Users\\murali\\OneDrive\\Desktop\\python projects\\Text-Audio\\images\\speak.png")
root.iconphoto(True,icon)


#Top
top = Frame(root,bg="cyan",width=900,height=100)
top.place(x=0,y=0)
logo = PhotoImage(file="C:\\Users\\murali\\OneDrive\\Desktop\\python projects\\Text-Audio\\images\\speaker logo.png")#speakerlogo
Label(top,image=logo,bg="cyan").place(x=10,y=10)
Label(top,text='TEXT TO SPEECH -by salmaan',font='arial 20 bold',bg='cyan',fg='black').place(x=100,y=40)


############################# Text Frane #################################################

#Text Area
area = Text(root,font='Robote 20',bg='white',relief=GROOVE,wrap=WORD)
area.place(x=10,y=130,width=400,height=180)
Label(root,text='VOICE',font='arial 15 bold',bg='grey',fg='White',).place(x=420,y=120)
Label(root,text='SPEED',font='arial 15 bold',bg='grey',fg='White',).place(x=580,y=120)
Label(root,text='vvv--Enter Text Here--vvv',font='arial 12 bold',bg='grey',fg='White').place(x=20,y=100)


#Gender
gender_combobox = Combobox(root,values=['Male','Female'],font='arial 14',state='r',width=10)
gender_combobox.place(x=420,y=150) 
gender_combobox.set('Male')


#Speed
speed_combobox = Combobox(root,values=['Fast','Normal','Slow'],font='arial 14',state='r',width=10)
speed_combobox.place(x=580,y=150)
speed_combobox.set('Normal')


#Icon1
imageicon = PhotoImage(file="C:\\Users\\murali\\OneDrive\\Desktop\\python projects\\Text-Audio\\images\\speak.png")
btn = Button(root,text="Speak",compound=LEFT,image=imageicon,width=120,height=50,font='arial 14 bold',command=speaknow)
btn.place(x=420,y=230)


#Icon2
imageicon2 = PhotoImage(file="C:\\Users\\murali\\OneDrive\\Desktop\\python projects\\Text-Audio\\images\\download.png")
save = Button(root,text="Save",compound=RIGHT,image=imageicon2,width=120,height=50,font='arial 14 bold',command=download)
save.place(x=580,y=230)


#Audiobook
ab = Button(root,text="🎵Audiobook🎵",fg='grey',width=13,height=2,font='arial 14 bold',command=audiobook)
ab.place(x=480,y=289)



    
    
    
    
    
    
    

root.mainloop()