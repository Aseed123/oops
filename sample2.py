# write to print to find the monthly emi with intrest ?

p=float(input("enter the loan amount\n"))
r=float(input("enter the intrest rate\n"))
n=int(input("how many year to pay the loan\n"))

# //EMI = P * r * (1 + r)**n / (1 + r)**n - 1
# p = loan amount
# r = intrest rate
# n = month
print("loan amount",p)
# convert annual intrest rate into monthly interest rate
r=r/100/12
print("intrest rate =",r)

# convert year to month
n=n*12
print(f"months ={n}")

# apply equation 
emi=((p)(r)((1+r)*n))/(((1+r)*n)-1)
print(f"your monthly emi = {emi}")

# total amount of pay loan
total_amount=emi*n
print("total amount of payment in loan",total_amount)

# total amount of intrest loan
total_intrest=total_amount-p
print("total amount of intrest in loan",total_intrest)