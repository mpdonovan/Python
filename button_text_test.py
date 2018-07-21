#!/usr/bin/python

#This allows the text of the button to be used in a function
from Tkinter import *
class GraphicsInterface:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("720x500")

        self.clicked=[]
        button1 = Button(self.window, text="Dice 1", width=13)
        button2 = Button(self.window, text="Dice 2", width=13)
        button1.pack()
        button2.pack()

        button1.configure(command=lambda btn=button1: self.OnClick(btn))
        button2.configure(command=lambda btn=button2: self.OnClick(btn))

        self.window.mainloop()

    def OnClick(self, btn):
        text = btn.cget("text")
        self.clicked.append(text)
        print "clicked:", self.clicked

app = GraphicsInterface()
