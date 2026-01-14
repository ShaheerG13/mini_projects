wage = 25
hours = 40
total = wage * hours
tax = 0.18 * total
insurance = 0.08 * total
print(f"Hourly rate: {wage} \nNumber of hours: {hours} \nTotal income: {total} \nTax: {tax} \nInsurance: {insurance}")
print(f"The net income is {total - tax - insurance} dollars")
