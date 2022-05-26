import tkinter as tk
from fpdf import FPDF
from nhsh import *
from mdr import *
from ur import *


root= tk.Tk()
options = [
    "NH/SH",
    "MDR/ODR/VR",
    "UR"
]
  
# datatype of menu text
clicked = tk.StringVar()
  
# initial menu text
clicked.set( "NH/SH" )

# Create Dropdown menu
drop = tk.OptionMenu( root , clicked , *options )
drop.pack()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

label1 = tk.Label(root, text= "Cracking (%)")
canvas1.create_window(100,100,window=label1)
entry1 = tk.Entry (root) 
canvas1.create_window(200, 100, window=entry1)

label2 = tk.Label(root, text= "Ravelling (%)")
canvas1.create_window(100,120,window=label2)
entry2 = tk.Entry (root) 
canvas1.create_window(200, 120, window=entry2)

label3 = tk.Label(root, text= "Potholes (%)")
canvas1.create_window(100,140,window=label3)
entry3 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry3)

label4 = tk.Label(root, text= "Shoving (%)")
canvas1.create_window(100,160,window=label4)
entry4 = tk.Entry (root) 
canvas1.create_window(200, 160, window=entry4)

label5 = tk.Label(root, text= "Patching (%)")
canvas1.create_window(100,180,window=label5)
entry5 = tk.Entry (root) 
canvas1.create_window(200, 180, window=entry5)

label6 = tk.Label(root, text= "Settlements (%)")
canvas1.create_window(100,200,window=label6)
entry6 = tk.Entry (root) 
canvas1.create_window(200, 200, window=entry6)

label7 = tk.Label(root, text= "Rut Depth (%)")
canvas1.create_window(100,220,window=label7)
entry7 = tk.Entry (root) 
canvas1.create_window(200, 220, window=entry7)

number = 0
def func():  
    global x1,x2,x3,x4,x5,x6,x7 
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    x3 = float(entry3.get())
    x4 = float(entry4.get())
    x5 = float(entry5.get())
    x6 = float(entry6.get())
    x7 = float(entry7.get())
    global OPTION
    OPTION = clicked.get()
    label1 = tk.Label(root, text= OPTION)
    canvas1.create_window(200, 250, window=label1)   
    
    
button1 = tk.Button(text='Submit', command=func)
canvas1.create_window(200, 280, window=button1)

root.mainloop()










inputs = []
if(OPTION == options[0]):
    wt = [1.0,0.75,0.5,1.0,0.75,0.75,1.0]
    inputs.append(x1)
    inputs.append(x2)
    inputs.append(x3)
    inputs.append(x4)
    inputs.append(x5)
    inputs.append(x6)
    inputs.append(x7)
elif(OPTION == options[1]):
    wt = [1.0,0.75,0.5,0.75,0.75]
    inputs.append(x1)
    inputs.append(x2)
    inputs.append(x3)
    inputs.append(x5)
    inputs.append(x6)
elif(OPTION == options[2]):
    wt = [1.0,0.75,0.5,0.75,1.0]
    inputs.append(x1)
    inputs.append(x2)
    inputs.append(x3)
    inputs.append(x6)
    inputs.append(x7)


sum = 0
final_list = [] #new comment
for i in range(len(inputs)):
    final,condition = computeNHSH(i+1,inputs[i])
    final_list.append(final)
    sum = sum +round(final*wt[i],3)

final_rating_value = sum/len(inputs)
if(final_rating_value <= 1):
    cond = "Poor"
elif(final_rating_value >= 1.1 and final_rating_value <= 2):
    cond = "Fair"
elif(final_rating_value >= 2.1 and final_rating_value<=3):
    cond = "Good"


if(OPTION == options[0]):
    data = (
    ("Distress Type", "Input(%)", "Rating", "Weightage","Wt Rating Value"),
    ("Cracking",str(inputs[0]),str(final_list[0]),str(wt[0]),str(round(final_list[0]*wt[0],1))),
    ("Ravelling",str(inputs[1]),str(final_list[1]),str(wt[1]),str(round(final_list[1]*wt[1],1))),
    ("Potholes",str(inputs[2]),str(final_list[2]),str(wt[2]),str(round(final_list[2]*wt[2],1))),
    ("Shoving",str(inputs[3]),str(final_list[3]),str(wt[3]),str(round(final_list[3]*wt[3],1))),
    ("Patching",str(inputs[4]),str(final_list[4]),str(wt[4]),str(round(final_list[4]*wt[4],1))),
    ("Settlements",str(inputs[5]),str(final_list[5]),str(wt[5]),str(round(final_list[5]*wt[5],1))),
    ("Run Depth",str(inputs[6]),str(final_list[6]),str(wt[6]),str(round(final_list[6]*wt[6],1))),
    )

if(OPTION == options[1]):
    data = (
    ("Distress Type", "Input(%)", "Rating", "Weightage","Wt Rating Value"),
    ("Cracking",str(inputs[0]),str(final_list[0]),str(wt[0]),str(round(final_list[0]*wt[0],1))),
    ("Ravelling",str(inputs[1]),str(final_list[1]),str(wt[1]),str(round(final_list[1]*wt[1],1))),
    ("Potholes",str(inputs[2]),str(final_list[2]),str(wt[2]),str(round(final_list[2]*wt[2],1))),
    ("Patching",str(inputs[3]),str(final_list[3]),str(wt[3]),str(round(final_list[3]*wt[3],1))),
    ("Settlements",str(inputs[4]),str(final_list[4]),str(wt[4]),str(round(final_list[4]*wt[4],1))),
    )
if(OPTION == options[2]):
    data = (
    ("Distress Type", "Input(%)", "Rating", "Weightage","Wt Rating Value"),
    ("Cracking",str(inputs[0]),str(final_list[0]),str(wt[0]),str(round(final_list[0]*wt[0],1))),
    ("Ravelling",str(inputs[1]),str(final_list[1]),str(wt[1]),str(round(final_list[1]*wt[1],1))),
    ("Potholes",str(inputs[2]),str(final_list[2]),str(wt[2]),str(round(final_list[2]*wt[2],1))),
    ("Settlements",str(inputs[3]),str(final_list[3]),str(wt[3]),str(round(final_list[3]*wt[3],1))),
    ("Rut depth",str(inputs[4]),str(final_list[4]),str(wt[4]),str(round(final_list[4]*wt[4],1))),
    )

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=10)
line_height = pdf.font_size * 2.5
col_width = pdf.epw / 5 

lh_list = [] #list with proper line_height for each row
use_default_height = 0 #flag

#create lh_list of line_heights which size is equal to num rows of data
for row in data:
    for datum in row:
        word_list = datum.split()
        number_of_words = len(word_list) #how many words
        if number_of_words>2: #names and cities formed by 2 words like Los Angeles are ok)
            use_default_height = 1
            new_line_height = pdf.font_size * (number_of_words/2) #new height change according to data 
    if not use_default_height:
        lh_list.append(line_height)
    else:
        lh_list.append(new_line_height)
        use_default_height = 0

#create your fpdf table ..passing also max_line_height!
for j,row in enumerate(data):
    for datum in row:
        line_height = lh_list[j] #choose right height for current row
        pdf.multi_cell(col_width, line_height, datum, border=1,align='L',ln=3, 
        max_line_height=pdf.font_size)
    pdf.ln(line_height)

pdf.cell(20, 100, txt = "Final Rating Value = " + str(round(final_rating_value,1)), 
            ln = 1, align = 'L')
pdf.cell(txt="Condition : " + cond,ln = 1,align='L')


pdf.output('table_with_cells.pdf')


# root= tk.Tk()

# canvas1 = tk.Canvas(root, width = 300, height = 300)
# canvas1.pack()

# def hello ():  
#     label1 = tk.Label(root, text= 'Hello World!', fg='green', font=('helvetica', 12, 'bold'))
#     canvas1.create_window(150, 200, window=label1)
    
# button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
# canvas1.create_window(150, 150, window=button1)

# root.mainloop()