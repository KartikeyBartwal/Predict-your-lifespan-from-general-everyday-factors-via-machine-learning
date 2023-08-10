# The library's are imported
from tkinter import *
import tkinter as tk
import tkvideo
from tkinter import font
from tkinter import ttk
import pickle
import random 
import os

#-----------------------------------------------------------------------------------------------------------------------------------------#
# The backend files used to calculate the age  
current_directory = os.getcwd()
model_frmin=pickle.load(open(current_directory+"\\life expectancy prediction_min.pkl","rb"))
model_frmax=pickle.load(open(current_directory+"\\life expectancy prediction_max.pkl","rb"))


#-----------------------------------------------------------------------------------------------------------------------------------------#
                             ## THE GUI IS CREATED WITH THE HELP FOR TKINTER AND MP4 VIDEO AS A BACKGROUND ##

# The Tkinter Window is Displayed
root=Tk()
width= root.winfo_screenwidth()
height=root.winfo_screenheight()
root.config(bg='Black')

root.geometry("%dx%d" % (width,height)) # window size

# The video is displayed
my_newlabel = Label(root)
my_newlabel.pack()
player = tkvideo.tkvideo(current_directory+"\\animation_3.mp4", my_newlabel, loop = 1, size = (1520,820))
my_newlabel.place(x=0,y=0)#adjust the picture
player.play()



#-------------------------------------------------------------------------------------------------------------------------------------------------------#
            ## THE INPUT BOX AND THE SAVE BUTTON IS CREATED TO TAKE INPUT FROM THE USER AND MOLDIFYING ACCORDING TO THE BACKEND ##
            
# TAKING INPUT OF THE NAME
name = "NAME"
current_age = 18
height = 140
weight = 34
# 1 -> male
gender = 1
financial_situation = 0
workout = 0
general_health = 0
alcohol = 3
smoking = 6
married = 1
never_married = 0
other = 0
diabetic = 2

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
         name=user.get()
         if name=='':
            user.insert(0,"NAME")

user=Entry(root,bg="#6B81E4",fg="black",width=16,font=('',16 , 'bold'))
user.place(x=310,y=218)
user.insert(0,"NAME")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)



# NAME 
def Save():
    global name
    name=user.get()
Button(root ,bg="#A1E2F3", fg="#02647D",text ="save", command=Save,font= "big.TButton",height = 1,width = 4).place (x=540,y =220)



# GENDER
def save():
    global gender
    itm = gender_listbox.get(gender_listbox.curselection())
    print(itm)
    if itm == "MALE":
        itm = 1
        print(itm)
    elif itm == "FEMALE":
        itm = 0
        print(itm)
    gender = itm
    print(itm)

Button(root ,bg="#A1E2F3", fg="#02647D", text ="save",font= "big.TButton", command=save,height = 1,width = 4).place (x=540,y =298)

gender_listbox = Listbox(root)
gender_listbox.insert(END,'MALE')
gender_listbox.insert(END,'FEMALE')
bolded = font.Font(weight='bold')
gender_listbox.config(background="#6B81E4",foreground="black",font=bolded)
gender_listbox.place(x=310,y=298,height=30,width=200)



# AGE 
def save():
    global current_age
    itm = age.get(age.curselection())
    current_age = itm

Button(root ,bg="#60CAD6", fg="#02647D",  text ="save",font= "big.TButton", command=save,height = 1,width = 4).place (x=540,y =375)

age=Listbox(root)
for i in range(18,81):
    age.insert(END,i)
    bolded = font.Font(weight='bold')
age.config(background="#6B81E4",foreground="black",font=bolded)
age.place(x=310,y=375,height=30,width=200)



# WEIGHT 
def save():
    global weight
    itm = weight_listbox.get(weight_listbox.curselection())
    weight = itm
Button(root ,bg="#60CAD6", fg="#02647D",  text ="save", command=save,font= "big.TButton",height = 1,width = 4).place (x=540,y =450)

weight_listbox=Listbox(root)
for i in range(34,181):
    weight_listbox.insert(END,i)
    bolded = font.Font(weight='bold')
weight_listbox.config(background="#6B81E4",foreground="black",font=bolded)
weight_listbox.place(x=310,y=450,height=30,width=200)



# HEIGHT
def save():
    global height
    itm = height_listbox.get(height_listbox.curselection())
    height = itm
Button(root ,bg="#02647D", fg="#A1E2F3", text ="save", command=save,font= "big.TButton",height = 1,width = 4).place (x=540,y =528)

height_listbox=Listbox(root)
for i in range(140,211):
    height_listbox.insert(END,i)
    bolded = font.Font(weight='bold')
height_listbox.config(background="#6B81E4",foreground="black",font=bolded)
height_listbox.place(x=310,y=528,height=30,width=200)



# MARITAL STATUS 
def save():
    global married 
    global never_married
    global other
    itm = marital_sta.get(marital_sta.curselection())
    if itm == "MARRIED":
        married = 1
        never_married = 0
        other = 0
    elif itm == "DIVORCED":
        married = 0
        never_married = 0
        other = 0
    elif itm == "NEVER MARRIED":
        married = 0
        never_married = 1
        other = 0
    elif itm == "OTHER":
        married = 0
        never_married = 0
        other = 1

Button(root ,bg="#02647D", fg="#A1E2F3", text ="save", command=save,font= "big.TButton",height = 1,width = 4).place (x=540,y =610)

marital_sta = Listbox(root)
marital_sta.insert(END,'MARRIED')
marital_sta.insert(END,'DIVORCED')
marital_sta.insert(END,'NEVER MARRIED')
marital_sta.insert(END,'OTHER')
bolded = font.Font(weight='bold')
marital_sta.config(background="#6B81E4",foreground="black",font=bolded)
marital_sta.place(x=310,y=610,height=30,width=200)



# INCOME
def save():
    global financial_situation
    itm = income.get(income.curselection())
    if itm == "Poor":
        itm = 0
    elif itm == "Fair":
        itm = 1
    elif itm == "Good":
        itm = 2
    elif itm == "Excellent":
        itm = 3
    financial_situation = itm
Button(root ,bg="#02647D", fg="#A1E2F3", text ="save", command=save,font= "big.TButton", height = 1,width = 4).place (x=1280,y =220)

income = Listbox(root)
income.insert(END,'Poor')
income.insert(END,'Fair')
income.insert(END,'Good')
income.insert(END,"Excellent")
bolded = font.Font(weight='bold')
income.config(background="#6B81E4",foreground="black",font=bolded)
income.place(x=1050,y=220,height=30,width=200)



# WORKOUT
def save():
    global workout
    itm = exercise.get(exercise.curselection())
    if itm == "NEVER":
        itm = 0
    elif itm == "RARELY":
        itm = 1
    elif itm == "1-2 PER WEEK":
        itm = 2
    elif itm == "3-4 PER WEEK":
        itm = 3
    elif itm == "+5 PER WEEK":
        itm = 4
    workout = itm
Button(root ,bg="#02647D", fg="#A1E2F3", text ="save", command=save,font= "big.TButton", height = 1,width = 4).place (x=1280,y =298)

exercise = Listbox(root)
exercise.insert(END,'NEVER')
exercise.insert(END,'RARELY')
exercise.insert(END,'1-2 PER WEEK')
exercise.insert(END,'3-4 PER WEEK')
exercise.insert(END,'+5 PER WEEK')
bolded = font.Font(weight='bold')
exercise.config(background="#6B81E4",foreground="black",font=bolded)
exercise.place(x=1050,y=298,height=30,width=200)



# GENERAL HEALTH 
def save():
    global general_health
    itm = health.get(health.curselection())
    if itm == "POOR":
        itm = 0
    elif itm == "FAIR":
        itm = 1
    elif itm == "GOOD":
        itm = 2
    elif itm == "VERY GOOD":
        itm = 3
    elif itm == "EXCELLENT":
        itm = 4
    general_health = itm
Button(root ,bg="#60CAD6", fg="#02647D", text ="save", command=save,font= "big.TButton", height = 1,width = 4).place (x=1280,y =375)

health= Listbox(root)
health.insert(END,'POOR')
health.insert(END,'FAIR')
health.insert(END,'GOOD')
health.insert(END,'VERY GOOD')
health.insert(END,'EXCELLENT')
bolded = font.Font(weight='bold')
health.config(background="#6B81E4",foreground="black",font=bolded)
health.place(x=1050,y=375,height=30,width=200)



# DIABETIC
def save():
    global diabetic
    itm = diabetes_listbox.get(diabetes_listbox.curselection())
    if itm == "NO":
        itm = 2
    elif itm == "YES":
        itm = 0
    diabetic = itm
Button(root ,bg="#60CAD6", fg="#02647D",  text ="save", command=save,font= "big.TButton", height = 1,width = 4).place (x=1280,y =450)

diabetes_listbox= Listbox(root)
diabetes_listbox.insert(END,'NO')
diabetes_listbox.insert(END,'YES')
bolded = font.Font(weight='bold')
diabetes_listbox.config(background="#6B81E4",foreground="black",font=bolded)
diabetes_listbox.place(x=1050,y=450,height=30,width=200)



# ALCHOL
def save():
    global alcohol 
    itm = alcohol.get(alcohol.curselection())
    if itm == "DON'T CONSUME":
        itm = 3
    elif itm == "LESS THAN 2 PER WEEK":
        itm = 2
    elif itm == "2-7 PER WEEK":
        itm = 1
    elif itm == "MORE THAN 8 PER WEEK":
        itm = 0   
    alcohol = itm
Button(root ,bg="#A1E2F3", fg="#02647D", text ="save", command=save,font= "big.TButton", height = 1,width = 4).place (x=1280,y =528)

alchol= Listbox(root)
alchol.insert(END,"DON'T CONSUME")
alchol.insert(END,'LESS THAN 2 PER WEEK')
alchol.insert(END,'2-7 PER WEEK')
alchol.insert(END,'MORE THAN 8 PER WEEK')
bolded = font.Font(weight='bold')
alchol.config(background="#6B81E4",foreground="black",font=bolded)
alchol.place(x=1050,y=528,height=30,width=200)



# SMOKING
def save():
    global smoking
    itm = smoking_listbox.get(smoking_listbox.curselection())
    if itm == "NEVER SMOKED":
        itm = 6
    elif itm == 'QUIT THIS YEAR':
        itm = 3
    elif itm == "QUIT 1-9 YEARS AGO":
        itm = 4
    elif itm == "QUIT >10 YEARS AGO":
        itm = 5
    elif itm == "STILL 1/2 PACK":
        itm = 2
    elif itm == "STILL 1 PACK":
        itm = 1
    elif itm == "STILL >2 PACK":
        itm = 0
    smoking = itm

Button(root ,bg="#A1E2F3", fg="#02647D", text ="save", command=save,font= "big.TButton", height = 1,width = 4).place (x=1280,y =610)

smoking_listbox= Listbox(root)
smoking_listbox.insert(END,'NEVER SMOKED')
smoking_listbox.insert(END,'QUIT THIS YEAR')
smoking_listbox.insert(END,'QUIT 1-9 YEARS AGO')
smoking_listbox.insert(END,'QUIT >10 YEARS AGO')
smoking_listbox.insert(END,'STILL 1/2 PACK')
smoking_listbox.insert(END,'STILL 1 PACK')
smoking_listbox.insert(END,'STILL >2 PACK')
bolded = font.Font(weight='bold')
smoking_listbox.config(background="#6B81E4",foreground="black",font=bolded)

smoking_listbox.place(x=1050,y=610,height=30,width=200)



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                ## THE OUTPUT WINDOW IS GENRATED WHICH PRINTS THE AGE AFTER CALCULATING THE LIFE EXPECTENCY USIND THE DATA BASE##
                
# OUTPUT WINDOW
def outputWindow():
       global current_age,height,weight,gender,financial_situation,workout,general_health,alcohol,smoking,married,   never_married,other,diabetic
        
       input_list_obtained.append([current_age, height, weight, gender, financial_situation,
          workout, general_health, alcohol, smoking, married,
          never_married, other, diabetic])

       for val in input_list_obtained[0]:
        print(val,"--->",type(val))

       output_min = max(current_age+2,int(model_frmin.predict(input_list_obtained)))
       output_max = output_min + random.randint(5,7)
       points = int(smoking) + int(workout) + int(general_health) + int(financial_situation) + int(alcohol) + int(diabetic)
       if points > 18:
        output_min += 25
        
       elif points <= 18 and points >= 16:
        output_min += 22
        
       elif (points < 16 and points > 12):
        output_min += 17
        
       elif (points <= 12 and points > 6):
        output_min += 10
       else:
        output_min -= 7
        if output_min < current_age:
            output_min = current_age + 2
       print("output_min",output_min)
       print("output_max",output_min + random.randint(5,7))
       output_max = output_min + random.randint(4,7)
       print("\nYour estimated lifespan: ",output_min,"-",output_max)    
       global name
       
       
       
# NEW WINDOW IS CREATED
       open_window= Tk()
       width= open_window.winfo_screenwidth()
       height=open_window.winfo_screenheight()
       open_window.geometry("%dx%d" % (width,height)) 
       
       
        
# The video is displayed
       my_newlabel_ = Label(open_window)
       my_newlabel_.pack()
       player = tkvideo.tkvideo(current_directory+"\\ending_animation3.mp4", my_newlabel_, loop = 1, size = (width,height-80))
       my_newlabel_.place(x=0,y=0)#adjust the picture
       player.play()
       
       

# Returning the outputs in boxes
       name_text = Text(open_window, height=2, width=30,font=('Times New Roman',40,'bold'))
       name_text.pack()
       name_text.insert(tk.END, name)
       name_text.place(x=260,y=45,height=55,width=250)
       name_text.config(background="#6B81E4",foreground="black",borderwidth=0,state=DISABLED)
 
       prediction_val_range = str(output_min) + "-" + str(output_max) + " Years"
       
       prediction_text = Text(open_window, height=2, width=30,font=('Times New Roman',40,'bold'))
       prediction_text.pack()
       prediction_text.insert(tk.END, prediction_val_range)
       prediction_text.place(x=670,y=114,height=55,width=280)
       prediction_text.config(background="#6B81E4",foreground="black",borderwidth=0,state=DISABLED)
       
       def close():
           open_window.quit()
       Button(open_window ,text ="THANK YOU",height= 1, width = 15,font= ("Handy Casual",20 ,"bold") , command=close).place (x=630,y =660)

       open_window.mainloop()
       
       

input_list_obtained = []
def onSubmitClick():
    
    root.destroy()       
    outputWindow()

Button(root , text ="SUBMIT",height= 1, width = 15,font= ('',20 , 'bold') , command=onSubmitClick).place (x=630,y =707)


root.mainloop() 