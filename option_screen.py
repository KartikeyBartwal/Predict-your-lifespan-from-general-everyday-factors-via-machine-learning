#Import tkinter library
from tkinter import *
from tkinter import ttk
import tkvideo
import os
import pygame



#Set the geometry of tkinter frame
win=Tk()
width= win.winfo_screenwidth()
height=win.winfo_screenheight()
win.config(bg='Black')

win.geometry("%dx%d" % (width,height))#window size

current_directory = os.getcwd()
my_newlabel = Label(win)
my_newlabel.pack()
player = tkvideo.tkvideo(current_directory+"\\main_animation.mp4", my_newlabel, loop = 1, size = (1520,820))
my_newlabel.place(x=0,y=0)#adjust the picture
player.play()

# Playing the background music and other sound effects
pygame.mixer.init()

def playbgm():
    pygame.mixer.music.load(current_directory +"\\healthcare bgm.mp3")
    pygame.mixer.music.play(loops = 15)
playbgm()

#Define a new function to open the window
def open_win1():
   os.startfile(current_directory+'\\main_project1.pyw')
   # win.destroy()
   
def open_win2():
   os.startfile(current_directory+'\\main_project2.pyw')
   # win.destroy()
   
def open_win3():
   os.startfile(current_directory+'\\main_project3.pyw')
   # win.destroy()
   
def open_win4():
   os.startfile(current_directory+'\\main_project4.pyw')
   # win.destroy()
   
   
#Create a button to open a New Window
Button(win,bg= "#4458BE",text="Open1", command=open_win1,height = 1,width = 27).place(x=223,y=410)
Button(win,bg="#077010" ,text="Open2", command=open_win2,height = 1,width = 27).place(x=1110,y=410)
Button(win,bg="#5FC1DB", text="Open3", command=open_win3,height = 1,width = 27).place(x=223, y=734)
Button(win,bg="#A2223D", text="Open4", command=open_win4,height = 1,width = 27).place(x=1110,y=734)


win.mainloop()