from tkinter import *
from PIL import ImageTk,Image

#opening the dictionary data, the jason file
#as it is a json file, we have to import json module inoder to access it
import json
data=json.load(open("data/data.json"))

win=Tk()
win.title("Simple Dictionary")
win.geometry("600x600+750+250")
win.iconbitmap("images/dicticon.ico")
# add image to the window\
myimg=ImageTk.PhotoImage(Image.open("images/binocular.png"))
myimglabel=Label(image=myimg)
myimglabel.place(x=170,y=70)
def findword():
    getword=word.get()

    win2=Tk()
    win2.title("Output")
    win2.geometry("500x500+800+300")
    win2.iconbitmap("images/dicticon.ico")


    try:
        meaning=data[getword]
        display1=Label(win2,text="Output:",font=("arial",15,"bold"),bg="white",fg="black")
        display1.pack()          
        for i in meaning:
            display=Label(win2,text=i,font=("arial",10,"bold"),bg="white",fg="black")
            display.pack()  
    except:
        display2=Label(win2,text="ERROR!",font=("arial",20,"bold"),bg="white",fg="black")
        display2.pack()  
        display=Label(win2,text="Unable to find the meaning of the word:(",font=("arial",10,"bold"),bg="white",fg="black")
        display.pack()
        display1=Label(win2,text="Please check whether you have given a valid word!",font=("arial",10,"bold"),bg="white",fg="black")
        display1.pack()
    win2.mainloop()


#heading
heading=Label(win,text="Wanna test me? Give me some word.I will tell you the meaning in no time!",font=("arial",10,"bold"))
heading.place(x=50,y=30)
#space for entering the word
word=Entry(win,textvar=StringVar())
word.place(x=200,y=300)
#search button
sbutton=Button(win,text="Search",font=("arial",10,"bold"),fg="white",bg="grey",command=findword)
sbutton.place(x=330,y=295)

#developed by
dby=Label(win,text="Developed by:Anandhu S",font=("arial",13,"bold"))
dby.place(x=390,y=520)
dby1=Label(win,text="As the project is under development stage, if a situation arises where you entered a valid word\n and it is showing ERROR!, then please mail us with the word to:\n aforprogramming@gmail.com")
dby1.place(x=10,y=550)
win.mainloop()
