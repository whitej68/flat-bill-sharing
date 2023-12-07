import webbrowser
from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as total amount
    and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image(name="house.png", w=30, h=30)

        # Insert titles
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


amount = float(input("Enter the bill amount: "))
period = input("Enter the bill period? E.g December 2023: ")

flatmate1_name = input("Enter the first flatmates name: ")
flatmate1_days = int(input(f"How many days did {flatmate1_name} spend in the house?: "))

flatmate2_name = input("Enter the second flatmates name: ")
flatmate2_days = int(input(f"How many days did {flatmate2_name} spend in the house?: "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_days)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_days)

print(f"{flatmate1.name} pays: ", round(flatmate1.pays(bill=the_bill, flatmate2=flatmate2), 2))
print(f"{flatmate2.name} pays: ", round(flatmate2.pays(bill=the_bill, flatmate2=flatmate1), 2))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)
