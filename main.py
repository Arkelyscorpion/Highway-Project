# IMPORTS 

import tkinter as tk
#from click import option
from fpdf import FPDF
from nhsh import *
from mdr import *
from ur import *
from idata import IData

x1, x2, x3, x4, x5, x6, x7 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0
OPTION = "NH/SH"

root = tk.Tk()
options = [
    "NH/SH",
    "MDR/ODR/VR",
    "UR"
]

root.title("Rating of Pavement Based On Quantity of Distress")
root.configure(background='#005555')
root.minsize(750, 680)

# datatype of menu text
clicked = tk.StringVar()

# initial menu text
clicked.set("NH/SH")

# Create Dropdown menu
# drop = tk.OptionMenu(root, clicked, *options)
# drop.config(bg='#A1E3D8', padx=10, pady=5)
# drop["menu"].config(bg="#005555", fg='white')
# drop.pack()

labeltitle = tk.Label(root, text="Calculation of Final Rating Values Based on Quantity of Distress", bg='#005555',fg="white",padx=20,pady=10)
labeltitle.config(font=('Bahnschrift SemiBold',16))
labeltitle.pack()

canvas1 = tk.Canvas(root, width=700, height=600, bg='#A1E3D8')
canvas1.pack()

# frame = tk.Frame(root, bg='#A1E3D8')
# frame.place(relwidth=0.9, relheight=0.9,relx=0.1,rely=0.1)

labelcategory = tk.Label(root, text="Category of road", bg='#A1E3D8')
canvas1.create_window(125, 50, window=labelcategory)

# Create Dropdown menu
drop = tk.OptionMenu(root, clicked, *options)
drop.config(bg='#A1E3D8')
drop["menu"].config(bg="#005555", fg='white')
canvas1.create_window(270, 45, window=drop)


# label = tk.Label(frame, text="Name of the road", bg='#A1E3D8')
# label.pack()

labelname = tk.Label(root, text="Name of the road", bg='#A1E3D8')
canvas1.create_window(125, 80, window=labelname)
entryname = tk.Entry(root)
canvas1.create_window(270, 80, window=entryname)

labelchainage = tk.Label(root, text="Chainage of test section", bg='#A1E3D8')
canvas1.create_window(125, 110, window=labelchainage)
entrychainage = tk.Entry(root)
canvas1.create_window(270, 110, window=entrychainage)

labelsurface = tk.Label(root, text="Type of surface", bg='#A1E3D8')
canvas1.create_window(125, 140, window=labelsurface)
entrysurface = tk.Entry(root)
canvas1.create_window(270, 140, window=entrysurface)

labelcarriage = tk.Label(root, text="Carriage width (m)", bg='#A1E3D8')
canvas1.create_window(425, 50, window=labelcarriage)
entrycarriage = tk.Entry(root)
canvas1.create_window(550, 50, window=entrycarriage)

labelweather = tk.Label(root, text="Weather condition", bg='#A1E3D8')
canvas1.create_window(425, 80, window=labelweather)
entryweather = tk.Entry(root)
canvas1.create_window(550, 80, window=entryweather)

labeldate = tk.Label(root, text="Date of observation", bg='#A1E3D8')
canvas1.create_window(425, 110, window=labeldate)
entrydate = tk.Entry(root)
canvas1.create_window(550, 110, window=entrydate)

labeldateformat = tk.Label(root, text="(dd/mm/yyyy)", bg='#A1E3D8')
canvas1.create_window(425, 130, window=labeldateformat)

# INPUTS FOR NUMERICALS

label1 = tk.Label(root, text="Cracking (%)", bg='#A1E3D8')
canvas1.create_window(225, 200, window=label1)
entry1 = tk.Entry(root)
canvas1.create_window(375, 200, window=entry1)

label2 = tk.Label(root, text="Ravelling (%)", bg='#A1E3D8')
canvas1.create_window(225, 240, window=label2)
entry2 = tk.Entry(root)
canvas1.create_window(375, 240, window=entry2)

label3 = tk.Label(root, text="Potholes (%)", bg='#A1E3D8')
canvas1.create_window(225, 280, window=label3)
entry3 = tk.Entry(root)
canvas1.create_window(375, 280, window=entry3)

label4 = tk.Label(root, text="Shoving (%)", bg='#A1E3D8')
canvas1.create_window(225, 320, window=label4)
entry4 = tk.Entry(root)
canvas1.create_window(375, 320, window=entry4)

label5 = tk.Label(root, text="Patching (%)", bg='#A1E3D8')
canvas1.create_window(225, 360, window=label5)
entry5 = tk.Entry(root)
canvas1.create_window(375, 360, window=entry5)

label6 = tk.Label(root, text="Settlements (%)", bg='#A1E3D8')
canvas1.create_window(225, 400, window=label6)
entry6 = tk.Entry(root)
canvas1.create_window(375, 400, window=entry6)

label7 = tk.Label(root, text="Rut Depth (%)", bg='#A1E3D8')
canvas1.create_window(225, 440, window=label7)
entry7 = tk.Entry(root)
canvas1.create_window(375, 440, window=entry7)

# -------------------------------------------------------------------------------------- 

#                  INTIALIZING INPUT BOXES FOR EASE REMOVE DURING DEPLOY 

# --------------------------------------------------------------------------------------

entry1.insert(0,"9")
entry2.insert(0,"9")
entry3.insert(0,"9")
entry4.insert(0,"9")
entry5.insert(0,"9")
entry6.insert(0,"9")
entry7.insert(0,"9")

entryname.insert(0,"default")
entrychainage.insert(0,"default")
entrysurface.insert(0,"default")
entrycarriage.insert(0,"8.92")
entryweather.insert(0,"Sunny")
entrydate.insert(0,"29/09/2102")

# --------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------- 

#                              READ THE USER ENTERED DATA 

# --------------------------------------------------------------------------------------


def func():
    global x1, x2, x3, x4, x5, x6, x7
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    x3 = float(entry3.get())
    x4 = float(entry4.get())
    x5 = float(entry5.get())
    x6 = float(entry6.get())
    x7 = float(entry7.get())

    global OPTION
    OPTION = clicked.get()

    IData['name'] = entryname.get()
    IData['chainage'] = entrychainage.get()
    IData['surface'] = entrysurface.get()
    IData['carriage'] = float(entrycarriage.get())
    IData['weather'] = entryweather.get()
    IData['date'] = entrydate.get()


button1 = tk.Button(text='Submit', command=func, padx=10,
                    pady=5, fg='white', bg='#005555')
canvas1.create_window(350, 510, window=button1)


root.mainloop()


# -------------------------------------------------------------------------------------- 

#                                     FUNCTIONALITY 

# --------------------------------------------------------------------------------------

# DEPENDING ON THE CATEGORY CHOSEN PICK THE NECESSARY VALUES

inputs = []

if(OPTION == options[0]):

    wt = [1.0, 0.75, 0.5, 1.0, 0.75, 0.75, 1.0]
    inputs.append(x1)
    inputs.append(x2)
    inputs.append(x3)
    inputs.append(x4)
    inputs.append(x5)
    inputs.append(x6)
    inputs.append(x7)

elif(OPTION == options[1]):

    wt = [1.0, 0.75, 0.5, 0.75, 0.75]
    inputs.append(x1)
    inputs.append(x2)
    inputs.append(x3)
    inputs.append(x5)
    inputs.append(x6)

elif(OPTION == options[2]):

    wt = [1.0, 0.75, 0.5, 0.75, 1.0]
    inputs.append(x1)
    inputs.append(x2)
    inputs.append(x3)
    inputs.append(x6)
    inputs.append(x7)


# COMPUTING FINAL RATING VALUE

sum = 0
final_list = []  # new comment
cond = ""

if(OPTION == options[0]):

    for i in range(len(inputs)):
        final, condition = computeNHSH(i+1, inputs[i])
        final_list.append(final)
        sum = sum + round(final*wt[i], 3)

elif(OPTION == options[1]):

    for i in range(len(inputs)):
        final, condition = computeMDR(i+1, inputs[i])
        final_list.append(final)
        sum = sum + round(final*wt[i], 3)


elif(OPTION == options[2]):

    for i in range(len(inputs)):
        final, condition = computeUR(i+1, inputs[i])
        final_list.append(final)
        sum = sum + round(final*wt[i], 3)


final_rating_value = sum/len(inputs)

# COMPUTING CONDITION OF THE ROAD

if(final_rating_value <= 1):
    cond = "Poor"
elif(final_rating_value >= 1.1 and final_rating_value <= 2):
    cond = "Fair"
elif(final_rating_value >= 2.1 and final_rating_value <= 3):
    cond = "Good"


# COMPUTING THE DATA AND STORING IN A TUPLE

# NH/SH 

if(OPTION == options[0]):
    data = (
        ("Distress Type", "Input(%)", "Rating", "Weightage", "Wt Rating Value"),
        ("Cracking", str(inputs[0]), str(final_list[0]),
         str(wt[0]), str(round(final_list[0]*wt[0], 1))),
        ("Ravelling", str(inputs[1]), str(final_list[1]), str(
            wt[1]), str(round(final_list[1]*wt[1], 1))),
        ("Potholes", str(inputs[2]), str(final_list[2]),
         str(wt[2]), str(round(final_list[2]*wt[2], 1))),
        ("Shoving", str(inputs[3]), str(final_list[3]),
         str(wt[3]), str(round(final_list[3]*wt[3], 1))),
        ("Patching", str(inputs[4]), str(final_list[4]),
         str(wt[4]), str(round(final_list[4]*wt[4], 1))),
        ("Settlements", str(inputs[5]), str(final_list[5]), str(
            wt[5]), str(round(final_list[5]*wt[5], 1))),
        ("Run Depth", str(inputs[6]), str(final_list[6]), str(
            wt[6]), str(round(final_list[6]*wt[6], 1))),
    )

# MDR/ODR/VR

if(OPTION == options[1]):
    data = (
        ("Distress Type", "Input(%)", "Rating", "Weightage", "Wt Rating Value"),
        ("Cracking", str(inputs[0]), str(final_list[0]),
         str(wt[0]), str(round(final_list[0]*wt[0], 1))),
        ("Ravelling", str(inputs[1]), str(final_list[1]), str(
            wt[1]), str(round(final_list[1]*wt[1], 1))),
        ("Potholes", str(inputs[2]), str(final_list[2]),
         str(wt[2]), str(round(final_list[2]*wt[2], 1))),
        ("Patching", str(inputs[3]), str(final_list[3]),
         str(wt[3]), str(round(final_list[3]*wt[3], 1))),
        ("Settlements", str(inputs[4]), str(final_list[4]), str(
            wt[4]), str(round(final_list[4]*wt[4], 1))),
    )

# UR

if(OPTION == options[2]):
    data = (
        ("Distress Type", "Input(%)", "Rating", "Weightage", "Wt Rating Value"),
        ("Cracking", str(inputs[0]), str(final_list[0]),
         str(wt[0]), str(round(final_list[0]*wt[0], 1))),
        ("Ravelling", str(inputs[1]), str(final_list[1]), str(
            wt[1]), str(round(final_list[1]*wt[1], 1))),
        ("Potholes", str(inputs[2]), str(final_list[2]),
         str(wt[2]), str(round(final_list[2]*wt[2], 1))),
        ("Settlements", str(inputs[3]), str(final_list[3]), str(
            wt[3]), str(round(final_list[3]*wt[3], 1))),
        ("Rut depth", str(inputs[4]), str(final_list[4]), str(
            wt[4]), str(round(final_list[4]*wt[4], 1))),
    )



# -------------------------------------------------------------------------------------- 

#                                     PDF PART 

# --------------------------------------------------------------------------------------

# INITIALIZE PAGE  

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=16, style='B')
pdf.ln()

# PDF TITLE

pdf.cell(0,txt="RATING OF PAVEMENTS BASED ON QUANTITY OF DISTRESS", align='C')
line_height = pdf.font_size * 2.5
col_width = pdf.epw / 5
pdf.ln()
pdf.ln()

# PDF CONTENT

pdf.set_font("Helvetica", size=10)
lh_list = []  # list with proper line_height for each row
use_default_height = 0  # flag

# CATEGORY OF THE ROAD BASED ON THE OPTION SELECTED BY THE USER

if(OPTION == options[0]):
    road_type = "National Highways / State Highways"
elif(OPTION == options[1]):
    road_type = "MDR(s) and Rural Roads"
else:
    road_type = "Urban Roads"

pdf.ln()

pdf.cell(txt="Category of Road : " + road_type)
pdf.ln()
pdf.ln()

pdf.cell(txt= f"Name of the Road : " + IData['name'])
pdf.cell(111, txt="Carraigeway Width(m) : " + str(IData['carriage']), align='R')
pdf.ln()
pdf.ln()

pdf.cell(txt="Chainage of Test Section : " + IData['chainage'])
pdf.cell(107, txt="Date of Observation : " + IData['date'], align='R')
pdf.ln()
pdf.ln()

pdf.cell(txt="Type of Surface : " + IData['surface'])
pdf.cell(112, txt="Weather Condition : " + IData['weather'], align='R')
pdf.ln()
pdf.ln()

pdf.ln()

# TABLE PART

pdf.set_font("Helvetica", size=10)

# create lh_list of line_heights which size is equal to num rows of data
for row in data:
    for datum in row:
        word_list = datum.split()
        number_of_words = len(word_list)  # how many words
        if number_of_words > 2:  # names and cities formed by 2 words like Los Angeles are ok)
            use_default_height = 1
            # new height change according to data
            new_line_height = pdf.font_size * (number_of_words/2)
    if not use_default_height:
        lh_list.append(line_height)
    else:
        lh_list.append(new_line_height)
        use_default_height = 0

# create your fpdf table ..passing also max_line_height!
for j, row in enumerate(data):
    for datum in row:
        if(j == 0):
            pdf.set_font(style='B')
        else:
            pdf.set_font()
        line_height = lh_list[j]  # choose right height for current row
        pdf.multi_cell(col_width, line_height, datum, border=1, align='L', ln=3,
                       max_line_height=pdf.font_size)
    pdf.ln(line_height)

pdf.ln()
pdf.set_font(style='B')
pdf.cell(txt="Final Rating Value = " + str(round(final_rating_value, 1)),ln=1, align='L')
pdf.ln()
pdf.cell(txt="Condition : " + cond, ln=1, align='L')


#pdf.output('table_with_cells.pdf')

pdf.output('Data.pdf')

print("PDF Generated")


# import os 

# os.startfile(r'C:\Users\jaggu\Code\Projects\Highway-Project\Data.pdf')