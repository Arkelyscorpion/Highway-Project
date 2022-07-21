# IMPORTS 

import tkinter as tk
from nhsh import calculateNHSH
from mdr import calculateMDR
from ur import calculateUR
from pdf import generatePDF
from idata import IData
from tkcalendar import Calendar, DateEntry
from datetime import datetime

import os

# GLOBAL DATA

OPTION = "NH/SH"

options = [
    "NH/SH",
    "MDR/ODR/VR",
    "UR"
]

categories = {
    "NH/SH" : "National Highways / State Highways",
    "MDR/ODR/VR" : "MDR(s) and Rural Roads",
    "UR" : "Urban Roads"
}


# -------------------------------------------------------------------------------------- 

#                                     WINDOW 

# --------------------------------------------------------------------------------------

# ROOT

root = tk.Tk()
root.title("Rating of Pavement Based On Quantity of Distress")
root.configure(background='#005555')
root.minsize(750, 680)

# TITLE

labeltitle = tk.Label(root, text="Calculation of Final Rating Values Based on Quantity of Distress", bg='#005555',fg="white",padx=20,pady=10)
labeltitle.config(font=('Bahnschrift SemiBold',16))
labeltitle.pack()

# CANVAS

canvas1 = tk.Canvas(root, width=700, height=600, bg='#A1E3D8')
canvas1.pack()

# DETAILS

labelcategory = tk.Label(root, text="Category of road", bg='#A1E3D8')                           # CATEGORY
canvas1.create_window(125, 50, window=labelcategory)

clicked = tk.StringVar()                                            # DATATYPE OF MENU TEXT
clicked.set("NH/SH")                                                # INITIAL MENU TEXT
dropdowncategory = tk.OptionMenu(root, clicked, *options)
dropdowncategory.config(bg='#A1E3D8')
dropdowncategory["menu"].config(bg="#005555", fg='white')
canvas1.create_window(270, 45, window=dropdowncategory)

labelname = tk.Label(root, text="Name of the road", bg='#A1E3D8')                               # NAME
canvas1.create_window(125, 80, window=labelname)
entryname = tk.Entry(root)
canvas1.create_window(270, 80, window=entryname)

labelchainage = tk.Label(root, text="Chainage of test section", bg='#A1E3D8')                   # CHAINAGE
canvas1.create_window(125, 110, window=labelchainage)
entrychainage = tk.Entry(root)
canvas1.create_window(270, 110, window=entrychainage)

labelsurface = tk.Label(root, text="Type of surface", bg='#A1E3D8')                             # SURFACE
canvas1.create_window(125, 140, window=labelsurface)
entrysurface = tk.Entry(root)
canvas1.create_window(270, 140, window=entrysurface)

labelcarriage = tk.Label(root, text="Carriage width (m)", bg='#A1E3D8')                         # CARRIAGE
canvas1.create_window(425, 50, window=labelcarriage)
entrycarriage = tk.Entry(root)
canvas1.create_window(550, 50, window=entrycarriage)

labelweather = tk.Label(root, text="Weather condition", bg='#A1E3D8')                           # WEATHER
canvas1.create_window(425, 80, window=labelweather)
entryweather = tk.Entry(root)
canvas1.create_window(550, 80, window=entryweather)

labeldate = tk.Label(root, text="Date of observation", bg='#A1E3D8')                            # DATE
canvas1.create_window(425, 110, window=labeldate)
entrydate = DateEntry(root, width= 16, background= "#005555", foreground= "white",bd=2)
canvas1.create_window(550, 110, window=entrydate)

labeldateformat = tk.Label(root, text="(dd/mm/yyyy)", bg='#A1E3D8')
canvas1.create_window(425, 130, window=labeldateformat)

# INPUTS FOR NUMERICALS

entry = []

for i in range(0,7):
    entry.append(tk.Entry(root,highlightthickness=2))

label1 = tk.Label(root, text="Cracking (%)", bg='#A1E3D8')
canvas1.create_window(225, 200, window=label1)
canvas1.create_window(375, 200, window=entry[0])

label2 = tk.Label(root, text="Ravelling (%)", bg='#A1E3D8')
canvas1.create_window(225, 240, window=label2)
canvas1.create_window(375, 240, window=entry[1])

label3 = tk.Label(root, text="Potholes (%)", bg='#A1E3D8')
canvas1.create_window(225, 280, window=label3)
canvas1.create_window(375, 280, window=entry[2])

label4 = tk.Label(root, text="Shoving (%)", bg='#A1E3D8')
canvas1.create_window(225, 320, window=label4)
canvas1.create_window(375, 320, window=entry[3])

label5 = tk.Label(root, text="Patching (%)", bg='#A1E3D8')
canvas1.create_window(225, 360, window=label5)
canvas1.create_window(375, 360, window=entry[4])

label6 = tk.Label(root, text="Settlements (%)", bg='#A1E3D8')
canvas1.create_window(225, 400, window=label6)
canvas1.create_window(375, 400, window=entry[5])

label7 = tk.Label(root, text="Rut Depth (%)", bg='#A1E3D8')
canvas1.create_window(225, 440, window=label7)
canvas1.create_window(375, 440, window=entry[6])

# -------------------------------------------------------------------------------------- 

#                  INTIALIZING INPUT BOXES FOR EASE REMOVE DURING DEPLOY 

# --------------------------------------------------------------------------------------

entry[0].insert(0,"9")
entry[1].insert(0,"9")
entry[2].insert(0,"9")
entry[3].insert(0,"9")
entry[4].insert(0,"9")
entry[5].insert(0,"9")
entry[6].insert(0,"9")

entryname.insert(0,"default")
entrychainage.insert(0,"default")
entrysurface.insert(0,"default")
entrycarriage.insert(0,"8.92")
entryweather.insert(0,"Sunny")

# SUBMIT 

def validate(a):
    if a.isdigit() and float(a)<=100 and float(a)>=0:
        return True
    else: 
        return False

def submit():

    valid=[]
    for i in range(0,7):
        valid.append(validate(entry[i].get()))
    
    if valid.count(False)==0:
        for i in range(0,7):
            IData['inum'][i] = float(entry[i].get())
            entry[i].config(highlightbackground = "white", highlightcolor= "white")
    else:
        for i in range(0,7):
            if valid[i] == False:
                entry[i].config(highlightbackground = "red", highlightcolor= "red")
            else:
                entry[i].config(highlightbackground = "white", highlightcolor= "white")

    global OPTION
    OPTION = clicked.get()

    IData['category'] = categories[OPTION]
    IData['name'] = entryname.get()
    IData['chainage'] = entrychainage.get()
    IData['surface'] = entrysurface.get()
    IData['carriage'] = float(entrycarriage.get())
    IData['weather'] = entryweather.get()
    IData['date'] = entrydate.get_date()
    IData['optionChosen'] = OPTION

    print(IData)

    # -------------------------------------------------------------------------------------- 
    #                                     FUNCTIONALITY 
    # --------------------------------------------------------------------------------------

    # DEPENDING ON THE CATEGORY CHOSEN PICK THE NECESSARY VALUES

    if(OPTION == options[0]):
        data, final_rating_value,cond = calculateNHSH()
    elif(OPTION == options[1]):
        data, final_rating_value,cond = calculateMDR()
    elif(OPTION == options[2]):
        data, final_rating_value,cond = calculateUR()

    date = datetime.now().strftime("%Y_%m_%d_%I_%M_%S_%p")  
    tempFileName = f"Rating_{date}"
    fileName = r'{}'.format(tempFileName)

    # -------------------------------------------------------------------------------------- 
    #                                     PDF GENERATION 
    # --------------------------------------------------------------------------------------

    # GENERATE THE PDF

    generatePDF(options,OPTION,data,final_rating_value,cond,fileName)

    # OPEN THE FILE

    os.startfile(r'{}.pdf'.format(fileName))


# RESET 

def reset():

    for i in range(0,7):
        entry[i].delete(0,tk.END)
        entry[i].insert(0,"") 

    entryname.delete(0,tk.END)
    entryname.insert(0,"")
    entrychainage.delete(0,tk.END)
    entrychainage.insert(0,"")
    entrysurface.delete(0,tk.END)
    entrysurface.insert(0,"")
    entrycarriage.delete(0,tk.END)
    entrycarriage.insert(0,"")
    entryweather.delete(0,tk.END)
    entryweather.insert(0,"")
    entrydate.delete(0,tk.END)
    entrydate.insert(0,"")


# -------------------------------------------------------------------------------------- 

#                              READ THE USER ENTERED DATA 

# --------------------------------------------------------------------------------------


submitButton = tk.Button(text='Submit', command=submit, padx=10,pady=5, fg='white', bg='#005555')
canvas1.create_window(450, 510, window=submitButton)

resetButton = tk.Button(text='Reset', command=reset, padx=12,pady=5, fg='white', bg='#005555')
canvas1.create_window(300, 510, window=resetButton)

root.mainloop()


# -------------------------------------------------------------------------------------- 

#                                     FUNCTIONALITY 

# --------------------------------------------------------------------------------------

# DEPENDING ON THE CATEGORY CHOSEN PICK THE NECESSARY VALUES

# if(OPTION == options[0]):
#     data, final_rating_value,cond = calculateNHSH()
# elif(OPTION == options[1]):
#     data, final_rating_value,cond = calculateMDR()
# elif(OPTION == options[2]):
#     data, final_rating_value,cond = calculateUR()

# -------------------------------------------------------------------------------------- 

#                                     PDF GENERATION 

# --------------------------------------------------------------------------------------

# GENERATE THE PDF

# generatePDF(options,OPTION,data,final_rating_value,cond)

# os.startfile(r'{}.pdf'.format(fileName))






# Create Dropdown menu
# drop = tk.OptionMenu(root, clicked, *options)
# drop.config(bg='#A1E3D8', padx=10, pady=5)
# drop["menu"].config(bg="#005555", fg='white')
# drop.pack()