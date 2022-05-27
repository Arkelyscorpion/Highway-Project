from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica',size = 12)
pdf.cell(txt = "Hello world")
pdf.cell(txt = "second line")

pdf.multi_cell(txt = "RATING OF PAVEMENTS BASED ON QUANTITY OF DISTRESS",align = 'C')


pdf.output("test.pdf")  