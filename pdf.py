# -------------------------------------------------------------------------------------- 

#                                     PDF PART 

# --------------------------------------------------------------------------------------

from fpdf import FPDF
from idata import IData


def generatePDF(options,OPTION,data,final_rating_value,cond,fileName):

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
    lh_list = []  # LIST WITH PROPER LINE_HEIGHT FOR EACH ROW
    use_default_height = 0  # FLAG

    # CATEGORY OF THE ROAD BASED ON THE OPTION SELECTED BY THE USER

    if(OPTION == options[0]):
        road_type = "National Highways / State Highways"
    elif(OPTION == options[1]):
        road_type = "MDR(s) and Rural Roads"
    else:
        road_type = "Urban Roads"

    pdf.ln()

    pdf.cell(txt="Category of Road : " + IData['category'], align='L')
    pdf.ln()
    pdf.ln()

    pdf.cell(txt= f"Name of the Road : " + IData['name'], align='L')
    pdf.ln()
    pdf.ln()

    pdf.cell(txt="Carraigeway Width(m) : " + str(IData['carriage']), align='L')
    pdf.ln()
    pdf.ln()

    pdf.cell(txt="Chainage of Test Section : " + IData['chainage'], align='L')
    pdf.ln()
    pdf.ln()

    pdf.cell(txt="Date of Observation : " + str(IData['date']), align='L')
    pdf.ln()
    pdf.ln()

    pdf.cell(txt="Type of Surface : " + IData['surface'], align='L')
    pdf.ln()
    pdf.ln()

    pdf.cell(txt="Weather Condition : " + IData['weather'], align='L')
    pdf.ln()
    pdf.ln()

    pdf.ln()

    # TABLE PART

    pdf.set_font("Helvetica", size=10)

    # CREATE LH_LIST OF LINE_HEIGHTS WHICH SIZE IS EQUAL TO NUM ROWS OF DATA
    for row in data:
        for datum in row:
            word_list = datum.split()
            number_of_words = len(word_list)  # HOW MANY WORDS
            if number_of_words > 2:
                use_default_height = 1
                # NEW HEIGHT CHANGE ACCORDING TO DATA
                new_line_height = pdf.font_size * (number_of_words/2)
        if not use_default_height:
            lh_list.append(line_height)
        else:
            lh_list.append(new_line_height)
            use_default_height = 0
    # CREATING FPDF TABLE... PASSING MAX_LINE_HEIGHT
    for j, row in enumerate(data):
        for datum in row:
            if(j == 0):
                pdf.set_font(style='B')
            else:
                pdf.set_font()
            line_height = lh_list[j]  # CHOOSE RIGHT HEIGHT FOR CURRENT ROW
            pdf.multi_cell(col_width, line_height, datum, border=1, align='L', ln=3,
                        max_line_height=pdf.font_size)
        pdf.ln(line_height)
    

    pdf.set_font(style='B')
    pdf.multi_cell(4*pdf.epw/5,line_height,"Final Rating Value",border=1,align='C',ln=3,max_line_height=pdf.font_size);
    pdf.multi_cell(pdf.epw/5,line_height,str(round(final_rating_value, 1)),border=1,align='C',ln=3,max_line_height=pdf.font_size);
    pdf.ln(line_height)
    pdf.multi_cell(4*pdf.epw/5,line_height,"Condition",border=1,align='C',ln=3,max_line_height=pdf.font_size);
    pdf.multi_cell(pdf.epw/5,line_height,cond,border=1,align='C',ln=3,max_line_height=pdf.font_size);
    pdf.ln(line_height)

    # pdf.ln()
    # pdf.set_font(style='B')
    # pdf.cell(txt="Final Rating Value = " + str(round(final_rating_value, 1)),ln=1, align='L')
    # pdf.ln()
    # pdf.cell(txt="Condition : " + cond, ln=1, align='L')

    pdf.output(r"{}.pdf".format(fileName))

    print("PDF Generated")  