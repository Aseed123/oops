# # write to print to find the monthly emi with intrest ?

# p = float(input("Enter the loan amount: "))
# annual_rate = float(input("Enter the annual interest rate: "))
# n = int(input("Enter the no. of years to  the loan: "))


# # p = loan amount
# # annual_rate = intrest rate
# # n = month

# # //EMI = P * r * (1 + r)**n / (1 + r)**n - 1
# print(f"loan amount :{p}")
# # convert annual intrest rate into monthly interest rate
# r=r/100/12
# print(f"intrest rate :{annual_rate}")

# # convert year to month
# n=n*12
# print(f"months ={n}")

# # apply equation 
# emi=((p)(r)((1+r)*n))/(((1+r)*n)-1)
# print(f"your monthly emi = {emi}")

# # total amount of pay loan
# total_amount=emi*n
# print("total amount of payment in loan",total_amount)

# # total amount of intrest loan
# total_intrest=total_amount-p
# print("total amount of intrest in loan",total_intrest)

#find Second largest among three numbers

num1=int(input("Enter first number:"))
num2=int(input("Enter Second number:"))
num3=int(input("Enter Third number:"))

if num1>num2 and num1<num3:
    print(f"{num1} is the Second Largest")
elif num2>num1 and num2<num3:
    print(f"{num2} is the Second Largest")
elif num3>num1 and num3<num2:
    print(f"{num3} is the Second Largest")