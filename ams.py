#AMS--1

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
from typing import Sized
from PIL import ImageTk, Image

def Database():
 global conn, cursor
 #creating student database
 conn = sqlite3.connect("ad.db")
 cursor = conn.cursor()
 #creating ad management system table
 cursor.execute("CREATE TABLE IF NOT EXISTS AD_MANAGE (SLNO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,DISTRICT TEXT,TOWN TEXT,LOCATION TEXT,SIZE TEXT,SQFEET TEXT,RATE TEXT,PERIOD TEXT,AVAILABILITY TEXT)")


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
 global district,town,location,size,sqfeet,rate,period,availability,search,tree,choosen
 global entry_district, entry_town, entry_location, entry_size, entry_sqfeet, entry_rate, entry_period, entry_availability

 district = StringVar()
 town = StringVar()
 location = StringVar()
 size = StringVar()
 sqfeet = StringVar()
 rate = StringVar()
 period = StringVar()
 availability = StringVar()
 search= StringVar()
 #creating frames for layout

 #frame for the heading
 HeadingForm = Frame(display_screen,bd=1,relief=SOLID)
 HeadingForm.pack(side=TOP,fill=X)
 
 #first left frame for the registration 
 LForm = Frame(display_screen,width=280, bd=3)
 LForm.pack(side=LEFT,fill=Y)
 #mid frame for displaying students record
 MidViewForm = Frame(display_screen, width="1000",bg="grey")
 MidViewForm.pack(side=RIGHT,fill=Y)

 #Search Panel for the students
 SearchPanel = Frame(MidViewForm, width="1000", height= "50", bg="white")
 SearchPanel.pack(side=TOP,fill=Y)

 #label for heading
 lbl_text = Label(HeadingForm, text="Advertisement Management System", font=('verdana', 22, "bold"),width=600,fg="#535DD1")
 lbl_text.pack()
 #creating the insert form in the LForm

 ID = Label(LForm,text="Insert Data",font = ('verdana',17, "bold"),height=4, fg="#535DD1")
 ID.grid(row=0,column=0,columnspan=2,sticky=" ")

 Label(LForm, text="District", font=("Arial", 12)).grid(row=1,column=0,pady=5)
 entry_district = Entry(LForm,font=("Arial",10,"bold"),textvariable=district)
 entry_district.grid(row=2,column=0,padx= 30, ipady=3)

 Label(LForm, text="Town ", font=("Arial", 12)).grid(row=1,column=1,pady=5)
 entry_town = Entry(LForm, font=("Arial", 10, "bold"),textvariable=town)
 entry_town.grid(row=2,column=1,padx= 30,pady=20, ipady=3)

 Label(LForm, text="Location ", font=("Arial", 12)).grid(row=3,column=0,pady=5)
 entry_location = Entry(LForm, font=("Arial", 10, "bold"),textvariable=location)
 entry_location.grid(row=4, column=0, padx=30, pady=20, ipady=3)

 Label(LForm, text="Size", font=("Arial", 12)).grid(row=3,column=1,pady=5)
 entry_size = Entry(LForm, font=("Arial", 10, "bold"),textvariable=size)
 entry_size.grid(row=4, column=1, padx=30, pady=20, ipady=3)

 Label(LForm, text="Sq.Feet ", font=("Arial", 12)).grid(row=5,column=0,pady=5)
 entry_sqfeet = Entry(LForm, font=("Arial", 10, "bold"),textvariable=sqfeet)
 entry_sqfeet.grid(row=6, column=0, padx=30, pady=20, ipady=3)

 Label(LForm, text="Rate ", font=("Arial", 12)).grid(row=5,column=1,pady=5)
 entry_rate = Entry(LForm, font=("Arial", 10, "bold"),textvariable=rate)
 entry_rate.grid(row=6,column=1,padx= 30,pady=20, ipady=3)
 entry_rate.delete(0, 'end') # to remove the initial value zero

 Label(LForm, text="Period", font=("Arial", 12)).grid(row=7,column=0,pady=5)
 entry_period = Entry(LForm, font=("Arial", 10, "bold"),textvariable=period)
 entry_period.grid(row=8, column=0, padx=30, pady=20, ipady=3)

 Label(LForm, text="Availability", font=("Arial", 12)).grid(row=7,column=1,pady=5)
 entry_availability = Entry(LForm, font=("Arial", 10, "bold"),textvariable=availability)
 entry_availability.grid(row=8,column=1,pady=5, ipady=3)

#Submit Button
 Button(LForm,text="Submit", font=("Arial", 10, "bold"),width=25,bg="#535DD1",fg="white",command=register).grid(row=9,column=0,columnspan=2,padx=20,pady=20, ipady = 3)

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
 choosen = ttk.Combobox(SearchPanel, state="readonly", width = 20,textvariable = clicked)
  
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
 # Shows District as a default value
 choosen.current(0) 

# Search Bar
 search_bar = Entry(SearchPanel,font=("Arial",10, "bold"),textvariable=search, width= 50, bd=1, bg = "#F5F4F4")
 search_bar.grid(row=0,column=1,padx= 10, pady= 10, ipady = 4, ipadx = 1)
 search_bar.insert(0,"  Search here ")
 search_bar.configure(state=DISABLED)

 def on_click(event):
     search_bar.configure(state=NORMAL)
     search_bar.delete(0, END)
     # make the callback only work once
     search_bar.unbind('<Button-1>', on_click_id)

 on_click_id = search_bar.bind('<Button-1>', on_click)



#Search Button with an image as an icon

 # search_btn = ImageTk.PhotoImage(Image.open("img/search_icon.png").resize((20, 20), Image.ANTIALIAS))
 # search_btn_label = Label(image=search_btn)
 # my_button = Button(SearchPanel,image= search_btn)
 # my_button.grid(row=0,column=2,padx=10,pady=10)

#Search Button
 Button(SearchPanel,text="Search",font=("Arial", 10, "bold"),width=10,bg="#535DD1",fg="white",relief="flat", command=SearchRecord).grid(row=0,column=2,padx=10,pady=10)

#ViewAll Button
 Button(SearchPanel,text="View All",font=("Arial", 10, "bold"),width=10,command=DisplayData).grid(row=0,column=3,padx=10,pady=10)

#Delete Button
 Button(SearchPanel,text="Delete",font=("Arial", 10, "bold"),width=10,command=Delete).grid(row=0,column=4,padx=10,pady=10)





 scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
 scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
 tree = ttk.Treeview(MidViewForm,columns=("SL.no.","District",'Town','Location','Size','Sqfeet','Rate','Period','Availability'),selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
 scrollbary.config(command=tree.yview)
 scrollbary.pack(side=RIGHT, fill=Y)
 scrollbarx.config(command=tree.xview)
 scrollbarx.pack(side=BOTTOM, fill=X)
 tree.heading('SL.no.', text="SL.no.", anchor=W)
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
 tree.column('#1', stretch=NO, minwidth=0, width=50)
 tree.column('#2', stretch=NO, minwidth=0, width=80)
 tree.column('#3', stretch=NO, minwidth=0, width=80)
 tree.column('#4', stretch=NO, minwidth=0, width=250)
 tree.column('#5', stretch=NO, minwidth=0, width=80)
 tree.column('#6', stretch=NO, minwidth=0, width=66)
 tree.column('#7', stretch=NO, minwidth=0, width=60)
 tree.column('#8', stretch=NO, minwidth=0, width=100)
 tree.column('#9', stretch=NO, minwidth=0, width=80)
 tree.pack()
 DisplayData()
 style = ttk.Style()
 #style.theme_use("alt")
 style.configure("Treeview",
                 #background = '#DEDEDE',
                 foreground = 'black',
                 rowheight = 30,
                 feildbackground = "silver",
                 )
 style.configure('Treeview.Heading', background="green3")

 style.map('Treeview', background=[('selected', '#535DD1')])
 style.map('Treeview.Heading', background=[('selected', '#535DD1')])
 tree.tag_configure('white', background='#F7F7F7')
 tree.tag_configure('grey', background='#DEDEDE')

def register():
 Database()
 #getting form data
 district1 = district.get()
 town1 = town.get()
 location1 = location.get()
 size1= size.get()
 sqfeet1 = sqfeet.get()
 rate1 = rate.get()
 period1 = period.get()
 availability1 = availability.get()
 if district1 == '' or town1 == '' or location1== '' or size1== '' or sqfeet1== '' or rate1 == '' or period1 == '' or availability1 == '':
     tkMessageBox.showinfo("Warning","fill the empty field!!!")
 else:
     entry_district.delete(0,END)
     entry_town.delete(0,END)
     entry_location.delete(0,END)
     entry_size.delete(0,END)
     entry_sqfeet.delete(0,END)
     entry_rate.delete(0,END)
     entry_period.delete(0,END)
     entry_availability.delete(0,END)
     conn.execute('INSERT INTO AD_MANAGE(DISTRICT,TOWN,LOCATION,SIZE,SQFEET,RATE,PERIOD,AVAILABILITY) \
              VALUES (?,?,?,?,?,?,?,?)',(district1,town1,location1,size1,sqfeet1,rate1,period1,availability1));
     conn.commit()
     tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
     DisplayData()
     conn.close()
 
def SearchRecord():
        # open database
        Database()
        # checking search text is empty or not
        lookup_record = search.get()

        for record in tree.get_children(): #First, clear the table
            tree.delete(record)
        conn = sqlite3.connect('ad.db')
        c = conn.cursor()
        choose = choosen.get()
        if ( choose == "District"):
            c.execute("SELECT rowid, * FROM AD_MANAGE WHERE district like ?", (lookup_record,))
            records = c.fetchall()
        if (choose == "Town"):
            c.execute("SELECT rowid, * FROM AD_MANAGE WHERE town like ?", (lookup_record,))
            records = c.fetchall()
        if (choose == "Location"):
            c.execute("SELECT rowid, * FROM AD_MANAGE WHERE location like ?", (lookup_record,))
            records = c.fetchall()
        if (choose == "Size"):
            c.execute("SELECT rowid, * FROM AD_MANAGE WHERE size like ?", (lookup_record,))
            records = c.fetchall()
        if (choose == "Sq. Feet"):
            c.execute("SELECT rowid, * FROM AD_MANAGE WHERE sqfeet like ?", (lookup_record,))
            records = c.fetchall()
        if (choose == "Rate"):
            c.execute("SELECT rowid, * FROM AD_MANAGE WHERE rate like ?", (lookup_record,))
            records = c.fetchall()
        if (choose == "Period"):
            c.execute("SELECT rowid, * FROM AD_MANAGE WHERE period like ?", (lookup_record,))
            records = c.fetchall()

        global count
        count = 0
        for record in records: #Print
            if count % 2 == 0:
                tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1],  record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]),
                               tags=('evenrow',))
            else:
                tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1],  record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]),
                               tags=('oddrow',))
            count += 1 # increment counter

        conn.commit()
        conn.close()



def Delete():
    # selected_item = tree.selection()[0]
    # tree.delete(selected_item)
    # conn = sqlite3.connect('ad.db')
    # c = conn.cursor()
    # c.execute("DELETE from AD_MANAGE WHERE oid="+ selected_item[-1])
    # #delete_box.delete(0, END)
    # conn.commit()
    # conn.close()
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else: 
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM AD_MANAGE WHERE SLNO= %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM AD_MANAGE")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    counter = 0
    for data in fetch:
        if(counter%2 == 0):
            tree.insert('', 'end', values=(data), tags=('white',))
        else:
            tree.insert('', 'end', values=(data), tags=('grey',))
        counter = counter + 1
    cursor.close()
    conn.close()


DisplayForm()
if __name__ == '__main__':
 mainloop()

 
