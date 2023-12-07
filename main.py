from flat import Bill, Flatmate
from reports import PdfReport

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
