# -------------------------------------------------------------------------------------- 

#                                     PDF PART 

# --------------------------------------------------------------------------------------

from fpdf import FPDF
from idata import IData

def generatePDF(options,OPTION,data,final_rating_value,cond):

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