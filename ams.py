#AMS--1

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
from typing import Sized
from PIL import ImageTk, Image

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
 global district,town,location,size,sqfeet,rate,period,availability,search
 district = StringVar()
 town = StringVar()
 location = StringVar()
 size = StringVar()
 sqfeet = StringVar()
 rate = IntVar()
 period = StringVar()
 availability = StringVar()
 search= StringVar()
 #creating frames for layout

 #frame for the heading
 HeadingForm = Frame(display_screen,bd=1,relief=SOLID)
 HeadingForm.pack(side=TOP,fill=X)
 
 #first left frame for the registration 
 LForm = Frame(display_screen,width=280)
 LForm.pack(side=LEFT,fill=Y)
 #mid frame for displaying students record
 MidViewForm = Frame(display_screen, width="1000",bg="grey")
 MidViewForm.pack(side=RIGHT,fill=Y)

 #Search Panel for the students
 SearchPanel = Frame(MidViewForm, width="1000", height= "50", bg="white")
 SearchPanel.pack(side=TOP,fill=Y)

 #label for heading
 lbl_text = Label(HeadingForm, text="Advertisement Management System", font=('verdana', 22),width=600,bg="#e6c68c",fg="#5b29ab")
 lbl_text.pack()
 #creating the insert form in the LForm

 ID = Label(LForm,text="Insert Data",font = ('verdana',15),height=4)
 ID.grid(row=0,column=0,columnspan=2,sticky=" ")

 Label(LForm, text="District", font=("Arial", 12)).grid(row=1,column=0,pady=5)
 Entry(LForm,font=("Arial",10,"bold"),textvariable=district).grid(row=2,column=0,padx= 30, ipady=3)

 Label(LForm, text="Town ", font=("Arial", 12)).grid(row=1,column=1,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=town).grid(row=2,column=1,padx= 30,pady=20, ipady=3)

 Label(LForm, text="Location ", font=("Arial", 12)).grid(row=3,column=0,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=location).grid(row=4,column=0,padx= 30,pady=20, ipady=3)

 Label(LForm, text="Size", font=("Arial", 12)).grid(row=3,column=1,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=size).grid(row=4,column=1,padx= 30,pady=20, ipady=3)

 Label(LForm, text="Sq.Feet ", font=("Arial", 12)).grid(row=5,column=0,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=sqfeet).grid(row=6,column=0,padx= 30,pady=20, ipady=3)
 
 Label(LForm, text="Rate ", font=("Arial", 12)).grid(row=5,column=1,pady=5)
 rate = Entry(LForm, font=("Arial", 10, "bold"),textvariable=rate)
 rate.grid(row=6,column=1,padx= 30,pady=20, ipady=3)
 rate.delete(0, 'end') # to remove the initial value zero

 Label(LForm, text="Period", font=("Arial", 12)).grid(row=7,column=0,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=period).grid(row=8,column=0,padx= 30,pady=20, ipady=3)

 Label(LForm, text="Availability", font=("Arial", 12)).grid(row=7,column=1,pady=5)
 Entry(LForm, font=("Arial", 10, "bold"),textvariable=availability).grid(row=8,column=1,pady=5, ipady=3)

#Submit Button
 Button(LForm,text="Submit", font=("Arial", 10, "bold"),width=30,bg="lightblue",fg="black",command=register).grid(row=9,column=0,columnspan=2,padx=20,pady=20)

# Name DropDown
 # Change the label text
 # options = [
 #  "District",
 #  "Town",
 #  "Location",
 #  "Size",
 #  "Sq. Feet",
 #  "Rate",
 #  "Period"
 # ]
 # clicked = StringVar()
 # clicked.set("District")  # initial menu text
 # OptionMenu(SearchPanel, clicked, *options).grid(row=0,column=0,padx=10,pady=10) # Dropdown menu

 global clicked 
 clicked = StringVar()
 choosen = ttk.Combobox(SearchPanel, width = 20,textvariable = clicked)
  
# Adding combobox drop down list
 choosen["values"] = [
     "District",
     "Town",
     "Location",
     "Size",
     "Sq. Feet",
     "Rate",
     "Period"]
  
 choosen.grid(row=0, column=0,padx=10,pady=10)
 # Shows february as a default value
 choosen.current(0) 

# Search Bar
 search_bar = Entry(SearchPanel,font=("Arial",10,"bold"),textvariable=search, width= 50)
 search_bar.grid(row=0,column=1,padx= 10, pady= 10)
 search_bar.insert(0,"Search here......")

#Search Button with an image as an icon

 # search_btn = ImageTk.PhotoImage(Image.open("img/search_icon.png").resize((20, 20), Image.ANTIALIAS))
 # search_btn_label = Label(image=search_btn)
 # my_button = Button(SearchPanel,image= search_btn)
 # my_button.grid(row=0,column=2,padx=10,pady=10)

 Button(SearchPanel,text="Search",font=("Arial", 10, "bold"),width=10,bg="black",fg="white",command=SearchRecord).grid(row=0,column=2,padx=10,pady=10)

 

#ViewAll Button
 Button(SearchPanel,text="View All",font=("Arial", 10, "bold"),width=10,command=DisplayData).grid(row=0,column=3,padx=10,pady=10)

#Delete Button
 Button(SearchPanel,text="Delete",font=("Arial", 10, "bold"),width=10,command=Delete).grid(row=0,column=4,padx=10,pady=10)


 scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
 scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
 tree = ttk.Treeview(MidViewForm,columns=("District",'Town','Location','Size','Sqfeet','Rate','Period','Availability'),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
 scrollbary.config(command=tree.yview)
 scrollbary.pack(side=RIGHT, fill=Y)
 scrollbarx.config(command=tree.xview)
 scrollbarx.pack(side=BOTTOM, fill=X)

 tree.heading('District', text="District", anchor=W)
 tree.heading('Town', text="Town", anchor=W)   
 tree.heading('Location', text="Location", anchor=W)
 tree.heading('Size', text="Size", anchor=W)
 tree.heading('Sqfeet', text="Sqfeet", anchor=W)
 tree.heading('Rate', text="Rate", anchor=W)
 tree.heading('Period', text="Period", anchor=W)
 tree.heading('Availability', text="Availability", anchor=W)
 #setting width of the columns
 tree.column('#0', stretch=NO, minwidth=0, width=0)
 tree.column('#1', stretch=NO, minwidth=0, width=100)
 tree.column('#2', stretch=NO, minwidth=0, width=100)
 tree.column('#3', stretch=NO, minwidth=0, width=210)
 tree.column('#4', stretch=NO, minwidth=0, width=80)
 tree.column('#5', stretch=NO, minwidth=0, width=100)
 tree.column('#6', stretch=NO, minwidth=0, width=90)
 tree.column('#7', stretch=NO, minwidth=0, width=89)
 tree.column('#8', stretch=NO, minwidth=0, width=80)
 tree.pack()
 DisplayData()

def register():
    return

def SearchRecord():
    return

def DisplayData():
    return

def Delete():
    return



DisplayForm()
if __name__ == '__main__':
 display_screen.mainloop()
# Hi I am Soumyajit
# I am collaborating with Subhadeep
 
