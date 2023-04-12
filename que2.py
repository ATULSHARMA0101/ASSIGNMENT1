gross=int(input("gross amount"))
dependent=int(input("no of dependents"))
taxable_income=gross-10000-(3000*dependent)
print(taxable_income)
tax=taxable_income/5
print(tax)