#write a program to find monthly emi with intrest

#method-1

# amount=int(input("enter the total amount:"))
# tenture=int(input("enter the total tenure:"))
# interst=int(input("enter the intrest:"))

# //EMI = P * r * (1 + r)*n / (1 + r)*n - 1

# emi = amount*interst*(1+interst)**tenture / ((1+interst)**tenture-1) 
# print(f"Loan Amount= Rs {amount}\nLoan Tenture={tenture} Months\nInterst Rate={interst}\nEMI = Rs {emi}")

#method-2

p=float(input("enter the loan amount:\n"))
r=float(input("enter the intrest rate:\n"))
n=int(input("how many year to pay the loan:\n"))


# p = loan amount
# r = intrest rate
# n = month

# //EMI = P * r * (1 + r)*n / (1 + r)*n - 1

print("loan amount",p)

r=r/100/12  # convert annual intrest rate into monthly interest rate
print("intrest rate =",r)


n=n*12  # convert year to month

print(f"months ={n}")


emi=((p)(r)((1+r)*n))/(((1+r)*n)-1)  # apply equation 

print(f"your monthly emi = {emi}")

# total amount of pay loan
total_amount=emi*n
print("total amount of payment in loan",total_amount)

# total amount of intrest loan
total_intrest=total_amount-p
print("total amount of intrest in loan",total_intrest)