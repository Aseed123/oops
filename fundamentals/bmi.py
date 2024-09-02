#write a program to calculate bmi
#bmi=(weight_in_kg / heigh_in_meter squre)

weight_in_kg=72
height_in_cm=165

height_in_meter=height_in_cm/100
bmi=weight_in_kg/height_in_meter**2
print(f"bmi of person={bmi}")