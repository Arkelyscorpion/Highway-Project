# IMPORTS 

import tkinter as tk
from nhsh import calculateNHSH
from mdr import calculateMDR
from ur import calculateUR
from pdf import generatePDF
from idata import IData
from tkcalendar import DateEntry
from datetime import datetime
from function import is_number
from tkinter import messagebox

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
canvas1.create_window(106, 50, window=labelcategory)

detail = []

for i in range(0,5):
    detail.append(tk.Entry(root,highlightthickness=2))

clicked = tk.StringVar()                                            # DATATYPE OF MENU TEXT
clicked.set("NH/SH")                                                # INITIAL MENU TEXT
dropdowncategory = tk.OptionMenu(root, clicked, *options)
dropdowncategory.config(bg='#A1E3D8')
dropdowncategory["menu"].config(bg="#005555", fg='white')
canvas1.create_window(270, 45, window=dropdowncategory)

labelname = tk.Label(root, text="Name of the road", bg='#A1E3D8')                               # NAME
canvas1.create_window(108, 80, window=labelname)
canvas1.create_window(270, 80, window=detail[0])

labelchainage = tk.Label(root, text="Chainage of test section", bg='#A1E3D8')                   # CHAINAGE
canvas1.create_window(125, 110, window=labelchainage)
canvas1.create_window(270, 110, window=detail[1])

labelsurface = tk.Label(root, text="Type of surface", bg='#A1E3D8')                             # SURFACE
canvas1.create_window(103, 140, window=labelsurface)
canvas1.create_window(270, 140, window=detail[2])

labelcarriage = tk.Label(root, text="Carriage width (m)", bg='#A1E3D8')                         # CARRIAGE
canvas1.create_window(422, 50, window=labelcarriage)
canvas1.create_window(550, 50, window=detail[3])

labelweather = tk.Label(root, text="Weather condition", bg='#A1E3D8')                           # WEATHER
canvas1.create_window(422, 80, window=labelweather)
canvas1.create_window(550, 80, window=detail[4])

labeldate = tk.Label(root, text="Date of observation", bg='#A1E3D8')                            # DATE
canvas1.create_window(425, 110, window=labeldate)
entrydate = DateEntry(root, width= 16, background= "#005555", foreground= "white",bd=2, date_pattern='dd/mm/yyyy')
canvas1.create_window(550, 110, window=entrydate)

labeldateformat = tk.Label(root, text="(dd/mm/yyyy)", bg='#A1E3D8')
canvas1.create_window(425, 130, window=labeldateformat)

# INPUTS FOR NUMERICALS

entry = []

for i in range(0,7):
    entry.append(tk.Entry(root,highlightthickness=2))

label1 = tk.Label(root, text="Cracking (%)", bg='#A1E3D8')
canvas1.create_window(276, 200, window=label1)
canvas1.create_window(425, 200, window=entry[0])

label2 = tk.Label(root, text="Ravelling (%)", bg='#A1E3D8')
canvas1.create_window(276, 240, window=label2)
canvas1.create_window(425, 240, window=entry[1])

label3 = tk.Label(root, text="Potholes (%)", bg='#A1E3D8')
canvas1.create_window(276, 280, window=label3)
canvas1.create_window(425, 280, window=entry[2])

label4 = tk.Label(root, text="Shoving (%)", bg='#A1E3D8')
canvas1.create_window(274, 320, window=label4)
canvas1.create_window(425, 320, window=entry[3])

label5 = tk.Label(root, text="Patching (%)", bg='#A1E3D8')
canvas1.create_window(276, 360, window=label5)
canvas1.create_window(425, 360, window=entry[4])

label6 = tk.Label(root, text="Settlements (%)", bg='#A1E3D8')
canvas1.create_window(282, 400, window=label6)
canvas1.create_window(425, 400, window=entry[5])

label7 = tk.Label(root, text="Rut Depth (mm)", bg='#A1E3D8')
canvas1.create_window(285, 440, window=label7)
canvas1.create_window(425, 440, window=entry[6])

# -------------------------------------------------------------------------------------- 

#                                      FUNCTIONALITY 

# --------------------------------------------------------------------------------------

# SUBMIT 

def validate(a):
    if is_number(a) and float(a)<=100 and float(a)>=0:
        return True
    else: 
        return False

def submit():

    entriesCheck = False
    detailsCheck = False

    # VALUES CHECK

    valid=[]
    for i in range(0,6):
        valid.append(validate(entry[i].get()))
    valid.append(is_number(entry[6].get()) and (float(entry[6].get())>=0))
    
    if valid.count(False) == 0:
        for i in range(0,7):
            IData['inum'][i] = float(entry[i].get())
            entry[i].config(highlightbackground = "white", highlightcolor= "white")
            entriesCheck = True
    else:
        for i in range(0,7):
            if valid[i] == False:
                entry[i].config(highlightbackground = "red", highlightcolor= "red")
            else:
                entry[i].config(highlightbackground = "white", highlightcolor= "white")

    global OPTION
    OPTION = clicked.get()

    # DETAILS CHECK 

    check = []
    check.append(len(detail[0].get())<=75 and len(detail[0].get())>0)
    check.append(len(detail[1].get())<=15 and len(detail[1].get())>0)
    check.append(len(detail[2].get())<=15 and len(detail[2].get())>0)
    check.append(is_number(detail[3].get()) and float(detail[3].get())<=15 and float(detail[3].get())>=0)
    check.append(len(detail[4].get())<=10 and len(detail[4].get())>0)
     
    if check.count(False) == 0:
        IData['category'] = categories[OPTION]
        IData['name'] = detail[0].get()
        IData['chainage'] = detail[1].get()
        IData['surface'] = detail[2].get()
        IData['carriage'] = float(detail[3].get())
        IData['weather'] = detail[4].get()
        IData['date'] = (entrydate.get_date()).strftime("%d/%m/%Y")
        IData['optionChosen'] = OPTION

        for i in range(0,5):
            detail[i].config(highlightbackground = "white", highlightcolor= "white")
        detailsCheck = True 
    else:
        for i in range(0,5):
            if check[i] == False:
                detail[i].config(highlightbackground = "red", highlightcolor= "red")
            else:
                detail[i].config(highlightbackground = "white", highlightcolor= "white")


    # -------------------------------------------------------------------------------------- 
    #                                     CALCULATION 
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

    if entriesCheck and detailsCheck:
        generatePDF(options,OPTION,data,final_rating_value,cond,fileName)
    
    # OPEN THE FILE
        os.startfile(r'{}.pdf'.format(fileName))
        tk.messagebox.showinfo("Success",  "Your pdf has been generated successfully!")
        reset()


# RESET 

def reset():

    for i in range(0,7):
        entry[i].delete(0,tk.END)
        entry[i].insert(0,"") 

    for i in range(0,5):
        detail[i].delete(0,tk.END)
        detail[i].insert(0,"")
    entrydate.delete(0,tk.END)


# -------------------------------------------------------------------------------------- 

#                              READ THE USER ENTERED DATA 

# --------------------------------------------------------------------------------------


submitButton = tk.Button(text='Submit', command=submit, padx=10,pady=5, fg='white', bg='#005555')
canvas1.create_window(440, 510, window=submitButton)

resetButton = tk.Button(text='Reset', command=reset, padx=14,pady=5, fg='white', bg='#005555')
canvas1.create_window(290, 510, window=resetButton)

root.mainloop()