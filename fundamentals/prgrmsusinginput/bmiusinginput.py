#write a program to calculate the bmi of a person

weight_in_kg=int(input("enter the weight in kg:"))
height_in_cm=int(input("enter the height in cm:"))

height_in_meter=height_in_cm/100
bmi=weight_in_kg/height_in_meter**2
print(f"bmi ={bmi}")