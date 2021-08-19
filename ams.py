#AMS--1

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
from typing import Sized 

# def Database():
#  global conn,cursor
#  #creating student database
#  conn = sqlite3.connect("ad.db")
#  cursor = conn.cursor()
#  #creating ad management system table
#  cursor.execute(""""
#  CREATE TABLE IF NOT EXISTS AD_MANAGE (
#   SL.NO. INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#   DISTRICT TEXT,
#   TOWN TEXT,
#   LOCATION TEXT,
#   SIZE TEXT,
#   SQFEET TEXT,
#   RATE INTEGER,
#   PERIOD TEXT,
#   AVAILIABILITY TEXT)
#  """)

def DisplayForm():
 #creating window
 global display_screen
 display_screen = Tk()

 # setting width and height for window
 # display_screen.geometry("{0}x{1}+0+0".format(display_screen.winfo_screenwidth(), display_screen.winfo_screenheight()))
 display_screen.geometry("1280x720")
 display_screen.resizable(width=0, height=0)

 #setting title for window
 display_screen.title("AMS")

 #declaring variables
 global district,town,location,size,sqfeet,rate,period,availability
 district = StringVar()
 town = StringVar()
 location = StringVar()
 size = StringVar()
 sqfeet = StringVar()
 rate = IntVar()
 period = StringVar()
 availability = StringVar()
 #creating frames for layout

 #frame for the heading
 HeadingForm = Frame(display_screen,bd=1,relief=SOLID)
 HeadingForm.pack(side=TOP,fill=X)
 
 #first left frame for the registration 
 LForm = Frame(display_screen,width=280)
 LForm.pack(side=LEFT,fill=Y)
 #mid frame for displaying students record
 MidViewForm = Frame(display_screen, width="1000",bg="gray")
 MidViewForm.pack(side=RIGHT,fill=Y)

 #label for heading
 lbl_text = Label(HeadingForm, text="Advertisement Management System", font=('verdana', 22),width=600,bg="#e6c68c",fg="#5b29ab")
 lbl_text.pack()
 #creating the insert form in the LForm

 ID = Label(LForm,text="Insert Data",font = ('verdana',15),height=4)
 ID.grid(row=0,column=0,columnspan=2,sticky=" ")

 Label(LForm, text="District", font=("Arial", 12)).grid(row=1,column=0,pady=5)
 Entry(LForm,font=("Arial",10,"bold"),textvariable=district).grid(row=2,column=0,padx= 30)

 Label(LForm, text="Town ", font=("Arial", 12)).grid(row=1,column=1,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=town).grid(row=2,column=1,padx= 30,pady=20)

 Label(LForm, text="Location ", font=("Arial", 12)).grid(row=3,column=0,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=location).grid(row=4,column=0,padx= 30,pady=20)

 Label(LForm, text="Size", font=("Arial", 12)).grid(row=3,column=1,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=size).grid(row=4,column=1,padx= 30,pady=20)

 Label(LForm, text="Sq.Feet ", font=("Arial", 12)).grid(row=5,column=0,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=sqfeet).grid(row=6,column=0,padx= 30,pady=20)
 
 Label(LForm, text="Rate ", font=("Arial", 12)).grid(row=5,column=1,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=rate).grid(row=6,column=1,padx= 30,pady=20)

 Label(LForm, text="Period", font=("Arial", 12)).grid(row=7,column=0,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=period).grid(row=8,column=0,padx= 30,pady=20)

 Label(LForm, text="Availability", font=("Arial", 12)).grid(row=7,column=1,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=availability).grid(row=8,column=1,pady=5)

 Button(LForm,text="Submit",font=("Arial", 10, "bold"),width=30).grid(row=9,column=0,columnspan=2,padx=20,pady=20)

DisplayForm()
display_screen.mainloop()
#Hi I am Soumyajit

 
