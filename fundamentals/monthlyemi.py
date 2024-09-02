#write a program to find monthy emi
#loan_amount
#tenure
#interest_rate
amount=200000
tenture=120
interst=0.0075
emi = amount*interst*(1+interst)**tenture / ((1+interst)**tenture-1) 
print(f"Loan Amount= Rs {amount}\nLoan Tenture={tenture} Months\nInterst Rate={interst}\nEMI = Rs {emi}")