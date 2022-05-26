from fpdf import FPDF
import tkinter as tk

from nhsh import *
from mdr import *
from ur import *

wt = [1.0,0.75,0.5,1.0,0.75,0.75,1.0]

inputs = [9,8,0,0.09,5,4,9]


sum = 0
for i in range(len(inputs)):
    final,condition = computeNHSH(i+1,inputs[i])
    sum = sum +round(final*wt[i],3)

final_rating_value = sum/len(inputs)
if(final_rating_value <= 1):
    cond = "Poor"
elif(final_rating_value >= 1.1 and final_rating_value <= 2):
    cond = "Fair"
elif(final_rating_value >= 2.1 and final_rating_value<=3):
    cond = "Good"



data = (
    ("Distress Type", "Input(%)", "Rating", "Weightage","Wt Rating Value"),
    ("Cracking",cond,"1.2","1.0","1.2"),
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

pdf.cell(20, 100, txt = "Final Rating Value = " + str(final_rating_value), 
            ln = 1, align = 'L')

pdf.cell(20, 100, txt = "Condition = " + cond, 
            ln = 1, align = 'L')


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