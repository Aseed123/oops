# write a program to find bmi ?

# // bmi=(weight_in_kg/height_in_metersqure)

weight=int(input("enter the weight in kg\n"))

height=int(input("enter the height in cm\n"))

height=(height/100)

print(f"weight = {weight} kg")

print(f"height= {height} cm")

bmi=weight/height**2

if(bmi<=19):#0-19

    print(f"under weight your bmi = {bmi}")

elif(bmi<=25):#20-25

    print(f"Normal weight your bmi = {bmi}")

elif(bmi<=30):#26-30

    print(f"over weight your bmi = {bmi}")

else:

    print("obesity")