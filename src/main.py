from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

def addCompanyTitle(pdf):
    pdf.set_font("Arial",size=18)
    pdf.cell(200,10, txt = "My company", ln=1, align="L")

def addCustomer(pdf):
    pdf.set_font("Arial",size=12)
    pdf.cell(0, 10, txt = "My Customer", ln=1, align="R")
    pdf.cell(0, 10, txt = "My Customer adresse", ln=1, align="R")
    pdf.cell(0, 10, txt = "My Customer country", ln=1, align="R")


def addBillElements(pdf, elements):
    pdf.set_font("Arial",size=12)
    pdf.cell(0, 10, txt = "----------------------", ln=1, align="L")
    for e in elements:
        pdf.cell(0, 10, txt = e + " |         50$ "  , ln=1, align="L")
    pdf.cell(0, 10, txt = "----------------------", ln=1, align="L")

def addFooter(pdf, count):
    pdf.set_font("Arial",size=12)
    pdf.cell(0, 10, txt = "----------------------", ln=1, align="R")
    pdf.cell(0, 10, txt = "Total : " + str(count * 50)+ "$           ", ln=1, align="R")
    pdf.cell(0, 10, txt = "----------------------", ln=1, align="R")


addCompanyTitle(pdf)
addCustomer(pdf)
elements = []
count = 0
while (count < 10):
    elements.append("my element n° "+ str(count)) 
    count +=1
addBillElements(pdf, elements)
addFooter(pdf, count)

pdf.output("./../out/out.pdf")
pdf.close()